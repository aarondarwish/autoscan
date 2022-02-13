# Purpose of the script
Automatically scan A4 papers, and keep track of when a page is flipped.

After the scanning is finished, optimize the images then convert them into a `pdf` file.

## Requirements
You need the `imagemagick` and `jpegoptim` packages installed, as well as the `SANE` (Scanner Access Now Easy) library suit.

## Use
Firstly find your scanner by issuing `scanimage -L` and then copy the endpoint and assign it to the `device_string` variable inside the `autoscan.py` file.

Then simply run the `autoscan.py` script using a python interpreter:
```console
python autoscan.py
```
