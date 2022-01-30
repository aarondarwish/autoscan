device_string = "escl:https://192.168.0.21:443" # Find out your device info using "scanimage -L" command

class bcolors:
    WARNING = '\033[31m'
    ENDC = '\033[0m'

import os 
index = input("\nEnter the initial index number:\t")
resolution = input("\n Enter resolution in DPI in the range of 1-1400:\t")
flipped = 1

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
