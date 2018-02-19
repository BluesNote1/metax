# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracefilesdlg.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TraceFilesDlg(object):
    def setupUi(self, TraceFilesDlg):
        TraceFilesDlg.setObjectName(_fromUtf8("TraceFilesDlg"))
        TraceFilesDlg.resize(694, 720)
        TraceFilesDlg.setSizeGripEnabled(False)
        TraceFilesDlg.setModal(False)
        self.gridLayout = QtGui.QGridLayout(TraceFilesDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkbox_unzip = QtGui.QCheckBox(TraceFilesDlg)
        self.checkbox_unzip.setObjectName(_fromUtf8("checkbox_unzip"))
        self.gridLayout.addWidget(self.checkbox_unzip, 5, 1, 1, 1)
        self.label_results = QtGui.QLabel(TraceFilesDlg)
        self.label_results.setObjectName(_fromUtf8("label_results"))
        self.gridLayout.addWidget(self.label_results, 7, 0, 1, 1)
        self.checkbox_dups = QtGui.QCheckBox(TraceFilesDlg)
        self.checkbox_dups.setObjectName(_fromUtf8("checkbox_dups"))
        self.gridLayout.addWidget(self.checkbox_dups, 5, 0, 1, 1)
        self.line = QtGui.QFrame(TraceFilesDlg)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 2, 18, 2)
        self.scan_button = QtGui.QPushButton(TraceFilesDlg)
        self.scan_button.setAutoFillBackground(False)
        self.scan_button.setCheckable(False)
        self.scan_button.setAutoDefault(True)
        self.scan_button.setDefault(False)
        self.scan_button.setFlat(False)
        self.scan_button.setObjectName(_fromUtf8("scan_button"))
        self.gridLayout.addWidget(self.scan_button, 4, 0, 1, 2)
        self.label_scan = QtGui.QLabel(TraceFilesDlg)
        self.label_scan.setObjectName(_fromUtf8("label_scan"))
        self.gridLayout.addWidget(self.label_scan, 0, 0, 1, 2)
        self.list_results = QtGui.QListWidget(TraceFilesDlg)
        self.list_results.setObjectName(_fromUtf8("list_results"))
        self.gridLayout.addWidget(self.list_results, 8, 0, 10, 2)
        self.label_picture = QtGui.QLabel(TraceFilesDlg)
        self.label_picture.setObjectName(_fromUtf8("label_picture"))
        self.gridLayout.addWidget(self.label_picture, 0, 4, 2, 1)
        self.label_map = QtGui.QLabel(TraceFilesDlg)
        self.label_map.setObjectName(_fromUtf8("label_map"))
        self.gridLayout.addWidget(self.label_map, 14, 4, 1, 1)
        self.piclabel_map = QtGui.QLabel(TraceFilesDlg)
        self.piclabel_map.setMinimumSize(QtCore.QSize(260, 260))
        self.piclabel_map.setText(_fromUtf8(""))
        self.piclabel_map.setScaledContents(False)
        self.piclabel_map.setAlignment(QtCore.Qt.AlignCenter)
        self.piclabel_map.setObjectName(_fromUtf8("piclabel_map"))
        self.gridLayout.addWidget(self.piclabel_map, 17, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(130, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.copy_coor_button = QtGui.QPushButton(TraceFilesDlg)
        self.copy_coor_button.setObjectName(_fromUtf8("copy_coor_button"))
        self.gridLayout.addWidget(self.copy_coor_button, 18, 3, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(240, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scan_dir = QtGui.QLineEdit(TraceFilesDlg)
        self.scan_dir.setObjectName(_fromUtf8("scan_dir"))
        self.horizontalLayout.addWidget(self.scan_dir)
        self.choose_dir_button = QtGui.QPushButton(TraceFilesDlg)
        self.choose_dir_button.setMaximumSize(QtCore.QSize(65, 16777215))
        self.choose_dir_button.setObjectName(_fromUtf8("choose_dir_button"))
        self.horizontalLayout.addWidget(self.choose_dir_button)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.piclabel_picture = QtGui.QLabel(TraceFilesDlg)
        self.piclabel_picture.setMinimumSize(QtCore.QSize(260, 260))
        self.piclabel_picture.setText(_fromUtf8(""))
        self.piclabel_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.piclabel_picture.setObjectName(_fromUtf8("piclabel_picture"))
        self.gridLayout.addWidget(self.piclabel_picture, 3, 6, 10, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 242, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 17, 3, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 242, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 3, 11, 2)
        self.label_status = QtGui.QLabel(TraceFilesDlg)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout.addWidget(self.label_status, 7, 1, 1, 1)
        self.copy_place_button = QtGui.QPushButton(TraceFilesDlg)
        self.copy_place_button.setObjectName(_fromUtf8("copy_place_button"))
        self.gridLayout.addWidget(self.copy_place_button, 18, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(270, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 13, 6, 1, 1)
        self.label_placename = QtGui.QLabel(TraceFilesDlg)
        self.label_placename.setText(_fromUtf8(""))
        self.label_placename.setObjectName(_fromUtf8("label_placename"))
        self.gridLayout.addWidget(self.label_placename, 14, 6, 1, 1)
        self.label_location = QtGui.QLabel(TraceFilesDlg)
        self.label_location.setText(_fromUtf8(""))
        self.label_location.setObjectName(_fromUtf8("label_location"))
        self.gridLayout.addWidget(self.label_location, 15, 6, 1, 1)

        self.retranslateUi(TraceFilesDlg)
        QtCore.QMetaObject.connectSlotsByName(TraceFilesDlg)
        TraceFilesDlg.setTabOrder(self.scan_button, self.list_results)
        TraceFilesDlg.setTabOrder(self.list_results, self.copy_place_button)
        TraceFilesDlg.setTabOrder(self.copy_place_button, self.copy_coor_button)

    def retranslateUi(self, TraceFilesDlg):
        TraceFilesDlg.setWindowTitle(_translate("TraceFilesDlg", "MetaX - Trace Files Location", None))
        self.checkbox_unzip.setText(_translate("TraceFilesDlg", "Extract zips", None))
        self.label_results.setText(_translate("TraceFilesDlg", "Location Extracts:", None))
        self.checkbox_dups.setText(_translate("TraceFilesDlg", "Remove duplicates (MD5)", None))
        self.scan_button.setText(_translate("TraceFilesDlg", "Scan", None))
        self.label_scan.setText(_translate("TraceFilesDlg", "Choose directory for scan", None))
        self.label_picture.setText(_translate("TraceFilesDlg", "Picture", None))
        self.label_map.setText(_translate("TraceFilesDlg", "Map", None))
        self.copy_coor_button.setText(_translate("TraceFilesDlg", "Copy coordinates", None))
        self.choose_dir_button.setText(_translate("TraceFilesDlg", "Browse", None))
        self.copy_place_button.setText(_translate("TraceFilesDlg", "Copy place name", None))

