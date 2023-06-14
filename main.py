import sys

from os import sep

from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDialog
from PyQt6.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, Qt

from infowindow import Ui_Dialog
from mainwindow import Ui_MainWindow
from constructors import Passport, PassportException

VERSION = "0.2.0"
SOURCE_URL = "https://github.com/GarborSergey/PassportTemplateReborn"


class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.labelVersionNumber.setText(f"VERSION - {VERSION}")
        self.ui.labelSourceLink.setText(f'<a href="{SOURCE_URL}">GitHub</a>')
        self.setWindowTitle("Info")
        icon = QtGui.QIcon(f'icons{sep}info_FILL0_wght400_GRAD0_opsz40.ico')
        self.setWindowIcon(icon)


class PassportTemplate(QMainWindow):
    def __init__(self):
        super(PassportTemplate, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.info = InfoWindow()
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

    def clear_all_input_field(self):
        for elem in self.uiVariableElementsPassportData:
            if type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QComboBox:
                self.uiVariableElementsPassportData[elem].setCurrentIndex(-1)
            elif type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QLineEdit:
                self.uiVariableElementsPassportData[elem].setText(None)

    def init_UI(self):
        icon = QtGui.QIcon(f'icons{sep}menu_book_FILL0_wght400_GRAD0_opsz40.ico')
        self.setWindowIcon(icon)
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

        self.clear_all_input_field()

        self.ui.lineEdDatabaseNumber.setValidator(QIntValidator(1000, 99999))
        self.ui.lineEdNominalCurrent.setValidator(QIntValidator(1, 9999))
        self.ui.lineEdNominalShortCircuitCurrent.setValidator(QDoubleValidator(0.0, 100.0, 1))
        self.ui.lineEdInputCrossSection.setValidator(QRegularExpressionValidator(QRegularExpression('\d{1}[x, х]\d{3}')))
        self.ui.lineEdWidth.setValidator(QIntValidator(0, 20000))
        self.ui.lineEdHeight.setValidator(QIntValidator(0, 3000))
        self.ui.lineEdDepth.setValidator(QIntValidator(0, 20000))
        self.ui.lineEdWeight.setValidator(QIntValidator(0, 20000))

        self.ui.btnCreatePassport.clicked.connect(self.create_passport)
        self.ui.btnClearFields.clicked.connect(self.clear_all_input_field)
        self.ui.btnInfo.clicked.connect(self.show_info)
        # self.auto_input_all_field()

    def if_empty_set_red_color(self):
        for elem in self.uiVariableElementsPassportData:
            if type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QComboBox:
                if self.uiVariableElementsPassportData[elem].currentText() == '':
                    elem.setStyleSheet("color: red;")
            elif type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QLineEdit:
                if self.uiVariableElementsPassportData[elem].text() == '':
                    elem.setStyleSheet("color: red;")

    def show_info(self):
        self.info.show()

    def auto_input_all_field(self):
        for elem in self.uiVariableElementsPassportData:
            if type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QComboBox:
                self.uiVariableElementsPassportData[elem].setCurrentIndex(0)
            elif type(self.uiVariableElementsPassportData[elem]) is QtWidgets.QLineEdit:
                self.uiVariableElementsPassportData[elem].setText('TestCase')

    def set_black_color(self):
        for elem in self.uiVariableElementsPassportData:
            elem.setStyleSheet("color: black;")

    def create_passport(self):
        pathFile = QFileDialog.getExistingDirectory()
        if not pathFile:
            return
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
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Заполните все поля!")
            error.setInformativeText("Некоторые поля незаполнены или заполнены некорректно, подсвечены красным")
            error.setIcon(QMessageBox.Icon.Warning)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.exec()
            return

        passport.create_word_passport(pathFile)

        if self.ui.checkBoxCreateHint.checkState() == Qt.CheckState.Checked:
            passport.create_word_helper(pathFile)

        self.set_black_color()
        success = QMessageBox()
        success.setWindowTitle("Success")
        success.setIcon(QMessageBox.Icon.Information)
        success.setInformativeText("Паспорт успешно создан.")
        success.setDetailedText(f"по пути: - {pathFile}{sep}{passport.construct_file_name()}")
        success.setStandardButtons(QMessageBox.StandardButton.Ok)
        success.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = PassportTemplate()
    root.show()
    sys.exit(app.exec())
