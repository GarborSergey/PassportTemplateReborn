import sys
from os import sep

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, Qt

from mainwindow import Ui_MainWindow
from constructors import Passport, PassportException

VERSION = "0.0.0"


class PassportTemplate(QMainWindow):
    def __init__(self):
        super(PassportTemplate, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # structure dict that consist, in key - invariable ui elements,
        # in value - variable ui elements. for passport data
        self.uiVariableElementsPassportData = {
            self.ui.labelPanelAssignment: self.ui.cboxPanelAssignment,
            self.ui.labelPurposeOfTheIntroductoryControlUnit: self.ui.cboxPurposeOfTheIntroductoryControlUnit,
            self.ui.labelAdditionalEquipment: self.ui.cboxAdditionalEquipment,
            self.ui.labelProtectiveDevices: self.ui.cboxProtectiveDevices,
            self.ui.labelIngressProtectionRating: self.ui.cboxIngressProtectionRating,
            self.ui.labelClimaticVersion: self.ui.cboxClimaticVersion,
            self.ui.labelDatabaseNumber: self.ui.lineEdDatabaseNumber,
            self.ui.labelNameBox: self.ui.lineEdNameBox,
            self.ui.labelNominalCurrent: self.ui.lineEdNominalCurrent,
            self.ui.labelNominalShortCircuitCurrent: self.ui.lineEdNominalShortCircuitCurrent,
            self.ui.labelSystemGrounding: self.ui.cboxSystemGrounding,
            self.ui.labelInstallationMethod: self.ui.cboxInstallationMethod,
            self.ui.labelInputCrossSection: self.ui.lineEdInputCrossSection,
            self.ui.labelHeight: self.ui.lineEdHeight,
            self.ui.labelWidth: self.ui.lineEdWidth,
            self.ui.labelDepth: self.ui.lineEdDepth,
            self.ui.labelWeight: self.ui.lineEdWeight,
            self.ui.labelProtectionClass: self.ui.cboxProtectionClass,
        }
        self.init_UI()

    def __clear_all_cbox(self):
        self.ui.cboxPanelAssignment.setCurrentIndex(-1)
        self.ui.cboxPurposeOfTheIntroductoryControlUnit.setCurrentIndex(-1)
        self.ui.cboxAdditionalEquipment.setCurrentIndex(-1)
        self.ui.cboxProtectiveDevices.setCurrentIndex(-1)
        self.ui.cboxIngressProtectionRating.setCurrentIndex(-1)
        self.ui.cboxClimaticVersion.setCurrentIndex(0)
        self.ui.cboxSystemGrounding.setCurrentIndex(-1)
        self.ui.cboxInstallationMethod.setCurrentIndex(-1)
        self.ui.cboxProtectionClass.setCurrentIndex(-1)

    def init_UI(self):
        self.ui.cboxPanelAssignment.addItems([
            '1 - Вводное',
            '2 - Вводно-распределительное',
            '3 - Распределительное',
        ])
        self.ui.cboxPurposeOfTheIntroductoryControlUnit.addItems([
            '0 - Отсутствует',
            '1 - Переключатель на 100А',
            '2 - Переключатель на 160А',
            '3 - Переключатель на 250А',
            '4 - Переключатель на 400А',
            '5 - Переключатель на 630А',
            '6 - Выключатель на 100А',
            '7 - Выключатель на 160А',
            '8 - Выключатель на 250А',
            '9 - Выключатель на 400А',
            '10 - Выключатель на 630А',
            '11 - Выключатель и аппаратура АВР на 100А',
            '12 - Выключатель и аппаратура АВР на 160А',
            '13 - Выключатель и аппаратура АВР на 250А',
            '14 - Выключатель и аппаратура АВР на 400А',
            '15 - Выключатель и аппаратура АВР на 630А',
            '16 - Два выключателя 100А',
            '17 - Два выключателя 160А',
            '18 - Два выключателя 250А',
            '19 - Два выключателя 400А',
            '20 - Два выключателя 630А',
            '21 - Выключатели и переключатели до 100А',
            '22 - Выключатели и переключатели более 630А',
            '23 - Выключатель и аппаратура АВР более 630А',
            '24 - Выключатель более 630А',
            '25 - Два выключателя боее 630А',
            '26 - Переключатель более 630А',
        ])
        self.ui.cboxAdditionalEquipment.addItems([
            '0 - Отсутствует',
            '1 - Блок автоматического управления освещением на 30 групп',
            '2 - Блок неавтоматического управления освещением на 30 групп',
            '3 - Блок автоматического управления освещением на 14 групп',
            '4 - Блок неавтоматического управления освещением на 14 групп',
            '5 - Блок автоматического управления освещением на 8 групп',
            '6 - Блок неавтоматического управления освещением на 8 групп',
        ])
        self.ui.cboxProtectiveDevices.addItems([
            '1 - Автоматические выключатели',
            '2 - Предохранители',
        ])
        self.ui.cboxIngressProtectionRating.addItems([
            '30',
            '31',
            '54',
            '65',
        ])
        self.ui.cboxClimaticVersion.addItems([
            'УХЛ4',
        ])
        self.ui.cboxSystemGrounding.addItems([
            'TN-S',
            'TN-C',
            'TN-C-S',
            'TT',
            'IT',
        ])
        self.ui.cboxInstallationMethod.addItems([
            'Навесной',
            'Напольный',
            'Встраиваемый',
        ])
        self.ui.cboxProtectionClass.addItems([
            'I',
            'II',
        ])

        self.__clear_all_cbox()

        self.ui.lineEdDatabaseNumber.setValidator(QIntValidator(1000, 99999))
        self.ui.lineEdNominalCurrent.setValidator(QIntValidator(1, 9999))
        self.ui.lineEdNominalShortCircuitCurrent.setValidator(QDoubleValidator(0.0, 100.0, 1))
        self.ui.lineEdInputCrossSection.setValidator(QRegularExpressionValidator(QRegularExpression('\d{1}[x, х]\d{3}')))
        self.ui.lineEdWidth.setValidator(QIntValidator(0, 20000))
        self.ui.lineEdHeight.setValidator(QIntValidator(0, 3000))
        self.ui.lineEdDepth.setValidator(QIntValidator(0, 20000))
        self.ui.lineEdWeight.setValidator(QIntValidator(0, 20000))

        self.ui.btnCreatePassport.clicked.connect(self.create_passport)

    def if_empty_set_red_color(self):
        for elem in self.uiVariableElementsPassportData:
            if type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QComboBox:
                if self.uiVariableElementsPassportData[elem].currentText() == '':
                    elem.setStyleSheet("color: red;")
            elif type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QLineEdit:
                if self.uiVariableElementsPassportData[elem].text() == '':
                    elem.setStyleSheet("color: red;")

    def set_black_color(self):
        for elem in self.uiVariableElementsPassportData:
            elem.setStyleSheet("color: black;")

    def create_passport(self):
        pathFile = QFileDialog.getExistingDirectory()
        try:
            passport = Passport(
                self.ui.cboxPanelAssignment.currentText(),
                self.ui.cboxPurposeOfTheIntroductoryControlUnit.currentText(),
                self.ui.cboxAdditionalEquipment.currentText(),
                self.ui.cboxProtectiveDevices.currentText(),
                self.ui.cboxIngressProtectionRating.currentText(),
                self.ui.cboxClimaticVersion.currentText(),
                self.ui.lineEdDatabaseNumber.text(),
                self.ui.lineEdNameBox.text(),
                self.ui.lineEdNominalCurrent.text(),
                self.ui.lineEdNominalShortCircuitCurrent.text(),
                self.ui.cboxSystemGrounding.currentText(),
                self.ui.cboxInstallationMethod.currentText(),
                self.ui.lineEdInputCrossSection.text(),
                self.ui.lineEdHeight.text(),
                self.ui.lineEdWidth.text(),
                self.ui.lineEdDepth.text(),
                self.ui.lineEdWeight.text(),
                self.ui.cboxProtectionClass.currentText()
            )
        except PassportException:
            self.set_black_color()
            self.if_empty_set_red_color()
            return

        passport.create_word_passport(pathFile)

        if self.ui.checkBoxCreateHint.checkState() == Qt.CheckState.Checked:
            passport.create_word_helper(pathFile)

        self.set_black_color()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = PassportTemplate()
    root.show()
    sys.exit(app.exec())
