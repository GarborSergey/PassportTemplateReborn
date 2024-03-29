# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1100, 714)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 714))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 714))
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(0, 0, 0, 255), stop:0.443182 rgba(255, 255, 255, 255));\n"
"font-family: \"MADE Likes Slab\";")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 120, 1081, 261))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("icons/electric_meter_FILL0_wght400_GRAD0_opsz40.svg"))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelPanelAssignment = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelPanelAssignment.setFont(font)
        self.labelPanelAssignment.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelPanelAssignment.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelPanelAssignment.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelPanelAssignment.setObjectName("labelPanelAssignment")
        self.horizontalLayout_6.addWidget(self.labelPanelAssignment)
        self.cboxPanelAssignment = QtWidgets.QComboBox(parent=self.frame)
        self.cboxPanelAssignment.setMaximumSize(QtCore.QSize(526, 16777215))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxPanelAssignment.setFont(font)
        self.cboxPanelAssignment.setObjectName("cboxPanelAssignment")
        self.horizontalLayout_6.addWidget(self.cboxPanelAssignment)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelPurposeOfTheIntroductoryControlUnit = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelPurposeOfTheIntroductoryControlUnit.setFont(font)
        self.labelPurposeOfTheIntroductoryControlUnit.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelPurposeOfTheIntroductoryControlUnit.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelPurposeOfTheIntroductoryControlUnit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelPurposeOfTheIntroductoryControlUnit.setObjectName("labelPurposeOfTheIntroductoryControlUnit")
        self.horizontalLayout_5.addWidget(self.labelPurposeOfTheIntroductoryControlUnit)
        self.cboxPurposeOfTheIntroductoryControlUnit = QtWidgets.QComboBox(parent=self.frame)
        self.cboxPurposeOfTheIntroductoryControlUnit.setMaximumSize(QtCore.QSize(526, 16777215))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxPurposeOfTheIntroductoryControlUnit.setFont(font)
        self.cboxPurposeOfTheIntroductoryControlUnit.setObjectName("cboxPurposeOfTheIntroductoryControlUnit")
        self.horizontalLayout_5.addWidget(self.cboxPurposeOfTheIntroductoryControlUnit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelAdditionalEquipment = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelAdditionalEquipment.setFont(font)
        self.labelAdditionalEquipment.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelAdditionalEquipment.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelAdditionalEquipment.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAdditionalEquipment.setObjectName("labelAdditionalEquipment")
        self.horizontalLayout_4.addWidget(self.labelAdditionalEquipment)
        self.cboxAdditionalEquipment = QtWidgets.QComboBox(parent=self.frame)
        self.cboxAdditionalEquipment.setMinimumSize(QtCore.QSize(526, 0))
        self.cboxAdditionalEquipment.setMaximumSize(QtCore.QSize(526, 16777215))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxAdditionalEquipment.setFont(font)
        self.cboxAdditionalEquipment.setObjectName("cboxAdditionalEquipment")
        self.horizontalLayout_4.addWidget(self.cboxAdditionalEquipment)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelProtectiveDevices = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelProtectiveDevices.setFont(font)
        self.labelProtectiveDevices.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelProtectiveDevices.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelProtectiveDevices.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelProtectiveDevices.setObjectName("labelProtectiveDevices")
        self.horizontalLayout_3.addWidget(self.labelProtectiveDevices)
        self.cboxProtectiveDevices = QtWidgets.QComboBox(parent=self.frame)
        self.cboxProtectiveDevices.setMaximumSize(QtCore.QSize(526, 16777215))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxProtectiveDevices.setFont(font)
        self.cboxProtectiveDevices.setObjectName("cboxProtectiveDevices")
        self.horizontalLayout_3.addWidget(self.cboxProtectiveDevices)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelIngressProtectionRating = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelIngressProtectionRating.setFont(font)
        self.labelIngressProtectionRating.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelIngressProtectionRating.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelIngressProtectionRating.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelIngressProtectionRating.setObjectName("labelIngressProtectionRating")
        self.horizontalLayout_2.addWidget(self.labelIngressProtectionRating)
        self.cboxIngressProtectionRating = QtWidgets.QComboBox(parent=self.frame)
        self.cboxIngressProtectionRating.setMaximumSize(QtCore.QSize(526, 16777215))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxIngressProtectionRating.setFont(font)
        self.cboxIngressProtectionRating.setObjectName("cboxIngressProtectionRating")
        self.horizontalLayout_2.addWidget(self.cboxIngressProtectionRating)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelClimaticVersion = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelClimaticVersion.setFont(font)
        self.labelClimaticVersion.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelClimaticVersion.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelClimaticVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelClimaticVersion.setObjectName("labelClimaticVersion")
        self.horizontalLayout.addWidget(self.labelClimaticVersion)
        self.cboxClimaticVersion = QtWidgets.QComboBox(parent=self.frame)
        self.cboxClimaticVersion.setMaximumSize(QtCore.QSize(526, 16777215))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxClimaticVersion.setFont(font)
        self.cboxClimaticVersion.setObjectName("cboxClimaticVersion")
        self.horizontalLayout.addWidget(self.cboxClimaticVersion)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.frame1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(10, 390, 641, 316))
        self.frame1.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout.setObjectName("gridLayout")
        self.labelInputCrossSection = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelInputCrossSection.setFont(font)
        self.labelInputCrossSection.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelInputCrossSection.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelInputCrossSection.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelInputCrossSection.setObjectName("labelInputCrossSection")
        self.gridLayout.addWidget(self.labelInputCrossSection, 6, 0, 1, 1)
        self.labelProtectionClass = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelProtectionClass.setFont(font)
        self.labelProtectionClass.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelProtectionClass.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelProtectionClass.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelProtectionClass.setObjectName("labelProtectionClass")
        self.gridLayout.addWidget(self.labelProtectionClass, 8, 0, 1, 1)
        self.labelInstallationMethod = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelInstallationMethod.setFont(font)
        self.labelInstallationMethod.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelInstallationMethod.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelInstallationMethod.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelInstallationMethod.setObjectName("labelInstallationMethod")
        self.gridLayout.addWidget(self.labelInstallationMethod, 7, 0, 1, 1)
        self.cboxProtectionClass = QtWidgets.QComboBox(parent=self.frame1)
        self.cboxProtectionClass.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxProtectionClass.setFont(font)
        self.cboxProtectionClass.setObjectName("cboxProtectionClass")
        self.gridLayout.addWidget(self.cboxProtectionClass, 8, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.frame1)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.labelNominalCurrent = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelNominalCurrent.setFont(font)
        self.labelNominalCurrent.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelNominalCurrent.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelNominalCurrent.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelNominalCurrent.setObjectName("labelNominalCurrent")
        self.gridLayout.addWidget(self.labelNominalCurrent, 3, 0, 1, 1)
        self.lineEdNominalCurrent = QtWidgets.QLineEdit(parent=self.frame1)
        self.lineEdNominalCurrent.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdNominalCurrent.setFont(font)
        self.lineEdNominalCurrent.setObjectName("lineEdNominalCurrent")
        self.gridLayout.addWidget(self.lineEdNominalCurrent, 3, 1, 1, 1)
        self.labelDatabaseNumber = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelDatabaseNumber.setFont(font)
        self.labelDatabaseNumber.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelDatabaseNumber.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelDatabaseNumber.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelDatabaseNumber.setObjectName("labelDatabaseNumber")
        self.gridLayout.addWidget(self.labelDatabaseNumber, 2, 0, 1, 1)
        self.lineEdNameBox = QtWidgets.QLineEdit(parent=self.frame1)
        self.lineEdNameBox.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdNameBox.setFont(font)
        self.lineEdNameBox.setObjectName("lineEdNameBox")
        self.gridLayout.addWidget(self.lineEdNameBox, 1, 1, 1, 1)
        self.lineEdDatabaseNumber = QtWidgets.QLineEdit(parent=self.frame1)
        self.lineEdDatabaseNumber.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdDatabaseNumber.setFont(font)
        self.lineEdDatabaseNumber.setObjectName("lineEdDatabaseNumber")
        self.gridLayout.addWidget(self.lineEdDatabaseNumber, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.frame1)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("icons/receipt_long_FILL1_wght300_GRAD0_opsz40.svg"))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 1)
        self.lineEdNominalShortCircuitCurrent = QtWidgets.QLineEdit(parent=self.frame1)
        self.lineEdNominalShortCircuitCurrent.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdNominalShortCircuitCurrent.setFont(font)
        self.lineEdNominalShortCircuitCurrent.setObjectName("lineEdNominalShortCircuitCurrent")
        self.gridLayout.addWidget(self.lineEdNominalShortCircuitCurrent, 4, 1, 1, 1)
        self.cboxSystemGrounding = QtWidgets.QComboBox(parent=self.frame1)
        self.cboxSystemGrounding.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxSystemGrounding.setFont(font)
        self.cboxSystemGrounding.setObjectName("cboxSystemGrounding")
        self.gridLayout.addWidget(self.cboxSystemGrounding, 5, 1, 1, 1)
        self.labelNominalShortCircuitCurrent = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelNominalShortCircuitCurrent.setFont(font)
        self.labelNominalShortCircuitCurrent.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelNominalShortCircuitCurrent.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelNominalShortCircuitCurrent.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelNominalShortCircuitCurrent.setObjectName("labelNominalShortCircuitCurrent")
        self.gridLayout.addWidget(self.labelNominalShortCircuitCurrent, 4, 0, 1, 1)
        self.labelSystemGrounding = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelSystemGrounding.setFont(font)
        self.labelSystemGrounding.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelSystemGrounding.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelSystemGrounding.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelSystemGrounding.setObjectName("labelSystemGrounding")
        self.gridLayout.addWidget(self.labelSystemGrounding, 5, 0, 1, 1)
        self.lineEdInputCrossSection = QtWidgets.QLineEdit(parent=self.frame1)
        self.lineEdInputCrossSection.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdInputCrossSection.setFont(font)
        self.lineEdInputCrossSection.setObjectName("lineEdInputCrossSection")
        self.gridLayout.addWidget(self.lineEdInputCrossSection, 6, 1, 1, 1)
        self.cboxInstallationMethod = QtWidgets.QComboBox(parent=self.frame1)
        self.cboxInstallationMethod.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.cboxInstallationMethod.setFont(font)
        self.cboxInstallationMethod.setObjectName("cboxInstallationMethod")
        self.gridLayout.addWidget(self.cboxInstallationMethod, 7, 1, 1, 1)
        self.labelNameBox = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelNameBox.setFont(font)
        self.labelNameBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelNameBox.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelNameBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelNameBox.setObjectName("labelNameBox")
        self.gridLayout.addWidget(self.labelNameBox, 1, 0, 1, 1)
        self.frame2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(660, 390, 431, 184))
        self.frame2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")
        self.frame2.setObjectName("frame2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelHeight = QtWidgets.QLabel(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelHeight.setFont(font)
        self.labelHeight.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelHeight.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelHeight.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelHeight.setObjectName("labelHeight")
        self.gridLayout_2.addWidget(self.labelHeight, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(parent=self.frame2)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        self.label_28 = QtWidgets.QLabel(parent=self.frame2)
        self.label_28.setEnabled(True)
        self.label_28.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("icons/straighten_FILL0_wght400_GRAD0_opsz40.svg"))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_8.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(parent=self.frame2)
        self.label_29.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(18)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color: none;\n"
"border: none;")
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("icons/weight_FILL0_wght400_GRAD0_opsz40.svg"))
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_8.addWidget(self.label_29)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 2)
        self.labelWidth = QtWidgets.QLabel(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelWidth.setFont(font)
        self.labelWidth.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelWidth.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelWidth.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelWidth.setObjectName("labelWidth")
        self.gridLayout_2.addWidget(self.labelWidth, 2, 0, 1, 1)
        self.lineEdWidth = QtWidgets.QLineEdit(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdWidth.setFont(font)
        self.lineEdWidth.setText("")
        self.lineEdWidth.setObjectName("lineEdWidth")
        self.gridLayout_2.addWidget(self.lineEdWidth, 2, 1, 1, 1)
        self.lineEdWeight = QtWidgets.QLineEdit(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdWeight.setFont(font)
        self.lineEdWeight.setObjectName("lineEdWeight")
        self.gridLayout_2.addWidget(self.lineEdWeight, 4, 1, 1, 1)
        self.labelDepth = QtWidgets.QLabel(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelDepth.setFont(font)
        self.labelDepth.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelDepth.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelDepth.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelDepth.setObjectName("labelDepth")
        self.gridLayout_2.addWidget(self.labelDepth, 3, 0, 1, 1)
        self.lineEdDepth = QtWidgets.QLineEdit(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdDepth.setFont(font)
        self.lineEdDepth.setText("")
        self.lineEdDepth.setObjectName("lineEdDepth")
        self.gridLayout_2.addWidget(self.lineEdDepth, 3, 1, 1, 1)
        self.labelWeight = QtWidgets.QLabel(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.labelWeight.setFont(font)
        self.labelWeight.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelWeight.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.labelWeight.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelWeight.setObjectName("labelWeight")
        self.gridLayout_2.addWidget(self.labelWeight, 4, 0, 1, 1)
        self.lineEdHeight = QtWidgets.QLineEdit(parent=self.frame2)
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.lineEdHeight.setFont(font)
        self.lineEdHeight.setText("")
        self.lineEdHeight.setObjectName("lineEdHeight")
        self.gridLayout_2.addWidget(self.lineEdHeight, 1, 1, 1, 1)
        self.frame3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(660, 580, 431, 125))
        self.frame3.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")
        self.frame3.setObjectName("frame3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxCreateHint = QtWidgets.QCheckBox(parent=self.frame3)
        self.checkBoxCreateHint.setMaximumSize(QtCore.QSize(16677, 50))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBoxCreateHint.setFont(font)
        self.checkBoxCreateHint.setStyleSheet("QCheckBox{ \n"
"    font:18px;\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 1px solid black;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid black;\n"
"    image: url(icons/done_FILL1_wght300_GRAD0_opsz40.svg);\n"
"}")
        self.checkBoxCreateHint.setIconSize(QtCore.QSize(1, 1))
        self.checkBoxCreateHint.setCheckable(True)
        self.checkBoxCreateHint.setChecked(False)
        self.checkBoxCreateHint.setAutoRepeat(False)
        self.checkBoxCreateHint.setAutoExclusive(False)
        self.checkBoxCreateHint.setAutoRepeatDelay(200)
        self.checkBoxCreateHint.setAutoRepeatInterval(97)
        self.checkBoxCreateHint.setObjectName("checkBoxCreateHint")
        self.verticalLayout_2.addWidget(self.checkBoxCreateHint)
        self.btnCreatePassport = QtWidgets.QPushButton(parent=self.frame3)
        self.btnCreatePassport.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("MADE Likes Slab")
        font.setPointSize(14)
        self.btnCreatePassport.setFont(font)
        self.btnCreatePassport.setStyleSheet("QPushButton {\n"
"color: black;\n"
"backgroud-color: rgb(138, 138, 138);\n"
"border: 1px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(25, 25, 25, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(25, 25, 25, 95);\n"
"margin-top: 1px;\n"
"margin-right: 1px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/save_FILL0_wght400_GRAD0_opsz40.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCreatePassport.setIcon(icon)
        self.btnCreatePassport.setIconSize(QtCore.QSize(40, 40))
        self.btnCreatePassport.setObjectName("btnCreatePassport")
        self.verticalLayout_2.addWidget(self.btnCreatePassport)
        self.lableCompanyLogo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lableCompanyLogo.setGeometry(QtCore.QRect(10, -10, 441, 151))
        self.lableCompanyLogo.setStyleSheet("background-color: none;\n"
"border: none;")
        self.lableCompanyLogo.setText("")
        self.lableCompanyLogo.setPixmap(QtGui.QPixmap("Pictures/eltat-logo-pc.png"))
        self.lableCompanyLogo.setScaledContents(True)
        self.lableCompanyLogo.setObjectName("lableCompanyLogo")
        self.btnClearFields = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClearFields.setGeometry(QtCore.QRect(980, 30, 40, 40))
        self.btnClearFields.setStyleSheet("QPushButton {\n"
"background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(25, 25, 25, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(25, 25, 25, 95);\n"
"margin-top: 1px;\n"
"margin-right: 1px;\n"
"}")
        self.btnClearFields.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/delete_FILL0_wght400_GRAD0_opsz40.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnClearFields.setIcon(icon1)
        self.btnClearFields.setIconSize(QtCore.QSize(40, 40))
        self.btnClearFields.setObjectName("btnClearFields")
        self.btnInfo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnInfo.setGeometry(QtCore.QRect(1030, 30, 40, 40))
        self.btnInfo.setStyleSheet("QPushButton {\n"
"background-color: none;\n"
"border: 1px solid black;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(25, 25, 25, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(25, 25, 25, 95);\n"
"margin-top: 1px;\n"
"margin-right: 1px;\n"
"}")
        self.btnInfo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/info_FILL0_wght400_GRAD0_opsz40.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnInfo.setIcon(icon2)
        self.btnInfo.setIconSize(QtCore.QSize(40, 40))
        self.btnInfo.setObjectName("btnInfo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cboxPanelAssignment, self.cboxPurposeOfTheIntroductoryControlUnit)
        MainWindow.setTabOrder(self.cboxPurposeOfTheIntroductoryControlUnit, self.cboxAdditionalEquipment)
        MainWindow.setTabOrder(self.cboxAdditionalEquipment, self.cboxProtectiveDevices)
        MainWindow.setTabOrder(self.cboxProtectiveDevices, self.cboxIngressProtectionRating)
        MainWindow.setTabOrder(self.cboxIngressProtectionRating, self.cboxClimaticVersion)
        MainWindow.setTabOrder(self.cboxClimaticVersion, self.lineEdNameBox)
        MainWindow.setTabOrder(self.lineEdNameBox, self.lineEdDatabaseNumber)
        MainWindow.setTabOrder(self.lineEdDatabaseNumber, self.lineEdNominalCurrent)
        MainWindow.setTabOrder(self.lineEdNominalCurrent, self.lineEdNominalShortCircuitCurrent)
        MainWindow.setTabOrder(self.lineEdNominalShortCircuitCurrent, self.cboxSystemGrounding)
        MainWindow.setTabOrder(self.cboxSystemGrounding, self.lineEdInputCrossSection)
        MainWindow.setTabOrder(self.lineEdInputCrossSection, self.cboxInstallationMethod)
        MainWindow.setTabOrder(self.cboxInstallationMethod, self.cboxProtectionClass)
        MainWindow.setTabOrder(self.cboxProtectionClass, self.lineEdHeight)
        MainWindow.setTabOrder(self.lineEdHeight, self.lineEdWidth)
        MainWindow.setTabOrder(self.lineEdWidth, self.lineEdDepth)
        MainWindow.setTabOrder(self.lineEdDepth, self.lineEdWeight)
        MainWindow.setTabOrder(self.lineEdWeight, self.btnCreatePassport)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Passport Consructor"))
        self.label_2.setText(_translate("MainWindow", "Условное обозначение"))
        self.labelPanelAssignment.setText(_translate("MainWindow", "Назначение панели "))
        self.labelPurposeOfTheIntroductoryControlUnit.setText(_translate("MainWindow", "Назначение вводного аппарата управления "))
        self.labelAdditionalEquipment.setText(_translate("MainWindow", "Наличие дополнительного оборудования "))
        self.labelProtectiveDevices.setText(_translate("MainWindow", "Защитные аппараты на отходящих линиях "))
        self.labelIngressProtectionRating.setText(_translate("MainWindow", "Степень защиты IP "))
        self.labelClimaticVersion.setText(_translate("MainWindow", "Климатическое исполнение "))
        self.labelInputCrossSection.setText(_translate("MainWindow", "Максимальное сечение жил [Nxмм^2] "))
        self.labelProtectionClass.setText(_translate("MainWindow", "Класс защиты "))
        self.labelInstallationMethod.setText(_translate("MainWindow", "Способ установки "))
        self.label_15.setText(_translate("MainWindow", "Общие данные"))
        self.labelNominalCurrent.setText(_translate("MainWindow", "Номинальный ток устройства [A] "))
        self.labelDatabaseNumber.setText(_translate("MainWindow", "Номер заказа в базе "))
        self.labelNominalShortCircuitCurrent.setText(_translate("MainWindow", "Минимальный ток КЗ  [kA] "))
        self.labelSystemGrounding.setText(_translate("MainWindow", "Система заземления "))
        self.labelNameBox.setText(_translate("MainWindow", "Название щита "))
        self.labelHeight.setText(_translate("MainWindow", "Высота [мм]"))
        self.label_17.setText(_translate("MainWindow", "Габаритные размеры, вес "))
        self.labelWidth.setText(_translate("MainWindow", "Ширина [мм]"))
        self.labelDepth.setText(_translate("MainWindow", "Глубина [мм]"))
        self.labelWeight.setText(_translate("MainWindow", "Вес [кг]"))
        self.checkBoxCreateHint.setText(_translate("MainWindow", "Создать подсказку для шильдика"))
        self.btnCreatePassport.setText(_translate("MainWindow", "Создать паспорт"))
