# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_person.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_person_popup(object):
    def setupUi(self, add_person_popup):
        add_person_popup.setObjectName("add_person_popup")
        add_person_popup.resize(507, 236)
        add_person_popup.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gridLayout = QtWidgets.QGridLayout(add_person_popup)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.type_cbox = QtWidgets.QComboBox(add_person_popup)
        self.type_cbox.setObjectName("type_cbox")
        self.type_cbox.addItem("")
        self.type_cbox.addItem("")
        self.type_cbox.addItem("")
        self.verticalLayout_4.addWidget(self.type_cbox)
        self.label_3 = QtWidgets.QLabel(add_person_popup)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.first_name_field = QtWidgets.QLineEdit(add_person_popup)
        self.first_name_field.setObjectName("first_name_field")
        self.verticalLayout_4.addWidget(self.first_name_field)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(add_person_popup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.last_name_field = QtWidgets.QLineEdit(add_person_popup)
        self.last_name_field.setObjectName("last_name_field")
        self.verticalLayout_3.addWidget(self.last_name_field)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem1)
        self.mentor_label = QtWidgets.QLabel(add_person_popup)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mentor_label.setFont(font)
        self.mentor_label.setObjectName("mentor_label")
        self.verticalLayout.addWidget(self.mentor_label)
        self.mentor_field_layout = QtWidgets.QHBoxLayout()
        self.mentor_field_layout.setSpacing(6)
        self.mentor_field_layout.setObjectName("mentor_field_layout")
        self.mentor_cbox_container = QtWidgets.QFrame(add_person_popup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mentor_cbox_container.sizePolicy().hasHeightForWidth())
        self.mentor_cbox_container.setSizePolicy(sizePolicy)
        self.mentor_cbox_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mentor_cbox_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mentor_cbox_container.setObjectName("mentor_cbox_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mentor_cbox_container)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mentor_field_layout.addWidget(self.mentor_cbox_container)
        self.new_mentor_btn = QtWidgets.QPushButton(add_person_popup)
        self.new_mentor_btn.setText("")
        self.new_mentor_btn.setIconSize(QtCore.QSize(16, 16))
        self.new_mentor_btn.setAutoDefault(False)
        self.new_mentor_btn.setFlat(True)
        self.new_mentor_btn.setObjectName("new_mentor_btn")
        self.mentor_field_layout.addWidget(self.new_mentor_btn)
        self.verticalLayout.addLayout(self.mentor_field_layout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(36)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_btn = QtWidgets.QPushButton(add_person_popup)
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(add_person_popup)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.mentor_field = QtWidgets.QLineEdit(add_person_popup)
        self.mentor_field.setObjectName("mentor_field")
        self.horizontalLayout.addWidget(self.mentor_field)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)

        self.retranslateUi(add_person_popup)
        QtCore.QMetaObject.connectSlotsByName(add_person_popup)

    def retranslateUi(self, add_person_popup):
        _translate = QtCore.QCoreApplication.translate
        add_person_popup.setWindowTitle(_translate("add_person_popup", "הוסף אדם חדש"))
        self.type_cbox.setItemText(0, _translate("add_person_popup", "תלמיד"))
        self.type_cbox.setItemText(1, _translate("add_person_popup", "צוות"))
        self.type_cbox.setItemText(2, _translate("add_person_popup", "אחר"))
        self.label_3.setText(_translate("add_person_popup", "שם פרטי"))
        self.label_2.setText(_translate("add_person_popup", "שם משפחה"))
        self.mentor_label.setText(_translate("add_person_popup", "חונך"))
        self.ok_btn.setText(_translate("add_person_popup", "אישור"))
        self.cancel_btn.setText(_translate("add_person_popup", "ביטול"))
