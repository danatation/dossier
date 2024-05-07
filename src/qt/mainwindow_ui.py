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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QWidget)

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
        self.mainTabWidget.setTabPosition(QTabWidget.North)
        self.mainTabWidget.setElideMode(Qt.ElideNone)
        self.mainTabWidget.setUsesScrollButtons(True)
        self.mainTabWidget.setDocumentMode(True)
        self.mainTabWidget.setTabsClosable(False)
        self.mainTabWidget.setMovable(False)
        self.libraryTab = QWidget()
        self.libraryTab.setObjectName(u"libraryTab")
        self.gridLayout_3 = QGridLayout(self.libraryTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.librarySettingsButton = QPushButton(self.libraryTab)
        self.librarySettingsButton.setObjectName(u"librarySettingsButton")
        self.librarySettingsButton.setCheckable(False)
        self.librarySettingsButton.setFlat(True)

        self.gridLayout_3.addWidget(self.librarySettingsButton, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.libraryImportButton = QPushButton(self.libraryTab)
        self.libraryImportButton.setObjectName(u"libraryImportButton")
        self.libraryImportButton.setCheckable(False)
        self.libraryImportButton.setFlat(True)

        self.gridLayout_3.addWidget(self.libraryImportButton, 0, 1, 1, 1)

        self.librarySplitter = QSplitter(self.libraryTab)
        self.librarySplitter.setObjectName(u"librarySplitter")
        self.librarySplitter.setOrientation(Qt.Horizontal)
        self.libraryModScrollArea = QScrollArea(self.librarySplitter)
        self.libraryModScrollArea.setObjectName(u"libraryModScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.libraryModScrollArea.sizePolicy().hasHeightForWidth())
        self.libraryModScrollArea.setSizePolicy(sizePolicy)
        self.libraryModScrollArea.setMinimumSize(QSize(224, 0))
        self.libraryModScrollArea.setSizeIncrement(QSize(0, 0))
        self.libraryModScrollArea.setBaseSize(QSize(0, 0))
        self.libraryModScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.libraryModScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.libraryModScrollArea.setWidgetResizable(True)
        self.libraryModScrollAreaWidgetContents = QWidget()
        self.libraryModScrollAreaWidgetContents.setObjectName(u"libraryModScrollAreaWidgetContents")
        self.libraryModScrollAreaWidgetContents.setGeometry(QRect(0, 0, 222, 519))
        self.gridLayout_4 = QGridLayout(self.libraryModScrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(4, -1, -1, -1)
        self.libraryModScrollArea.setWidget(self.libraryModScrollAreaWidgetContents)
        self.librarySplitter.addWidget(self.libraryModScrollArea)
        self.libraryViewTabWidget = QTabWidget(self.librarySplitter)
        self.libraryViewTabWidget.setObjectName(u"libraryViewTabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.libraryViewTabWidget.sizePolicy().hasHeightForWidth())
        self.libraryViewTabWidget.setSizePolicy(sizePolicy1)
        self.libraryViewTabWidget.setTabPosition(QTabWidget.South)
        self.libraryViewTabWidget.setDocumentMode(True)
        self.libraryModInfoTab = QWidget()
        self.libraryModInfoTab.setObjectName(u"libraryModInfoTab")
        self.libraryModInfoTab.setLayoutDirection(Qt.LeftToRight)
        self.libraryModInfoTab.setAutoFillBackground(False)
        self.gridLayout_6 = QGridLayout(self.libraryModInfoTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.libraryModInfoScrollArea = QScrollArea(self.libraryModInfoTab)
        self.libraryModInfoScrollArea.setObjectName(u"libraryModInfoScrollArea")
        sizePolicy.setHeightForWidth(self.libraryModInfoScrollArea.sizePolicy().hasHeightForWidth())
        self.libraryModInfoScrollArea.setSizePolicy(sizePolicy)
        self.libraryModInfoScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.libraryModInfoScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.libraryModInfoScrollArea.setWidgetResizable(True)
        self.libraryModInfoScrollArea.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.libraryModInfoScrollAreaWidgetContents = QWidget()
        self.libraryModInfoScrollAreaWidgetContents.setObjectName(u"libraryModInfoScrollAreaWidgetContents")
        self.libraryModInfoScrollAreaWidgetContents.setGeometry(QRect(0, 0, 543, 478))
        self.gridLayout_9 = QGridLayout(self.libraryModInfoScrollAreaWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(16, 32, 16, 0)
        self.libraryModInfoName = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoName.setObjectName(u"libraryModInfoName")

        self.gridLayout_9.addWidget(self.libraryModInfoName, 1, 1, 1, 2, Qt.AlignHCenter)

        self.libraryModInfoPlay = QPushButton(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoPlay.setObjectName(u"libraryModInfoPlay")

        self.gridLayout_9.addWidget(self.libraryModInfoPlay, 3, 1, 1, 1, Qt.AlignRight)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_11, 8, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_13, 11, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer1, 0, 0, 1, 4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 2, 3, 1, 1)

        self.libraryModInfoScreenshotsContents = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoScreenshotsContents.setObjectName(u"libraryModInfoScreenshotsContents")
        self.libraryModInfoScreenshotsContents.setFrameShadow(QFrame.Plain)
        self.libraryModInfoScreenshotsContents.setLineWidth(1)
        self.libraryModInfoScreenshotsContents.setTextFormat(Qt.AutoText)
        self.libraryModInfoScreenshotsContents.setScaledContents(False)

        self.gridLayout_9.addWidget(self.libraryModInfoScreenshotsContents, 12, 0, 1, 1)

        self.verticalSpacer4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer4, 10, 0, 1, 1)

        self.libraryModInfoAuthor = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoAuthor.setObjectName(u"libraryModInfoAuthor")

        self.gridLayout_9.addWidget(self.libraryModInfoAuthor, 2, 1, 1, 2, Qt.AlignHCenter)

        self.verticalSpacer5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer5, 13, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_14, 11, 0, 1, 1)

        self.libraryModInfoDescription = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoDescription.setObjectName(u"libraryModInfoDescription")

        self.gridLayout_9.addWidget(self.libraryModInfoDescription, 5, 1, 1, 2, Qt.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.libraryModInfoAdditionalNotes = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoAdditionalNotes.setObjectName(u"libraryModInfoAdditionalNotes")
        self.libraryModInfoAdditionalNotes.setFrameShadow(QFrame.Plain)
        self.libraryModInfoAdditionalNotes.setLineWidth(1)
        self.libraryModInfoAdditionalNotes.setTextFormat(Qt.AutoText)
        self.libraryModInfoAdditionalNotes.setScaledContents(False)

        self.gridLayout_9.addWidget(self.libraryModInfoAdditionalNotes, 8, 1, 1, 2, Qt.AlignHCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.verticalSpacer2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer2, 4, 0, 1, 4)

        self.libraryModInfoDescriptionContents = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoDescriptionContents.setObjectName(u"libraryModInfoDescriptionContents")
        self.libraryModInfoDescriptionContents.setWordWrap(True)

        self.gridLayout_9.addWidget(self.libraryModInfoDescriptionContents, 6, 0, 1, 4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 5, 0, 1, 1)

        self.verticalSpacer3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer3, 7, 0, 1, 1)

        self.libraryModInfoOptions = QPushButton(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoOptions.setObjectName(u"libraryModInfoOptions")
        self.libraryModInfoOptions.setFlat(False)

        self.gridLayout_9.addWidget(self.libraryModInfoOptions, 3, 2, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 5, 3, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 8, 3, 1, 1)

        self.libraryModInfoScreenshots = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoScreenshots.setObjectName(u"libraryModInfoScreenshots")
        self.libraryModInfoScreenshots.setFrameShadow(QFrame.Plain)
        self.libraryModInfoScreenshots.setLineWidth(1)
        self.libraryModInfoScreenshots.setTextFormat(Qt.AutoText)
        self.libraryModInfoScreenshots.setScaledContents(False)

        self.gridLayout_9.addWidget(self.libraryModInfoScreenshots, 11, 1, 1, 2, Qt.AlignHCenter)

        self.libraryModInfoAdditionalNotesContents = QLabel(self.libraryModInfoScrollAreaWidgetContents)
        self.libraryModInfoAdditionalNotesContents.setObjectName(u"libraryModInfoAdditionalNotesContents")
        self.libraryModInfoAdditionalNotesContents.setFrameShadow(QFrame.Plain)
        self.libraryModInfoAdditionalNotesContents.setLineWidth(1)
        self.libraryModInfoAdditionalNotesContents.setTextFormat(Qt.AutoText)
        self.libraryModInfoAdditionalNotesContents.setScaledContents(False)
        self.libraryModInfoAdditionalNotesContents.setWordWrap(True)

        self.gridLayout_9.addWidget(self.libraryModInfoAdditionalNotesContents, 9, 0, 1, 4)

        self.libraryModInfoScrollArea.setWidget(self.libraryModInfoScrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.libraryModInfoScrollArea, 0, 0, 1, 1)

        self.libraryViewTabWidget.addTab(self.libraryModInfoTab, "")
        self.libraryAssetViewerTab = QWidget()
        self.libraryAssetViewerTab.setObjectName(u"libraryAssetViewerTab")
        self.gridLayout = QGridLayout(self.libraryAssetViewerTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.libraryAssetViewScrollArea = QScrollArea(self.libraryAssetViewerTab)
        self.libraryAssetViewScrollArea.setObjectName(u"libraryAssetViewScrollArea")
        self.libraryAssetViewScrollArea.setWidgetResizable(True)
        self.libraryAssetViewScrollAreaWidgetContents = QWidget()
        self.libraryAssetViewScrollAreaWidgetContents.setObjectName(u"libraryAssetViewScrollAreaWidgetContents")
        self.libraryAssetViewScrollAreaWidgetContents.setGeometry(QRect(0, 0, 543, 478))
        self.gridLayout_8 = QGridLayout(self.libraryAssetViewScrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label = QLabel(self.libraryAssetViewScrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.libraryAssetViewScrollArea.setWidget(self.libraryAssetViewScrollAreaWidgetContents)

        self.gridLayout.addWidget(self.libraryAssetViewScrollArea, 0, 0, 1, 1)

        self.libraryViewTabWidget.addTab(self.libraryAssetViewerTab, "")
        self.libraryOptionsTab = QWidget()
        self.libraryOptionsTab.setObjectName(u"libraryOptionsTab")
        self.gridLayout_10 = QGridLayout(self.libraryOptionsTab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.libraryOptionsScrollArea = QScrollArea(self.libraryOptionsTab)
        self.libraryOptionsScrollArea.setObjectName(u"libraryOptionsScrollArea")
        self.libraryOptionsScrollArea.setWidgetResizable(True)
        self.libraryOptionsScrollAreaWidgetContents = QWidget()
        self.libraryOptionsScrollAreaWidgetContents.setObjectName(u"libraryOptionsScrollAreaWidgetContents")
        self.libraryOptionsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 543, 478))
        self.gridLayout_13 = QGridLayout(self.libraryOptionsScrollAreaWidgetContents)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.libraryOptionsScrollArea.setWidget(self.libraryOptionsScrollAreaWidgetContents)

        self.gridLayout_10.addWidget(self.libraryOptionsScrollArea, 0, 0, 1, 1)

        self.libraryViewTabWidget.addTab(self.libraryOptionsTab, "")
        self.librarySplitter.addWidget(self.libraryViewTabWidget)

        self.gridLayout_3.addWidget(self.librarySplitter, 1, 1, 1, 3)

        self.mainTabWidget.addTab(self.libraryTab, "")
        self.storeTab = QWidget()
        self.storeTab.setObjectName(u"storeTab")
        self.gridLayout_5 = QGridLayout(self.storeTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.storeSettingsButton = QPushButton(self.storeTab)
        self.storeSettingsButton.setObjectName(u"storeSettingsButton")
        self.storeSettingsButton.setCheckable(False)
        self.storeSettingsButton.setFlat(True)

        self.gridLayout_5.addWidget(self.storeSettingsButton, 0, 2, 1, 1)

        self.storeCategoryTab = QTabWidget(self.storeTab)
        self.storeCategoryTab.setObjectName(u"storeCategoryTab")
        self.storeCategoryTab.setTabPosition(QTabWidget.South)
        self.storeCategoryTab.setElideMode(Qt.ElideNone)
        self.storeCategory_01 = QWidget()
        self.storeCategory_01.setObjectName(u"storeCategory_01")
        self.gridLayout_7 = QGridLayout(self.storeCategory_01)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.storeCategory_01)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignHCenter)

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
        self.statusBar.setTextFormat(Qt.PlainText)

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
        self.librarySettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.libraryImportButton.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.libraryModInfoName.setText(QCoreApplication.translate("MainWindow", u"Mod Name", None))
        self.libraryModInfoPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.libraryModInfoScreenshotsContents.setText(QCoreApplication.translate("MainWindow", u"Screenshots Text", None))
        self.libraryModInfoAuthor.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.libraryModInfoDescription.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.libraryModInfoAdditionalNotes.setText(QCoreApplication.translate("MainWindow", u"Additional Notes", None))
        self.libraryModInfoDescriptionContents.setText(QCoreApplication.translate("MainWindow", u"Description Text", None))
        self.libraryModInfoOptions.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.libraryModInfoScreenshots.setText(QCoreApplication.translate("MainWindow", u"Screenshots", None))
        self.libraryModInfoAdditionalNotesContents.setText(QCoreApplication.translate("MainWindow", u"Additional Notes Text", None))
        self.libraryViewTabWidget.setTabText(self.libraryViewTabWidget.indexOf(self.libraryModInfoTab), QCoreApplication.translate("MainWindow", u"Mod Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TODO !!!", None))
        self.libraryViewTabWidget.setTabText(self.libraryViewTabWidget.indexOf(self.libraryAssetViewerTab), QCoreApplication.translate("MainWindow", u"Asset Viewer", None))
        self.libraryViewTabWidget.setTabText(self.libraryViewTabWidget.indexOf(self.libraryOptionsTab), QCoreApplication.translate("MainWindow", u"Options", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.libraryTab), QCoreApplication.translate("MainWindow", u"Library", None))
        self.storeSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TODO !!!", None))
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

