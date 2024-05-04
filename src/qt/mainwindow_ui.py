# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 634)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.mainTabWidget = QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.mainTabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.mainTabWidget.setDocumentMode(True)
        self.mainTabWidget.setTabsClosable(False)
        self.mainTabWidget.setMovable(False)
        self.libraryTab = QWidget()
        self.libraryTab.setObjectName(u"libraryTab")
        self.gridLayout_3 = QGridLayout(self.libraryTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.libraryImportButton = QPushButton(self.libraryTab)
        self.libraryImportButton.setObjectName(u"libraryImportButton")
        self.libraryImportButton.setCheckable(False)
        self.libraryImportButton.setFlat(True)

        self.gridLayout_3.addWidget(self.libraryImportButton, 0, 1, 1, 1)

        self.librarySettingsButton = QPushButton(self.libraryTab)
        self.librarySettingsButton.setObjectName(u"librarySettingsButton")
        self.librarySettingsButton.setCheckable(False)
        self.librarySettingsButton.setFlat(True)

        self.gridLayout_3.addWidget(self.librarySettingsButton, 0, 3, 1, 1)

        self.librarySplitter = QSplitter(self.libraryTab)
        self.librarySplitter.setObjectName(u"librarySplitter")
        self.librarySplitter.setOrientation(Qt.Orientation.Horizontal)
        self.libraryModScrollArea = QScrollArea(self.librarySplitter)
        self.libraryModScrollArea.setObjectName(u"libraryModScrollArea")
        self.libraryModScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.libraryModScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.libraryModScrollArea.setWidgetResizable(True)
        self.libraryModScrollAreaWidgetContents = QWidget()
        self.libraryModScrollAreaWidgetContents.setObjectName(u"libraryModScrollAreaWidgetContents")
        self.libraryModScrollAreaWidgetContents.setGeometry(QRect(0, 0, 56, 519))
        self.gridLayout_4 = QGridLayout(self.libraryModScrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(4, -1, -1, -1)
        self.libraryModScrollArea.setWidget(self.libraryModScrollAreaWidgetContents)
        self.librarySplitter.addWidget(self.libraryModScrollArea)
        self.libraryViewTabWidget = QTabWidget(self.librarySplitter)
        self.libraryViewTabWidget.setObjectName(u"libraryViewTabWidget")
        self.libraryViewTabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.libraryViewTabWidget.setDocumentMode(True)
        self.libraryNormalViewTab = QWidget()
        self.libraryNormalViewTab.setObjectName(u"libraryNormalViewTab")
        self.gridLayout_6 = QGridLayout(self.libraryNormalViewTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.libraryNormalViewScrollArea = QScrollArea(self.libraryNormalViewTab)
        self.libraryNormalViewScrollArea.setObjectName(u"libraryNormalViewScrollArea")
        self.libraryNormalViewScrollArea.setWidgetResizable(True)
        self.libraryNormalViewScrollAreaWidgetContents = QWidget()
        self.libraryNormalViewScrollAreaWidgetContents.setObjectName(u"libraryNormalViewScrollAreaWidgetContents")
        self.libraryNormalViewScrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 478))
        self.gridLayout_9 = QGridLayout(self.libraryNormalViewScrollAreaWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.libraryNormalViewScrollArea.setWidget(self.libraryNormalViewScrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.libraryNormalViewScrollArea, 0, 0, 1, 1)

        self.libraryViewTabWidget.addTab(self.libraryNormalViewTab, "")
        self.libraryAssetViewTab = QWidget()
        self.libraryAssetViewTab.setObjectName(u"libraryAssetViewTab")
        self.gridLayout = QGridLayout(self.libraryAssetViewTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.libraryAssetViewScrollArea = QScrollArea(self.libraryAssetViewTab)
        self.libraryAssetViewScrollArea.setObjectName(u"libraryAssetViewScrollArea")
        self.libraryAssetViewScrollArea.setWidgetResizable(True)
        self.libraryAssetViewScrollAreaWidgetContents = QWidget()
        self.libraryAssetViewScrollAreaWidgetContents.setObjectName(u"libraryAssetViewScrollAreaWidgetContents")
        self.libraryAssetViewScrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 478))
        self.gridLayout_8 = QGridLayout(self.libraryAssetViewScrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.libraryAssetViewScrollArea.setWidget(self.libraryAssetViewScrollAreaWidgetContents)

        self.gridLayout.addWidget(self.libraryAssetViewScrollArea, 0, 0, 1, 1)

        self.libraryViewTabWidget.addTab(self.libraryAssetViewTab, "")
        self.librarySplitter.addWidget(self.libraryViewTabWidget)

        self.gridLayout_3.addWidget(self.librarySplitter, 1, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.mainTabWidget.addTab(self.libraryTab, "")
        self.storeTab = QWidget()
        self.storeTab.setObjectName(u"storeTab")
        self.gridLayout_5 = QGridLayout(self.storeTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.storeSettingsButton = QPushButton(self.storeTab)
        self.storeSettingsButton.setObjectName(u"storeSettingsButton")
        self.storeSettingsButton.setCheckable(False)
        self.storeSettingsButton.setFlat(True)

        self.gridLayout_5.addWidget(self.storeSettingsButton, 0, 2, 1, 1)

        self.storeCategoryTab = QTabWidget(self.storeTab)
        self.storeCategoryTab.setObjectName(u"storeCategoryTab")
        self.storeCategoryTab.setTabPosition(QTabWidget.TabPosition.South)
        self.storeCategoryTab.setElideMode(Qt.TextElideMode.ElideNone)
        self.storeCategory_01 = QWidget()
        self.storeCategory_01.setObjectName(u"storeCategory_01")
        self.gridLayout_7 = QGridLayout(self.storeCategory_01)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.storeCategoryTab.addTab(self.storeCategory_01, "")
        self.storeCategory_02 = QWidget()
        self.storeCategory_02.setObjectName(u"storeCategory_02")
        self.gridLayout_12 = QGridLayout(self.storeCategory_02)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.storeCategoryTab.addTab(self.storeCategory_02, "")
        self.storeCategory_03 = QWidget()
        self.storeCategory_03.setObjectName(u"storeCategory_03")
        self.gridLayout_23 = QGridLayout(self.storeCategory_03)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.storeCategoryTab.addTab(self.storeCategory_03, "")
        self.storeCategory_04 = QWidget()
        self.storeCategory_04.setObjectName(u"storeCategory_04")
        self.gridLayout_24 = QGridLayout(self.storeCategory_04)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.storeCategoryTab.addTab(self.storeCategory_04, "")
        self.storeCategory_05 = QWidget()
        self.storeCategory_05.setObjectName(u"storeCategory_05")
        self.gridLayout_25 = QGridLayout(self.storeCategory_05)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.storeCategoryTab.addTab(self.storeCategory_05, "")
        self.storeCategory_06 = QWidget()
        self.storeCategory_06.setObjectName(u"storeCategory_06")
        self.gridLayout_26 = QGridLayout(self.storeCategory_06)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.storeCategoryTab.addTab(self.storeCategory_06, "")
        self.storeCategory_07 = QWidget()
        self.storeCategory_07.setObjectName(u"storeCategory_07")
        self.gridLayout_27 = QGridLayout(self.storeCategory_07)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.storeCategoryTab.addTab(self.storeCategory_07, "")
        self.storeCategory_08 = QWidget()
        self.storeCategory_08.setObjectName(u"storeCategory_08")
        self.gridLayout_28 = QGridLayout(self.storeCategory_08)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.storeCategoryTab.addTab(self.storeCategory_08, "")
        self.storeCategory_09 = QWidget()
        self.storeCategory_09.setObjectName(u"storeCategory_09")
        self.gridLayout_29 = QGridLayout(self.storeCategory_09)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.storeCategoryTab.addTab(self.storeCategory_09, "")
        self.storeCategory_10 = QWidget()
        self.storeCategory_10.setObjectName(u"storeCategory_10")
        self.gridLayout_30 = QGridLayout(self.storeCategory_10)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.storeCategoryTab.addTab(self.storeCategory_10, "")
        self.storeCategory_11 = QWidget()
        self.storeCategory_11.setObjectName(u"storeCategory_11")
        self.gridLayout_31 = QGridLayout(self.storeCategory_11)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.storeCategoryTab.addTab(self.storeCategory_11, "")
        self.storeCategory_12 = QWidget()
        self.storeCategory_12.setObjectName(u"storeCategory_12")
        self.gridLayout_32 = QGridLayout(self.storeCategory_12)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.storeCategoryTab.addTab(self.storeCategory_12, "")
        self.storeCategory_13 = QWidget()
        self.storeCategory_13.setObjectName(u"storeCategory_13")
        self.gridLayout_33 = QGridLayout(self.storeCategory_13)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.storeCategoryTab.addTab(self.storeCategory_13, "")
        self.storeCategory_14 = QWidget()
        self.storeCategory_14.setObjectName(u"storeCategory_14")
        self.gridLayout_34 = QGridLayout(self.storeCategory_14)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.storeCategoryTab.addTab(self.storeCategory_14, "")
        self.storeCategory_15 = QWidget()
        self.storeCategory_15.setObjectName(u"storeCategory_15")
        self.gridLayout_35 = QGridLayout(self.storeCategory_15)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.storeCategoryTab.addTab(self.storeCategory_15, "")

        self.gridLayout_5.addWidget(self.storeCategoryTab, 1, 0, 1, 3)

        self.storeFetchModListButton = QPushButton(self.storeTab)
        self.storeFetchModListButton.setObjectName(u"storeFetchModListButton")
        self.storeFetchModListButton.setFlat(True)

        self.gridLayout_5.addWidget(self.storeFetchModListButton, 0, 0, 1, 1)

        self.mainTabWidget.addTab(self.storeTab, "")

        self.gridLayout_2.addWidget(self.mainTabWidget, 0, 0, 1, 5)

        self.searchLineEdit = QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setDragEnabled(True)
        self.searchLineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.searchLineEdit, 1, 0, 1, 1)

        self.statusBar = QLabel(self.centralwidget)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setTextFormat(Qt.TextFormat.AutoText)

        self.gridLayout_2.addWidget(self.statusBar, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainTabWidget.setCurrentIndex(0)
        self.libraryViewTabWidget.setCurrentIndex(0)
        self.storeCategoryTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.libraryImportButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.librarySettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.libraryViewTabWidget.setTabText(self.libraryViewTabWidget.indexOf(self.libraryNormalViewTab), QCoreApplication.translate("MainWindow", u"Normal View", None))
        self.libraryViewTabWidget.setTabText(self.libraryViewTabWidget.indexOf(self.libraryAssetViewTab), QCoreApplication.translate("MainWindow", u"Asset View", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.libraryTab), QCoreApplication.translate("MainWindow", u"Library", None))
        self.storeSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_01), QCoreApplication.translate("MainWindow", u"Mod List", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_02), QCoreApplication.translate("MainWindow", u"Multiple/All", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_03), QCoreApplication.translate("MainWindow", u"Yuri", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_04), QCoreApplication.translate("MainWindow", u"Natsuki", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_05), QCoreApplication.translate("MainWindow", u"Sayori", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_06), QCoreApplication.translate("MainWindow", u"Monika", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_07), QCoreApplication.translate("MainWindow", u"Drama", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_08), QCoreApplication.translate("MainWindow", u"Horror", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_09), QCoreApplication.translate("MainWindow", u"Meta", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_10), QCoreApplication.translate("MainWindow", u"Romance", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_11), QCoreApplication.translate("MainWindow", u"Adventure", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_12), QCoreApplication.translate("MainWindow", u"Action", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_13), QCoreApplication.translate("MainWindow", u"Slice of Life", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_14), QCoreApplication.translate("MainWindow", u"Comedy/Meme", None))
        self.storeCategoryTab.setTabText(self.storeCategoryTab.indexOf(self.storeCategory_15), QCoreApplication.translate("MainWindow", u"Holiday", None))
        self.storeFetchModListButton.setText(QCoreApplication.translate("MainWindow", u"Fetch Mod List", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.storeTab), QCoreApplication.translate("MainWindow", u"Store", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.statusBar.setText(QCoreApplication.translate("MainWindow", u"Status Bar", None))
    # retranslateUi

