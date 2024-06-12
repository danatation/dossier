# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optionsdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Options(object):
    def setupUi(self, Options):
        if not Options.objectName():
            Options.setObjectName(u"Options")
        Options.resize(500, 613)
        self.gridLayout = QGridLayout(Options)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Options)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 490, 571))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(16, 16, 16, 0)
        self.optionsGeneralInfo = QGroupBox(self.scrollAreaWidgetContents)
        self.optionsGeneralInfo.setObjectName(u"optionsGeneralInfo")
        self.optionsGeneralInfo.setFlat(False)
        self.optionsGeneralInfo.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.optionsGeneralInfo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelNickname = QLabel(self.optionsGeneralInfo)
        self.labelNickname.setObjectName(u"labelNickname")

        self.gridLayout_2.addWidget(self.labelNickname, 0, 0, 1, 1)

        self.lineEditNickname = QLineEdit(self.optionsGeneralInfo)
        self.lineEditNickname.setObjectName(u"lineEditNickname")
        self.lineEditNickname.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEditNickname, 1, 0, 1, 2)

        self.labelCategories = QLabel(self.optionsGeneralInfo)
        self.labelCategories.setObjectName(u"labelCategories")

        self.gridLayout_2.addWidget(self.labelCategories, 2, 0, 1, 2)

        self.lineEditCategories = QLineEdit(self.optionsGeneralInfo)
        self.lineEditCategories.setObjectName(u"lineEditCategories")
        self.lineEditCategories.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEditCategories, 3, 0, 1, 2)

        self.labelCustomSaveDirectory = QLabel(self.optionsGeneralInfo)
        self.labelCustomSaveDirectory.setObjectName(u"labelCustomSaveDirectory")

        self.gridLayout_2.addWidget(self.labelCustomSaveDirectory, 4, 0, 1, 2)

        self.lineEditCustomSaveDirectory = QLineEdit(self.optionsGeneralInfo)
        self.lineEditCustomSaveDirectory.setObjectName(u"lineEditCustomSaveDirectory")
        self.lineEditCustomSaveDirectory.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.lineEditCustomSaveDirectory, 5, 0, 1, 1)

        self.browseCustomSaveDirectory = QPushButton(self.optionsGeneralInfo)
        self.browseCustomSaveDirectory.setObjectName(u"browseCustomSaveDirectory")

        self.gridLayout_2.addWidget(self.browseCustomSaveDirectory, 5, 1, 1, 1)


        self.gridLayout_5.addWidget(self.optionsGeneralInfo, 0, 0, 1, 1)

        self.optionsAdvanced = QGroupBox(self.scrollAreaWidgetContents)
        self.optionsAdvanced.setObjectName(u"optionsAdvanced")
        self.gridLayout_4 = QGridLayout(self.optionsAdvanced)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buttonDeleteMod = QPushButton(self.optionsAdvanced)
        self.buttonDeleteMod.setObjectName(u"buttonDeleteMod")

        self.gridLayout_4.addWidget(self.buttonDeleteMod, 3, 0, 1, 1)

        self.buttonFixBrokenLinks = QPushButton(self.optionsAdvanced)
        self.buttonFixBrokenLinks.setObjectName(u"buttonFixBrokenLinks")

        self.gridLayout_4.addWidget(self.buttonFixBrokenLinks, 0, 0, 1, 1)

        self.buttonResetStats = QPushButton(self.optionsAdvanced)
        self.buttonResetStats.setObjectName(u"buttonResetStats")

        self.gridLayout_4.addWidget(self.buttonResetStats, 1, 0, 1, 1)

        self.buttonDeleteSaves = QPushButton(self.optionsAdvanced)
        self.buttonDeleteSaves.setObjectName(u"buttonDeleteSaves")

        self.gridLayout_4.addWidget(self.buttonDeleteSaves, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 4, 1)


        self.gridLayout_5.addWidget(self.optionsAdvanced, 2, 0, 1, 1)

        self.optionsModParameters = QGroupBox(self.scrollAreaWidgetContents)
        self.optionsModParameters.setObjectName(u"optionsModParameters")
        self.gridLayout_3 = QGridLayout(self.optionsModParameters)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkDiscordRPC = QCheckBox(self.optionsModParameters)
        self.checkDiscordRPC.setObjectName(u"checkDiscordRPC")
        self.checkDiscordRPC.setTristate(True)

        self.gridLayout_3.addWidget(self.checkDiscordRPC, 4, 0, 1, 1)

        self.checkDefaultSaveDirectory = QCheckBox(self.optionsModParameters)
        self.checkDefaultSaveDirectory.setObjectName(u"checkDefaultSaveDirectory")
        self.checkDefaultSaveDirectory.setTristate(True)

        self.gridLayout_3.addWidget(self.checkDefaultSaveDirectory, 0, 0, 1, 1)

        self.checkSkipMainMenu = QCheckBox(self.optionsModParameters)
        self.checkSkipMainMenu.setObjectName(u"checkSkipMainMenu")
        self.checkSkipMainMenu.setTristate(True)

        self.gridLayout_3.addWidget(self.checkSkipMainMenu, 3, 0, 1, 1)

        self.checkSkipSplashScreen = QCheckBox(self.optionsModParameters)
        self.checkSkipSplashScreen.setObjectName(u"checkSkipSplashScreen")
        self.checkSkipSplashScreen.setTristate(True)

        self.gridLayout_3.addWidget(self.checkSkipSplashScreen, 2, 0, 1, 1)

        self.checkCustomSaveDirectory = QCheckBox(self.optionsModParameters)
        self.checkCustomSaveDirectory.setObjectName(u"checkCustomSaveDirectory")
        self.checkCustomSaveDirectory.setChecked(False)
        self.checkCustomSaveDirectory.setTristate(False)

        self.gridLayout_3.addWidget(self.checkCustomSaveDirectory, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.optionsModParameters, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Options)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Options)

        QMetaObject.connectSlotsByName(Options)
    # setupUi

    def retranslateUi(self, Options):
        Options.setWindowTitle(QCoreApplication.translate("Options", u"Dialog", None))
        self.optionsGeneralInfo.setTitle(QCoreApplication.translate("Options", u"General Info (Mod Name)", None))
        self.labelNickname.setText(QCoreApplication.translate("Options", u"Nickname", None))
        self.lineEditNickname.setPlaceholderText(QCoreApplication.translate("Options", u"Mod Name", None))
        self.labelCategories.setText(QCoreApplication.translate("Options", u"Categories", None))
        self.lineEditCategories.setPlaceholderText(QCoreApplication.translate("Options", u"Separated by commas,", None))
        self.labelCustomSaveDirectory.setText(QCoreApplication.translate("Options", u"Custom save directory", None))
        self.lineEditCustomSaveDirectory.setPlaceholderText(QCoreApplication.translate("Options", u"I would pick game/saves/ if i were you", None))
        self.browseCustomSaveDirectory.setText(QCoreApplication.translate("Options", u"Browse", None))
        self.optionsAdvanced.setTitle(QCoreApplication.translate("Options", u"Advanced", None))
        self.buttonDeleteMod.setText(QCoreApplication.translate("Options", u"Delete mod", None))
        self.buttonFixBrokenLinks.setText(QCoreApplication.translate("Options", u"Fix broken links", None))
        self.buttonResetStats.setText(QCoreApplication.translate("Options", u"Reset stats", None))
        self.buttonDeleteSaves.setText(QCoreApplication.translate("Options", u"Delete saves", None))
        self.optionsModParameters.setTitle(QCoreApplication.translate("Options", u"Mod parameters", None))
        self.checkDiscordRPC.setText(QCoreApplication.translate("Options", u"Enable Discord RPC", None))
        self.checkDefaultSaveDirectory.setText(QCoreApplication.translate("Options", u"Use default Ren'py save directory (game/saves/)", None))
        self.checkSkipMainMenu.setText(QCoreApplication.translate("Options", u"Skip main menu", None))
        self.checkSkipSplashScreen.setText(QCoreApplication.translate("Options", u"Skip splash screen", None))
        self.checkCustomSaveDirectory.setText(QCoreApplication.translate("Options", u"Use custom save directory", None))
    # retranslateUi

