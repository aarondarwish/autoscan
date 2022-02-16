# Set below your device endpoint.
# ------------------------------------------------------------------------------------------------------
device_string = "escl:https://192.168.0.20:443" # Find out your device info using "scanimage -L" command
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------


import subprocess, os, sys

# Fetch one character from the standard input stream.
def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # On POSIX/UNIX systems, return a getch that manipulates the tty.
    import tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch
getch = _find_getch()

# Set colours for warning.
class colour:
    warning = '\033[31m'
    note = '\033[34m'
    end = '\033[0m'

# Check if the required packages exists.
check_scanimage = "/" in str(subprocess.check_output(["whereis", "scanimage"]))
check_jpegoptim = "/" in str(subprocess.check_output(["whereis", "jpegoptim"]))
check_imagemagick = "/" in str(subprocess.check_output(["whereis", "convert"]))

# If they do not exist, then inform the user then exit the program.
if (check_scanimage == False):
    sys.exit("\nPlease install SANE to acquire the " + colour.warning + "scanimage" + colour.end + " package.\n")
if (check_jpegoptim == False):
    sys.exit("\nPlease install " + colour.warning + "jpegoptim" + colour.end + ".\n")
if (check_imagemagick == False):
    sys.exit("\nPlease install " + colour.warning + "imagemagick" + colour.end + ".\n")

# Ask for the starting number to be used in naming the image files.
while True:
    index = input("\nEnter the initial page number:\t")
    try:
        int(index)
        break
    except ValueError:
        print(colour.warning + "\nPlease enter a number.\n" + colour.end)

# Ensure that index is a number and in the range of 1-1400.
while True:
    resolution = input("\nEnter resolution in DPI in the range of 1-1400 (Just press ENTER for the default set-point, which is 300 DPI).\
            \n"+ colour.note + "⚠ Please note that the higher the DPI set-point, the slower the scanning will be. ⚠" + colour.end + \
            "\nDPI value:\t")

    # Set the default resolution in case no value is provided.
    if resolution == '':
        resolution = "300"
        break

    # Check if the value is within range.
    try:
        resolution = int(resolution)
        if resolution in range(1, 1401):
            resolution = str(resolution) # The command flag must be a string.
            break
        else:
            print(colour.warning + "\n⚠ Please enter a number that is within the range. ⚠" + colour.end)
    except ValueError:
        print(colour.warning + "⚠ You did not enter a number. ⚠\n" + colour.end)

# Set a valid scanner's colour mode flag.
while True:
    print("\nWould you like the scanned image to be:\n\t Coloured [1]\t\t Black & white [2]?\n")
    colour_mode = getch()
    # Test for valid colour mode inputs.
    try:
        colour_mode = int(colour_mode)
        if colour_mode == 1:
            colour_mode = "color"
            break
        elif colour_mode == 2:
            colour_mode = "grey"
            break
    except ValueError:
        print(colour.warning + "\n⚠ Cannot recognise your colour mode option selection. ⚠\n" + colour.end)

# By default, the page isn't flipped.
flipped = False

# Attempt the scanning according to the user's set-points.
while True:
    # Perform the scan.
    print(colour.warning + "\nAttempting the scan...\n" + colour.end)
    command = "scanimage --device " + device_string + " --format=jpeg --mode=color --resolution=" + resolution + " \
            -x 210 -y 297 --progress --output-file=page_" + str(index) + ".jpeg"
    os.system(command)

    # Increase the counter.
    index = int(index)
    index += 1

    # Flag the page as flipped depending on user input.
    if flipped == True:
        scan_message = "\n[" + colour.warning + "Flipped" + colour.end + "] - Scan again? Press 'ENTER' \
                to continue, or 's' for skip to scanning without flipping.\t"
    else:
        scan_message = "\nScan again? Press 'ENTER' to continue, or 's' for skip to scanning without flipping.\t"

   # Ask the user to confirm what the next course of action is. Whether it is to skip the flag and scan, or flag or stop scanning.
    again = input(scan_message)
    if again == '':
        # If the page has been flipped previously, remove the flip tag. Otherwise, then enable it.
        flipped *= False 
        continue
    elif again =='s':
        flipped = False 
        continue
    else:
        break;

# Optimize and convert the images into a pdf.
os.system("jpegoptim ./*.jpeg && convert ./*.jpeg scan.pdf")
