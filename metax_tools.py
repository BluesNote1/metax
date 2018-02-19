#!/usr/bin/env python3

# METAX Copyright (c) 2018 Maor Blaustein
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 
## Functions for MetaX program
##

import os
import string
import json
import requests
import shutil
from urllib.request import urlopen
#from pprint import pprint

# Changing python dir to program binary dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Reading API key from 'maps_quest_api.key' file
try:
    with open('maps_quest_api.key') as key_file:
        api_key = key_file.read().strip()
except FileNotFoundError as err:
    print(' [#] Generate API ket at "https://developer.mapquest.com/user/register" and put in "maps_quest_api.key" file of binary')
    api_key = ''

def check_meta(dirname, unzip_flag=False, dups_flag=False, convert_gps=True):
    '''Checks meta-data with exiftool on *dirname* files,
       optionally uncompresses zip, removes duplicate files by MD5 in *dirname*.
       
       returns filenames list and locations list both in tuple
       (when *convert_gps* is True, each location is in tuple, ex: (lat, lon)),
       or empty tuples (nothing found/failure)
       
    dirname: str
    return: 2 lists in tuple
    '''
    # Checking flags and setting options (unzip, dups remove)
    cmd_exif = 'exiftool -ext "*"'
    cmd_dups = 'fdupes -d -N'
    if unzip_flag:
        unzipper(dirname)
    if dups_flag:
        cmd_dups += ' "%s" 1> /dev/null' % dirname
        os.system(cmd_dups)
    cmd_exif += """ "%s" | grep -E 'GPS Position|========'""" % dirname
    # exiftool extracts locations data
    output = os.popen(cmd_exif).read()
    
    filepathes = []
    locations = []
    name = ''
    loc = ''
    
    lines = output.split('\n')
    for i in range(len(lines)):
        # Avoid wrong indexing
        if lines[i] is lines[-1]:
            break
        # looking for filename in a line, location in the next
        if not (lines[i].startswith('========')
                and
                lines[i+1].startswith('GPS')):
            continue
        # Adding data
        name = lines[i].partition('========')[2].strip()
        loc = lines[i+1].split(':')[1].strip()
        if convert_gps:
            loc = gps_time2decimal(loc) # GPS Conversion (time to decimal)
        filepathes.append(name)
        locations.append(loc)
        name = ''
        loc = ''
    return (tuple(filepathes), tuple(locations))
        
def unzipper(path):
    '''Unzips all zip compressed files in given *path* dir
    return: int 1 - error, 0 - success
    '''
    last_dir = os.getcwd()
    # Changing dir because of unzip bash command nature of work
    os.chdir(path)
    try:
        for filename in os.listdir('.'):
            if filename.lower().endswith('.zip'):
                os.system('unzip -o "%s" 1> /dev/null' % filename)
    except Exception as err:
        print(' [#] Error while unzipping: %s' % err)
        os.chdir(last_dir)
        return 1
    os.chdir(last_dir)
    return 0
        
def gps_time2decimal(coor):
    '''Converts GPS coordinates minutes seconds type to decimal type
       (Meant to work with 'exiftool' 'GPS Position' output line)
       
    coor: string of minutes seconds coordinates (ex: 25 deg 5' 16.26" N, 34 deg 46' 29.21" E) - exiftool output
                                                (ex: 20° 26′ 46″, 79° 58′ 56″)
                                                (ex: 44 26 46, 79 58 56)
                                                
    return: tuple of 2 float, of decimal degrees (ex: 42.0390905, 37.7816849 - 7 digits precision) 
    '''
    # Removing letters
    for l in 'NWSE':
        coor = coor.replace(l, '')
    coor = coor.replace('deg', '')
    # Splitting latitude, longtitude
    try:
        x, y = coor.split(',')
    except ValueError:
        return (0.0, 0.0)
    # Cleaning data, converting gps syntax
    ncoors = []
    for i in x, y:
        parts = [float(v.strip(string.punctuation + string.ascii_letters + '°'))
                 for v in i.split()]
        ncoors.append(round(parts[0] + \
                            parts[1]/60 + \
                            parts[2]/3600, 7)) # 7 precision digits after decimal point
    return tuple(ncoors)

def get_map(x, y, filename=False):
    '''Getting JPG map data of x, y (lat, lon) coordinates
       Using Map Quest API (static map call)
    
    x: latitude float
    y: longtitude float
    filename (optional): string for saving JPG as filename (in current working dir)
    
    return: JPG map data, or False (failure)
    '''
    # URL for Map Quest API (static map call)
    url = 'https://open.mapquestapi.com/staticmap/v4/getmap?key=%s&imagetype=jpg&size=300,300&zoom=15&pois=red_1,%.7f,%.7f,0,0' \
          % (api_key, x, y)
    # JPG Request
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        res.raw.decode_content = True
        # File write option
        if filename and type(filename) == str:  
            with open(filename, 'wb') as file:
                shutil.copyfileobj(res.raw, file)
        return res.raw
    else:
        return False
    
def get_placename(x, y):
    '''Gets location details (country, city, street, etc..) from coordinates (nearest place)
    
    x: latitude float
    y: longtitude float
    
    return: str of place details, or empty str (failure)
    '''
    url = 'https://open.mapquestapi.com/nominatim/v1/reverse.php?key=%s&format=json&lat=%.7f&lon=%.7f'\
          % (api_key, x, y)
    try:
        res = urlopen(url)
    except Exception as err:
        print(' [#] Error getting place name: %s' % err)
        return ''
    data = json.load(res)
    # Return address, trying with constant templates
    # (works better according to data amount)
    try:
        return '%s %s, %s, %s'\
        % (data['address']['road'],\
           data['address']['house_number'],\
           data['address']['city'],\
           data['address']['country'])
    except KeyError:
        try:
            return '%s, %s, %s'\
            % (data['address']['road'],\
               data['address']['city'],\
               data['address']['country'])
        except KeyError:
            try:
                return '%s, %s, %s'\
                % (data['address']['road'],\
                   data['address']['village'],\
                   data['address']['country'])
            except KeyError:
                dat = data['display_name'].split(',')
                dat = ','.join(dat[:4])
                return dat
            
def md5sum(name):
    '''Returns MD5 checksum of file or of string given *name*
    name: str
    return: str
    '''
    if not type(name) == str:
        return ''
    if os.path.isfile(name):
        output = os.popen("""md5sum '%s'""" % name).read()
    else:
        output = os.popen("""echo '%s' | md5sum""" % name).read()
    return output.split()[0]
            
if __name__ == '__main__':
    pass