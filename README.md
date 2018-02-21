# Metax
Python GUI, lets you scan a directory for GPS location metadata in files, visualize each result from list, showing generated map next to original photo


## Description

Metax is a python GUI script, which lets you scan a directory for GPS location metadata (using exiftool).
The files with location data get visually listed, you can see the original picture (BMP, JPEG, JPG, PNG, GIF, and more...)
next to the corresponding map image of coordinates of each file with place name above it (using Map Quest API).

Optionally use duplicates removal (by MD5 checksums), on files in chosen dir (using fdupes), \
Optionally extract zip files (both available with checkboxes)

Button to copy coordinates of file \
Button to copy place name of file (usually of photo)

The program minimize API use: copies existing maps for same location, scan each file once according to its content sig (with MD5)

The script uses a few excellent programs:
* exiftool by Phil Harvey (https://sno.phy.queensu.ca/~phil/exiftool/)
* fdupes by Adrian Lopez (https://github.com/adrianlopezroche/fdupes)
* Map Quest API (https://wiki.openstreetmap.org/wiki/Main_Page)


## Demonstration (GIF)

![metax example](https://i.imgur.com/HrGqFzR.gif)


## Installation

**NOTE:** The program was tested on kali linux

* The installation script gets all required dependencies (written below), makes symbolic link of program in /usr/local/bin 

* Go to dir where you want metax data to be permanently, then run the following command: \
``` sudo apt-get install git && git clone 'https://github.com/BluesNote1/metax' && cd metax && chmod +x install.sh && ./install.sh ```

* GO TO "https://developer.mapquest.com/user/register" \
**REGISTER AND GENERATE A PERSONAL API KEY**, put it in "map_quest_api.key" file

If everthing was installed successfully, you can run the program by typing 'metax' in a terminal


## Dependencies

**NOTE:** The script was tested and used on kali linux

* GO TO "https://developer.mapquest.com/user/register" \
**REGISTER AND GENERATE A PERSONAL API KEY**, put it in "map_quest_api.key" file

* fdupes: should be available for installation from a package manager (apt-get install fdupes)
* exiftool: should be available for installation from a package manager (apt-get install libimage-exiftool-perl)
* python3: should be available for installation from a package manager (apt-get install python3 python3-pip)
* pyqt4: GUI module, should be available for installation from a package manager (apt-get install python-qt4)
* requests: python module (pip3 install requests)

