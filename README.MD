# Purpose of the script
It automatically scans A4 papers, and enables you to keep track of when a page is flipped.
When the scanning is finished, it optimizes the images and then converts them into a `pdf` file.

## Requirements
You need the `imagemagick` and `jpegoptim` packages installed, as well as the `SANE` (Scanner Access Now Easy) library suit.

## Use
Firstly find your scanner by issuing `scanimage -L` and then copy the endpoint and assign it to the `device_string` variable inside the `autoscan.py` file.

Then simply run the `autoscan.py` script using a python interpreter:
```console
python autoscan.py
```
