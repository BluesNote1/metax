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

import os
import sys
import shutil
from metax_tools import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_tracefilesdlg
 
class TraceFilesDlg(QDialog,
                    ui_tracefilesdlg.Ui_TraceFilesDlg):
    def __init__(self, parent=None):
        super(TraceFilesDlg, self).__init__(parent)
        # Sets Qt Designer things
        self.setupUi(self) 
        # Disable scan button when empty text field
        self.updateUi()
        # Changing python dir to program binary dir
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        # Setting user home path for QFileDialog (choosing directories)
        self.home_dir = os.path.expanduser('~')
        # Check box flags
        self.unzip_flag = False
        self.dups_flag = False
        # Same location for different file flag (used because of nested loops)
        self.same_loc_flag = False
        # hash names and hash places colletions (avoid API re-calls)
        self.maps_hashes = dict()
        # pyqt4 clipboard settings for copy functions
        self.clipboard = QApplication.clipboard()
        # Setting
        self.scan_button.setEnabled(True)

    # Enables/disables scan button    
    def updateUi(self):
        '''Enables/disables button'''
        enable = ''
        enable = self.scan_dir.text()
        if enable:
            enable = True
        else:
            enable = False
        self.scan_button.setEnabled(enable)
        
    def on_choose_dir_button_released(self):
        chosen = QFileDialog.getExistingDirectory(self, 'Choose scan directory', self.home_dir)
        self.scan_dir.setText(chosen)

    def on_checkbox_unzip_stateChanged(self):
        self.unzip_flag = not self.unzip_flag
        
    def on_checkbox_dups_stateChanged(self):
        self.dups_flag = not self.dups_flag
        
    def on_scan_button_released(self):
        '''Scans scan_dir text given dir, for files with meta info, adds filenames to list widget,
           downloads maps, saves places descriptions
        return: 0 - success, 1 - failure
        '''
        scan_text = self.scan_dir.text()
        # dir name validation
        if not os.path.isdir(scan_text):
            self.red_status('Not a directory')
            return 1
        else:
            self.status('')
        # checking if meta in dir files (checkboxes flags - unzip, dups removal)
        filepathes, locations = check_meta(scan_text, self.unzip_flag, self.dups_flag)
        if not filepathes:
            self.red_status('No GPS data')
            return 1
        else:
            self.status('Please wait')
            for i in range(len(filepathes)):
                # Getting existing maps filenames each iteration (to spare API calls)
                maps_names = os.listdir('maps/')
                # Download maps of locations (constant storage, doesn't re-download if exists, checked with MD5 sig and coordinates)
                # NOTE: map and place filenames are made of md5sum of original picture, and of coordinates (in certain format)
                map_name = md5sum(filepathes[i])
                # Adding hashes mappings to currenty used filenames for later list view of results
                self.maps_hashes[filepathes[i]] = '%s_%.7f-%.7f' % (map_name, *locations[i])
                # Adding new item path name to QLisetWidget
                if not self.list_results.findItems(filepathes[i], Qt.MatchExactly):
                    self.list_results.addItem(filepathes[i])
                else:
                    print('DEBUG: File already scanned, skipping instead of using API calls')
                    continue
                # If we already got map/placename for picture, skip (verified by MD5)
                if '%s_%.7f-%.7f.jpg' % (map_name, *locations[i]) in maps_names:
                    print('DEBUG: seen picture in different filepath, using stashed data instead of using API calls')
                    continue
                # If picture has same location of existing picture, copy map and place description instead of using API calls
                for loc in maps_names:
                    if loc.endswith('%.7f-%.7f.jpg' % locations[i]):
                        print('DEBUG: Already have map of coordinates for new picture, copying instead of using API calls')
                        self.same_loc_flag = True
                        loc = loc.replace('.jpg', '')
                        # copying map/placename files with different picture hash and same location
                        shutil.copy2('maps/%s.jpg' % loc, 'maps/%s%s.jpg' % (map_name, loc[32:]))
                        shutil.copy2('places/%s.txt' % loc, 'places/%s%s.txt' % (map_name, loc[32:]))
                        break
                if self.same_loc_flag:
                    self.same_loc_flag = False
                    continue
                # Saving map as hashname (relating by hash to original picture) (API Call)
                if not get_map(*locations[i], 'maps/%s_%.7f-%.7f.jpg' % (map_name, *locations[i])):
                    self.red_status('API Call Fail (key?)')
                    return 1
                print('DEBUG: Used map API call')
                # Saving place name as hashname (relating by.."") (API Call)
                place = get_placename(*locations[i])
                print('DEBUG: Used place name API call')
                with open('places/' + '%s_%.7f-%.7f' % (map_name, *locations[i]) + '.txt', 'w') as placefile:
                    if not place:
                        placefile.write('Unknown Place')
                    else:
                        placefile.write(place)
            # Message of scan successfully finished
            self.green_status('Found %d locations' % len(filepathes))
            return 0
    
    def on_list_results_currentItemChanged(self, item):
        pic_path = item.text()
        map_name = self.maps_hashes[pic_path]
        map_path = 'maps/' + map_name + '.jpg'
        # pic arrangements
        pic_profile = QImage(pic_path)
        pic_profile = pic_profile.scaled(270,270, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.piclabel_picture.setPixmap(QPixmap.fromImage(pic_profile))
        # map arrangements
        map_profile = QImage(map_path)
        map_profile = map_profile.scaled(270,270, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.piclabel_map.setPixmap(QPixmap.fromImage(map_profile))
        # Setting current place name and location (for copy buttons, visual lables)
        with open('places/' + map_name + '.txt') as placefile:
            self.current_place = placefile.read()
        self.current_location = map_name.split('_')[-1].replace('-', ', ')
        # Set map description labels
        self.label_placename.setText('''<p align='right'><font size="2">%s</font></p>''' % (self.current_place))
        self.label_location.setText('''<p align='right'><font size="2">(%s)</font></p>''' % (self.current_location))
        
    def on_copy_place_button_released(self):
        self.clipboard.setText(self.current_place)
        
    def on_copy_coor_button_released(self):
        self.clipboard.setText(self.current_location.strip(string.punctuation))
        
    def status(self, text):
        '''Updating status label with red text
        text: str message
        '''
        self.label_status.setText('''<b>%s</b>''' % text)
        
    def red_status(self, text):
        '''Updating status label with red text
        text: str message
        '''
        self.label_status.setText('''<font color='red'><b>%s</b></font>''' % text)
    
    def green_status(self, text):
        '''Updating status label with green text
        text: str message
        '''
        self.label_status.setText('''<font color='green'><b>%s</b></font>''' % text)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TraceFilesDlg()
    form.show()
    form.exec_()
