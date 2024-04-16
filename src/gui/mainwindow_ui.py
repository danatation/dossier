# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(679, 534)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.libraryTab = QWidget()
        self.libraryTab.setObjectName(u"libraryTab")
        self.gridLayout_2 = QGridLayout(self.libraryTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.libraryTabWidget = QTabWidget(self.libraryTab)
        self.libraryTabWidget.setObjectName(u"libraryTabWidget")
        self.libraryTabWidget.setTabPosition(QTabWidget.South)
        self.libraryTabWidget.setTabShape(QTabWidget.Rounded)
        self.modsTab = QWidget()
        self.modsTab.setObjectName(u"modsTab")
        self.gridLayout_3 = QGridLayout(self.modsTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter = QSplitter(self.modsTab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.modLibraryScrollArea = QScrollArea(self.splitter)
        self.modLibraryScrollArea.setObjectName(u"modLibraryScrollArea")
        self.modLibraryScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 56, 430))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.modLibraryScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.modLibraryScrollArea)
        self.modInfoFrame = QFrame(self.splitter)
        self.modInfoFrame.setObjectName(u"modInfoFrame")
        self.modInfoFrame.setAcceptDrops(False)
        self.modInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.modInfoFrame.setFrameShadow(QFrame.Raised)
        self.modInfoFrame.setLineWidth(1)
        self.gridLayout_4 = QGridLayout(self.modInfoFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(32, -1, 32, 16)
        self.modSizeLabel = QLabel(self.modInfoFrame)
        self.modSizeLabel.setObjectName(u"modSizeLabel")

        self.gridLayout_4.addWidget(self.modSizeLabel, 2, 2, 1, 1, Qt.AlignHCenter)

        self.modNameLabel = QLabel(self.modInfoFrame)
        self.modNameLabel.setObjectName(u"modNameLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.modNameLabel.sizePolicy().hasHeightForWidth())
        self.modNameLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.modNameLabel, 0, 1, 1, 1, Qt.AlignHCenter)

        self.modPlaytimeLabel = QLabel(self.modInfoFrame)
        self.modPlaytimeLabel.setObjectName(u"modPlaytimeLabel")
        sizePolicy2.setHeightForWidth(self.modPlaytimeLabel.sizePolicy().hasHeightForWidth())
        self.modPlaytimeLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.modPlaytimeLabel, 2, 0, 1, 1, Qt.AlignHCenter)

        self.modLastPlayedLabel = QLabel(self.modInfoFrame)
        self.modLastPlayedLabel.setObjectName(u"modLastPlayedLabel")

        self.gridLayout_4.addWidget(self.modLastPlayedLabel, 2, 1, 1, 1, Qt.AlignHCenter)

        self.modAuthorLabel = QLabel(self.modInfoFrame)
        self.modAuthorLabel.setObjectName(u"modAuthorLabel")
        sizePolicy2.setHeightForWidth(self.modAuthorLabel.sizePolicy().hasHeightForWidth())
        self.modAuthorLabel.setSizePolicy(sizePolicy2)
        self.modAuthorLabel.setMargin(0)
        self.modAuthorLabel.setIndent(-1)

        self.gridLayout_4.addWidget(self.modAuthorLabel, 1, 1, 1, 1, Qt.AlignHCenter)

        self.modOptionsButton = QPushButton(self.modInfoFrame)
        self.modOptionsButton.setObjectName(u"modOptionsButton")

        self.gridLayout_4.addWidget(self.modOptionsButton, 3, 2, 1, 1)

        self.modPlayButton = QPushButton(self.modInfoFrame)
        self.modPlayButton.setObjectName(u"modPlayButton")

        self.gridLayout_4.addWidget(self.modPlayButton, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.splitter.addWidget(self.modInfoFrame)

        self.gridLayout_3.addWidget(self.splitter, 1, 0, 1, 1)

        self.libraryTabWidget.addTab(self.modsTab, "")
        self.assetViewerTab = QWidget()
        self.assetViewerTab.setObjectName(u"assetViewerTab")
        self.libraryTabWidget.addTab(self.assetViewerTab, "")

        self.gridLayout_2.addWidget(self.libraryTabWidget, 0, 0, 1, 1)

        icon = QIcon()
        icon.addFile(u":/icons/bootstrap-icons/device-hdd.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.libraryTab, icon, "")
        self.storeTab = QWidget()
        self.storeTab.setObjectName(u"storeTab")
        self.tabWidget.addTab(self.storeTab, "")
        self.importTab = QWidget()
        self.importTab.setObjectName(u"importTab")
        self.gridLayout_6 = QGridLayout(self.importTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame = QFrame(self.importTab)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(2)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_2, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(16)
        self.gridLayout_5.setVerticalSpacing(8)
        self.gridLayout_5.setContentsMargins(64, -1, 64, -1)
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_5.addWidget(self.toolButton, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 1, 1, 1, 2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_5, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.importTab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(128, 0, 128, -1)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.importTab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.importTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.tabWidget.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.libraryTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.modSizeLabel.setText(QCoreApplication.translate("MainWindow", u"$MODSIZE", None))
        self.modNameLabel.setText(QCoreApplication.translate("MainWindow", u"$MODNAME", None))
        self.modPlaytimeLabel.setText(QCoreApplication.translate("MainWindow", u"$MODPLAYTIME", None))
        self.modLastPlayedLabel.setText(QCoreApplication.translate("MainWindow", u"$MODLASTPLAYED", None))
        self.modAuthorLabel.setText(QCoreApplication.translate("MainWindow", u"$MODAUTHOR", None))
        self.modOptionsButton.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.modPlayButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.libraryTabWidget.setTabText(self.libraryTabWidget.indexOf(self.modsTab), QCoreApplication.translate("MainWindow", u"Mods", None))
        self.libraryTabWidget.setTabText(self.libraryTabWidget.indexOf(self.assetViewerTab), QCoreApplication.translate("MainWindow", u"Asset Viewer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.libraryTab), QCoreApplication.translate("MainWindow", u"Library", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.storeTab), QCoreApplication.translate("MainWindow", u"Store", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Archive Path:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.importTab), QCoreApplication.translate("MainWindow", u"Import", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

