import os 

device_string = "escl:https://192.168.0.26:443" # Find out your device info using "scanimage -L" command
index = input("\nEnter the initial index number:\t")
flipped = 1

while True:
    command = "scanimage --device" + device_string + "--format=jpeg --mode=grey --resolution=300 -x 210 -y 297 --progress --output-file=page_" + str(index) + ".jpeg"
    os.system(command)
    index = int(index)
    index += 1
    flipped *= -1
    if flipped == 1:
        scan_message = "\n(Flipped) - Scan again? [y/n]\t"
    else:
        scan_message = "\nScan again? [y/n]\t"
    if input(scan_message) == "y":
        continue
    else:
        break;
