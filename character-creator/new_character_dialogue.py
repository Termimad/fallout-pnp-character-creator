# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\new_character_dialogue.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 628)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.racePicker = QtWidgets.QComboBox(self.page)
        self.racePicker.setObjectName("racePicker")
        self.racePicker.addItem("")
        self.racePicker.addItem("")
        self.racePicker.addItem("")
        self.racePicker.addItem("")
        self.racePicker.addItem("")
        self.racePicker.addItem("")
        self.racePicker.addItem("")
        self.gridLayout_2.addWidget(self.racePicker, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.nameField = QtWidgets.QLineEdit(self.page)
        self.nameField.setObjectName("nameField")
        self.gridLayout_2.addWidget(self.nameField, 0, 1, 1, 1)
        self.ageField = QtWidgets.QLineEdit(self.page)
        self.ageField.setObjectName("ageField")
        self.gridLayout_2.addWidget(self.ageField, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.eyesField = QtWidgets.QLineEdit(self.page)
        self.eyesField.setObjectName("eyesField")
        self.gridLayout_2.addWidget(self.eyesField, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.hairField = QtWidgets.QLineEdit(self.page)
        self.hairField.setObjectName("hairField")
        self.gridLayout_2.addWidget(self.hairField, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.heightField = QtWidgets.QLineEdit(self.page)
        self.heightField.setObjectName("heightField")
        self.gridLayout_2.addWidget(self.heightField, 6, 1, 1, 1)
        self.weightField = QtWidgets.QLineEdit(self.page)
        self.weightField.setObjectName("weightField")
        self.gridLayout_2.addWidget(self.weightField, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        self.appearanceField = QtWidgets.QTextEdit(self.page)
        self.appearanceField.setObjectName("appearanceField")
        self.gridLayout_2.addWidget(self.appearanceField, 8, 1, 1, 1)
        self.sexPicker = QtWidgets.QComboBox(self.page)
        self.sexPicker.setObjectName("sexPicker")
        self.gridLayout_2.addWidget(self.sexPicker, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 155, 294))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.intelligenceBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.intelligenceBox.setObjectName("intelligenceBox")
        self.gridLayout_4.addWidget(self.intelligenceBox, 4, 1, 1, 1)
        self.strengthLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.strengthLabel.setObjectName("strengthLabel")
        self.gridLayout_4.addWidget(self.strengthLabel, 0, 0, 1, 1)
        self.agilityLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.agilityLabel.setObjectName("agilityLabel")
        self.gridLayout_4.addWidget(self.agilityLabel, 5, 0, 1, 1)
        self.strengthBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.strengthBox.setObjectName("strengthBox")
        self.gridLayout_4.addWidget(self.strengthBox, 0, 1, 1, 1)
        self.charismaLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.charismaLabel.setObjectName("charismaLabel")
        self.gridLayout_4.addWidget(self.charismaLabel, 3, 0, 1, 1)
        self.luckLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.luckLabel.setObjectName("luckLabel")
        self.gridLayout_4.addWidget(self.luckLabel, 6, 0, 1, 1)
        self.intelligenceLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.intelligenceLabel.setObjectName("intelligenceLabel")
        self.gridLayout_4.addWidget(self.intelligenceLabel, 4, 0, 1, 1)
        self.charismaBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.charismaBox.setObjectName("charismaBox")
        self.gridLayout_4.addWidget(self.charismaBox, 3, 1, 1, 1)
        self.luckBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.luckBox.setObjectName("luckBox")
        self.gridLayout_4.addWidget(self.luckBox, 6, 1, 1, 1)
        self.enduranceLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.enduranceLabel.setObjectName("enduranceLabel")
        self.gridLayout_4.addWidget(self.enduranceLabel, 2, 0, 1, 1)
        self.perceptionLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.perceptionLabel.setObjectName("perceptionLabel")
        self.gridLayout_4.addWidget(self.perceptionLabel, 1, 0, 1, 1)
        self.agilityBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.agilityBox.setObjectName("agilityBox")
        self.gridLayout_4.addWidget(self.agilityBox, 5, 1, 1, 1)
        self.perceptionBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.perceptionBox.setObjectName("perceptionBox")
        self.gridLayout_4.addWidget(self.perceptionBox, 1, 1, 1, 1)
        self.enduranceBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.enduranceBox.setObjectName("enduranceBox")
        self.gridLayout_4.addWidget(self.enduranceBox, 2, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 7, 0, 1, 1)
        self.availablePointsBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.availablePointsBox.setReadOnly(True)
        self.availablePointsBox.setObjectName("availablePointsBox")
        self.gridLayout_4.addWidget(self.availablePointsBox, 7, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 151, 531))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.skillLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.skillLayout.setContentsMargins(0, 0, 0, 0)
        self.skillLayout.setObjectName("skillLayout")
        self.throwingLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.throwingLabel.setObjectName("throwingLabel")
        self.skillLayout.addWidget(self.throwingLabel, 5, 0, 1, 1)
        self.explosivesBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.explosivesBox.setObjectName("explosivesBox")
        self.skillLayout.addWidget(self.explosivesBox, 6, 1, 1, 1)
        self.sneakBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.sneakBox.setObjectName("sneakBox")
        self.skillLayout.addWidget(self.sneakBox, 8, 1, 1, 1)
        self.pilotLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.pilotLabel.setObjectName("pilotLabel")
        self.skillLayout.addWidget(self.pilotLabel, 13, 0, 1, 1)
        self.unarmedLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.unarmedLabel.setObjectName("unarmedLabel")
        self.skillLayout.addWidget(self.unarmedLabel, 3, 0, 1, 1)
        self.meleeWeaponsBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.meleeWeaponsBox.setObjectName("meleeWeaponsBox")
        self.skillLayout.addWidget(self.meleeWeaponsBox, 4, 1, 1, 1)
        self.repairLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.repairLabel.setObjectName("repairLabel")
        self.skillLayout.addWidget(self.repairLabel, 12, 0, 1, 1)
        self.energyWeaponsBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.energyWeaponsBox.setObjectName("energyWeaponsBox")
        self.skillLayout.addWidget(self.energyWeaponsBox, 2, 1, 1, 1)
        self.gamblingLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.gamblingLabel.setObjectName("gamblingLabel")
        self.skillLayout.addWidget(self.gamblingLabel, 16, 0, 1, 1)
        self.unarmedBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.unarmedBox.setObjectName("unarmedBox")
        self.skillLayout.addWidget(self.unarmedBox, 3, 1, 1, 1)
        self.speechLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.speechLabel.setObjectName("speechLabel")
        self.skillLayout.addWidget(self.speechLabel, 14, 0, 1, 1)
        self.lockpickLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lockpickLabel.setObjectName("lockpickLabel")
        self.skillLayout.addWidget(self.lockpickLabel, 9, 0, 1, 1)
        self.smallGunsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.smallGunsLabel.setObjectName("smallGunsLabel")
        self.skillLayout.addWidget(self.smallGunsLabel, 0, 0, 1, 1)
        self.survivalLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.survivalLabel.setObjectName("survivalLabel")
        self.skillLayout.addWidget(self.survivalLabel, 17, 0, 1, 1)
        self.doctorLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.doctorLabel.setObjectName("doctorLabel")
        self.skillLayout.addWidget(self.doctorLabel, 7, 0, 1, 1)
        self.scienceLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.scienceLabel.setObjectName("scienceLabel")
        self.skillLayout.addWidget(self.scienceLabel, 11, 0, 1, 1)
        self.smallGunsBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.smallGunsBox.setObjectName("smallGunsBox")
        self.skillLayout.addWidget(self.smallGunsBox, 0, 1, 1, 1)
        self.speechBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.speechBox.setObjectName("speechBox")
        self.skillLayout.addWidget(self.speechBox, 14, 1, 1, 1)
        self.bigGunsBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.bigGunsBox.setObjectName("bigGunsBox")
        self.skillLayout.addWidget(self.bigGunsBox, 1, 1, 1, 1)
        self.trapsBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.trapsBox.setObjectName("trapsBox")
        self.skillLayout.addWidget(self.trapsBox, 10, 1, 1, 1)
        self.barterLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.barterLabel.setObjectName("barterLabel")
        self.skillLayout.addWidget(self.barterLabel, 15, 0, 1, 1)
        self.survivalBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.survivalBox.setObjectName("survivalBox")
        self.skillLayout.addWidget(self.survivalBox, 17, 1, 1, 1)
        self.explosivesLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.explosivesLabel.setObjectName("explosivesLabel")
        self.skillLayout.addWidget(self.explosivesLabel, 6, 0, 1, 1)
        self.repairBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.repairBox.setObjectName("repairBox")
        self.skillLayout.addWidget(self.repairBox, 12, 1, 1, 1)
        self.sneakLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.sneakLabel.setObjectName("sneakLabel")
        self.skillLayout.addWidget(self.sneakLabel, 8, 0, 1, 1)
        self.pilotBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.pilotBox.setObjectName("pilotBox")
        self.skillLayout.addWidget(self.pilotBox, 13, 1, 1, 1)
        self.barterBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.barterBox.setObjectName("barterBox")
        self.skillLayout.addWidget(self.barterBox, 15, 1, 1, 1)
        self.bigGunsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.bigGunsLabel.setObjectName("bigGunsLabel")
        self.skillLayout.addWidget(self.bigGunsLabel, 1, 0, 1, 1)
        self.trapsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.trapsLabel.setObjectName("trapsLabel")
        self.skillLayout.addWidget(self.trapsLabel, 10, 0, 1, 1)
        self.gamblingBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.gamblingBox.setObjectName("gamblingBox")
        self.skillLayout.addWidget(self.gamblingBox, 16, 1, 1, 1)
        self.meleeWeaponsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.meleeWeaponsLabel.setObjectName("meleeWeaponsLabel")
        self.skillLayout.addWidget(self.meleeWeaponsLabel, 4, 0, 1, 1)
        self.doctorBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.doctorBox.setObjectName("doctorBox")
        self.skillLayout.addWidget(self.doctorBox, 7, 1, 1, 1)
        self.throwingBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.throwingBox.setObjectName("throwingBox")
        self.skillLayout.addWidget(self.throwingBox, 5, 1, 1, 1)
        self.energyWeaponsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.energyWeaponsLabel.setObjectName("energyWeaponsLabel")
        self.skillLayout.addWidget(self.energyWeaponsLabel, 2, 0, 1, 1)
        self.scienceBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.scienceBox.setObjectName("scienceBox")
        self.skillLayout.addWidget(self.scienceBox, 11, 1, 1, 1)
        self.lockpickBox = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        self.lockpickBox.setObjectName("lockpickBox")
        self.skillLayout.addWidget(self.lockpickBox, 9, 1, 1, 1)
        self.unarmedTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.unarmedTag.setText("")
        self.unarmedTag.setObjectName("unarmedTag")
        self.skillLayout.addWidget(self.unarmedTag, 3, 2, 1, 1)
        self.throwingTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.throwingTag.setText("")
        self.throwingTag.setObjectName("throwingTag")
        self.skillLayout.addWidget(self.throwingTag, 5, 2, 1, 1)
        self.meleeWeaponsTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.meleeWeaponsTag.setText("")
        self.meleeWeaponsTag.setObjectName("meleeWeaponsTag")
        self.skillLayout.addWidget(self.meleeWeaponsTag, 4, 2, 1, 1)
        self.energyWeaponsTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.energyWeaponsTag.setText("")
        self.energyWeaponsTag.setObjectName("energyWeaponsTag")
        self.skillLayout.addWidget(self.energyWeaponsTag, 2, 2, 1, 1)
        self.bigGunsTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.bigGunsTag.setText("")
        self.bigGunsTag.setObjectName("bigGunsTag")
        self.skillLayout.addWidget(self.bigGunsTag, 1, 2, 1, 1)
        self.doctorTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.doctorTag.setText("")
        self.doctorTag.setObjectName("doctorTag")
        self.skillLayout.addWidget(self.doctorTag, 7, 2, 1, 1)
        self.explosivesTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.explosivesTag.setText("")
        self.explosivesTag.setObjectName("explosivesTag")
        self.skillLayout.addWidget(self.explosivesTag, 6, 2, 1, 1)
        self.lockpickTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.lockpickTag.setText("")
        self.lockpickTag.setObjectName("lockpickTag")
        self.skillLayout.addWidget(self.lockpickTag, 9, 2, 1, 1)
        self.sneakTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.sneakTag.setText("")
        self.sneakTag.setObjectName("sneakTag")
        self.skillLayout.addWidget(self.sneakTag, 8, 2, 1, 1)
        self.gamblingTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.gamblingTag.setText("")
        self.gamblingTag.setObjectName("gamblingTag")
        self.skillLayout.addWidget(self.gamblingTag, 16, 2, 1, 1)
        self.trapsTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.trapsTag.setText("")
        self.trapsTag.setObjectName("trapsTag")
        self.skillLayout.addWidget(self.trapsTag, 10, 2, 1, 1)
        self.speechTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.speechTag.setText("")
        self.speechTag.setObjectName("speechTag")
        self.skillLayout.addWidget(self.speechTag, 14, 2, 1, 1)
        self.repairTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.repairTag.setText("")
        self.repairTag.setObjectName("repairTag")
        self.skillLayout.addWidget(self.repairTag, 12, 2, 1, 1)
        self.scienceTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.scienceTag.setText("")
        self.scienceTag.setObjectName("scienceTag")
        self.skillLayout.addWidget(self.scienceTag, 11, 2, 1, 1)
        self.barterTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.barterTag.setText("")
        self.barterTag.setObjectName("barterTag")
        self.skillLayout.addWidget(self.barterTag, 15, 2, 1, 1)
        self.survivalTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.survivalTag.setText("")
        self.survivalTag.setObjectName("survivalTag")
        self.skillLayout.addWidget(self.survivalTag, 17, 2, 1, 1)
        self.pilotTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.pilotTag.setText("")
        self.pilotTag.setObjectName("pilotTag")
        self.skillLayout.addWidget(self.pilotTag, 13, 2, 1, 1)
        self.smallGunsTag = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.smallGunsTag.setText("")
        self.smallGunsTag.setTristate(False)
        self.smallGunsTag.setObjectName("smallGunsTag")
        self.skillLayout.addWidget(self.smallGunsTag, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter = QtWidgets.QSplitter(self.page_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.traitListWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.traitListWidget.setObjectName("traitListWidget")
        self.gridLayout_7.addWidget(self.traitListWidget, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 0, 0, 1, 1)
        self.descriptionBox = QtWidgets.QTextBrowser(self.groupBox)
        self.descriptionBox.setObjectName("descriptionBox")
        self.gridLayout_6.addWidget(self.descriptionBox, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.splitter, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.strengthLabel.setBuddy(self.strengthBox)
        self.agilityLabel.setBuddy(self.agilityBox)
        self.charismaLabel.setBuddy(self.charismaBox)
        self.luckLabel.setBuddy(self.luckBox)
        self.intelligenceLabel.setBuddy(self.intelligenceBox)
        self.enduranceLabel.setBuddy(self.enduranceBox)
        self.perceptionLabel.setBuddy(self.perceptionBox)
        self.throwingLabel.setBuddy(self.throwingTag)
        self.pilotLabel.setBuddy(self.pilotTag)
        self.unarmedLabel.setBuddy(self.unarmedTag)
        self.repairLabel.setBuddy(self.repairTag)
        self.gamblingLabel.setBuddy(self.gamblingTag)
        self.speechLabel.setBuddy(self.speechTag)
        self.lockpickLabel.setBuddy(self.lockpickTag)
        self.smallGunsLabel.setBuddy(self.smallGunsTag)
        self.survivalLabel.setBuddy(self.survivalTag)
        self.doctorLabel.setBuddy(self.doctorTag)
        self.scienceLabel.setBuddy(self.scienceTag)
        self.barterLabel.setBuddy(self.barterTag)
        self.explosivesLabel.setBuddy(self.explosivesTag)
        self.sneakLabel.setBuddy(self.sneakTag)
        self.bigGunsLabel.setBuddy(self.bigGunsTag)
        self.trapsLabel.setBuddy(self.trapsTag)
        self.meleeWeaponsLabel.setBuddy(self.meleeWeaponsTag)
        self.energyWeaponsLabel.setBuddy(self.energyWeaponsTag)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.nameField, self.ageField)
        Dialog.setTabOrder(self.ageField, self.sexPicker)
        Dialog.setTabOrder(self.sexPicker, self.racePicker)
        Dialog.setTabOrder(self.racePicker, self.eyesField)
        Dialog.setTabOrder(self.eyesField, self.hairField)
        Dialog.setTabOrder(self.hairField, self.heightField)
        Dialog.setTabOrder(self.heightField, self.weightField)
        Dialog.setTabOrder(self.weightField, self.appearanceField)
        Dialog.setTabOrder(self.appearanceField, self.intelligenceBox)
        Dialog.setTabOrder(self.intelligenceBox, self.strengthBox)
        Dialog.setTabOrder(self.strengthBox, self.charismaBox)
        Dialog.setTabOrder(self.charismaBox, self.luckBox)
        Dialog.setTabOrder(self.luckBox, self.agilityBox)
        Dialog.setTabOrder(self.agilityBox, self.perceptionBox)
        Dialog.setTabOrder(self.perceptionBox, self.enduranceBox)
        Dialog.setTabOrder(self.enduranceBox, self.availablePointsBox)
        Dialog.setTabOrder(self.availablePointsBox, self.explosivesBox)
        Dialog.setTabOrder(self.explosivesBox, self.meleeWeaponsBox)
        Dialog.setTabOrder(self.meleeWeaponsBox, self.energyWeaponsBox)
        Dialog.setTabOrder(self.energyWeaponsBox, self.sneakBox)
        Dialog.setTabOrder(self.sneakBox, self.unarmedBox)
        Dialog.setTabOrder(self.unarmedBox, self.lockpickBox)
        Dialog.setTabOrder(self.lockpickBox, self.survivalBox)
        Dialog.setTabOrder(self.survivalBox, self.bigGunsBox)
        Dialog.setTabOrder(self.bigGunsBox, self.doctorBox)
        Dialog.setTabOrder(self.doctorBox, self.throwingBox)
        Dialog.setTabOrder(self.throwingBox, self.smallGunsBox)
        Dialog.setTabOrder(self.smallGunsBox, self.barterBox)
        Dialog.setTabOrder(self.barterBox, self.pilotBox)
        Dialog.setTabOrder(self.pilotBox, self.gamblingBox)
        Dialog.setTabOrder(self.gamblingBox, self.speechBox)
        Dialog.setTabOrder(self.speechBox, self.trapsBox)
        Dialog.setTabOrder(self.trapsBox, self.repairBox)
        Dialog.setTabOrder(self.repairBox, self.scienceBox)
        Dialog.setTabOrder(self.scienceBox, self.smallGunsTag)
        Dialog.setTabOrder(self.smallGunsTag, self.bigGunsTag)
        Dialog.setTabOrder(self.bigGunsTag, self.energyWeaponsTag)
        Dialog.setTabOrder(self.energyWeaponsTag, self.unarmedTag)
        Dialog.setTabOrder(self.unarmedTag, self.meleeWeaponsTag)
        Dialog.setTabOrder(self.meleeWeaponsTag, self.throwingTag)
        Dialog.setTabOrder(self.throwingTag, self.explosivesTag)
        Dialog.setTabOrder(self.explosivesTag, self.doctorTag)
        Dialog.setTabOrder(self.doctorTag, self.sneakTag)
        Dialog.setTabOrder(self.sneakTag, self.lockpickTag)
        Dialog.setTabOrder(self.lockpickTag, self.trapsTag)
        Dialog.setTabOrder(self.trapsTag, self.scienceTag)
        Dialog.setTabOrder(self.scienceTag, self.repairTag)
        Dialog.setTabOrder(self.repairTag, self.pilotTag)
        Dialog.setTabOrder(self.pilotTag, self.speechTag)
        Dialog.setTabOrder(self.speechTag, self.barterTag)
        Dialog.setTabOrder(self.barterTag, self.gamblingTag)
        Dialog.setTabOrder(self.gamblingTag, self.survivalTag)
        Dialog.setTabOrder(self.survivalTag, self.traitListWidget)
        Dialog.setTabOrder(self.traitListWidget, self.descriptionBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.racePicker.setItemText(0, _translate("Dialog", "Human"))
        self.racePicker.setItemText(1, _translate("Dialog", "Ghoul"))
        self.racePicker.setItemText(2, _translate("Dialog", "Super Mutant"))
        self.racePicker.setItemText(3, _translate("Dialog", "Half Mutant"))
        self.racePicker.setItemText(4, _translate("Dialog", "Deathclaw"))
        self.racePicker.setItemText(5, _translate("Dialog", "Dog"))
        self.racePicker.setItemText(6, _translate("Dialog", "Robot"))
        self.label_2.setText(_translate("Dialog", "Age"))
        self.label_3.setText(_translate("Dialog", "Sex"))
        self.label_4.setText(_translate("Dialog", "Race"))
        self.label_8.setText(_translate("Dialog", "Weight"))
        self.label_5.setText(_translate("Dialog", "Eyes"))
        self.label_7.setText(_translate("Dialog", "Height"))
        self.label_6.setText(_translate("Dialog", "Hair"))
        self.label_9.setText(_translate("Dialog", "Appearance"))
        self.strengthLabel.setText(_translate("Dialog", "Strength"))
        self.agilityLabel.setText(_translate("Dialog", "Agility"))
        self.charismaLabel.setText(_translate("Dialog", "Charisma"))
        self.luckLabel.setText(_translate("Dialog", "Luck"))
        self.intelligenceLabel.setText(_translate("Dialog", "Intelligence"))
        self.enduranceLabel.setText(_translate("Dialog", "Endurance"))
        self.perceptionLabel.setText(_translate("Dialog", "Perception"))
        self.label_35.setText(_translate("Dialog", "Points to go"))
        self.throwingLabel.setText(_translate("Dialog", "Throwing"))
        self.pilotLabel.setText(_translate("Dialog", "Pilot"))
        self.unarmedLabel.setText(_translate("Dialog", "Unarmed"))
        self.repairLabel.setText(_translate("Dialog", "Repair"))
        self.gamblingLabel.setText(_translate("Dialog", "Gambling"))
        self.speechLabel.setText(_translate("Dialog", "Speech"))
        self.lockpickLabel.setText(_translate("Dialog", "Lockpick"))
        self.smallGunsLabel.setText(_translate("Dialog", "Small Guns"))
        self.survivalLabel.setText(_translate("Dialog", "Survival"))
        self.doctorLabel.setText(_translate("Dialog", "Doctor"))
        self.scienceLabel.setText(_translate("Dialog", "Science"))
        self.barterLabel.setText(_translate("Dialog", "Barter"))
        self.explosivesLabel.setText(_translate("Dialog", "Explosives"))
        self.sneakLabel.setText(_translate("Dialog", "Sneak"))
        self.bigGunsLabel.setText(_translate("Dialog", "Big Guns"))
        self.trapsLabel.setText(_translate("Dialog", "Traps"))
        self.meleeWeaponsLabel.setText(_translate("Dialog", "Melee Weapons"))
        self.energyWeaponsLabel.setText(_translate("Dialog", "Energy Weapons"))
        self.groupBox_2.setTitle(_translate("Dialog", "Available Traits"))
        self.traitListWidget.setSortingEnabled(True)
        self.groupBox.setTitle(_translate("Dialog", "Description"))
        self.label_10.setText(_translate("Dialog", "Available for:"))

