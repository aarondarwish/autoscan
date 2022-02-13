# Set below your device endpoint.
# ------------------------------------------------------------------------------------------------------
device_string = "escl:https://192.168.0.20:443" # Find out your device info using "scanimage -L" command
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
import subprocess, os, sys
# Set colours for warning.
class bcolors:
    WARNING = '\033[31m'
    ENDC = '\033[0m'

# Check if the required packages exists. If not, exit the program.
check_scanimage = "/" in str(subprocess.check_output(["whereis", "scanimage"]))
check_jpegoptim = "/" in str(subprocess.check_output(["whereis", "jpegoptim"]))
check_imagemagick = "/" in str(subprocess.check_output(["whereis", "convert"]))

if (check_scanimage == False):
    sys.exit("Please install SANE to acquire the scanimage package.")
if (check_jpegoptim == False):
    sys.exit("Please install jpegoptim.")
if (check_imagemagick == False):
    sys.exit("Please install imagemagick.")

# Ask for the resolution and starting number to be used in naming the image files.
index = input("\nEnter the initial index number:\t")
flipped = 1
resolution = str(input("\n Enter resolution in DPI in the range of 1-1400 (the default set-point is 300 DPI):\t"))
if resolution == '':
    resolution = "300"

# Perform the scanning according to the user's set-points.
while True:
    command = "scanimage --device " + device_string + " --format=jpeg --mode=grey --resolution=" + resolution + " -x 210 -y 297 --progress --output-file=page_" + str(index) + ".jpeg"
    os.system(command)
    index = int(index)
    index += 1
    flipped *= -1

    if flipped == 1:
        scan_message = "\n[" + bcolors.WARNING + "Flipped" + bcolors.ENDC + "] - Scan again? Press 'ENTER' to continue, or 's' for skip to scanning without flipping.\t"
    else:
        scan_message = "\nScan again? Press 'ENTER' to continue, or 's' for skip to scanning without flipping.\t"

    again = input(scan_message)

    if again == '':
        continue
    elif again =='s':
        flipped *= -1
        continue
    else:
        break;

# Optimize and convert the images into a pdf.
os.system("jpegoptim ./*.jpeg && convert ./*.jpeg scan.pdf")
