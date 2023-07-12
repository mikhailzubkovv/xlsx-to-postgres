# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 638)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(100, 100))
        icon = QIcon()
        icon.addFile(u"../1993279ba43da14bed43e0a4bde6c8ed.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(100, 100))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(100, 100))
        self.tabWidget.setDocumentMode(False)
        self.list_staff_pass = QWidget()
        self.list_staff_pass.setObjectName(u"list_staff_pass")
        self.list_staff_pass.setMinimumSize(QSize(100, 0))
        self.list_staff_pass.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.list_staff_pass)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_photo_from_db_list_staff_pass = QLabel(self.list_staff_pass)
        self.label_photo_from_db_list_staff_pass.setObjectName(u"label_photo_from_db_list_staff_pass")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_photo_from_db_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.label_photo_from_db_list_staff_pass.setSizePolicy(sizePolicy1)
        self.label_photo_from_db_list_staff_pass.setFrameShape(QFrame.NoFrame)
        self.label_photo_from_db_list_staff_pass.setPixmap(QPixmap(u"../id-photo-design-illustration-isolated-on-white-background-free-vector.png"))
        self.label_photo_from_db_list_staff_pass.setScaledContents(False)
        self.label_photo_from_db_list_staff_pass.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_photo_from_db_list_staff_pass)

        self.button_path_update_photo_list_staff_pass = QPushButton(self.list_staff_pass)
        self.button_path_update_photo_list_staff_pass.setObjectName(u"button_path_update_photo_list_staff_pass")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_path_update_photo_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.button_path_update_photo_list_staff_pass.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.button_path_update_photo_list_staff_pass)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 4, 0, 1, 1)

        self.tableWidget_list_staff_pass = QTableWidget(self.list_staff_pass)
        if (self.tableWidget_list_staff_pass.columnCount() < 12):
            self.tableWidget_list_staff_pass.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"1. ID");
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_list_staff_pass.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget_list_staff_pass.setObjectName(u"tableWidget_list_staff_pass")
        self.tableWidget_list_staff_pass.setMinimumSize(QSize(100, 100))
        self.tableWidget_list_staff_pass.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_list_staff_pass.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_list_staff_pass.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_list_staff_pass.setDragEnabled(True)
        self.tableWidget_list_staff_pass.setDragDropMode(QAbstractItemView.DropOnly)
        self.tableWidget_list_staff_pass.setAlternatingRowColors(False)
        self.tableWidget_list_staff_pass.setGridStyle(Qt.SolidLine)
        self.tableWidget_list_staff_pass.setSortingEnabled(False)
        self.tableWidget_list_staff_pass.setWordWrap(True)
        self.tableWidget_list_staff_pass.setColumnCount(12)
        self.tableWidget_list_staff_pass.horizontalHeader().setVisible(True)
        self.tableWidget_list_staff_pass.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_list_staff_pass.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_list_staff_pass.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_list_staff_pass.horizontalHeader().setHighlightSections(True)
        self.tableWidget_list_staff_pass.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_list_staff_pass.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_list_staff_pass.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_list_staff_pass.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_list_staff_pass.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_list_staff_pass.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_list_staff_pass.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tableWidget_list_staff_pass, 2, 3, 4, 2)

        self.show_db_bt_list_staff_pass = QPushButton(self.list_staff_pass)
        self.show_db_bt_list_staff_pass.setObjectName(u"show_db_bt_list_staff_pass")

        self.gridLayout_4.addWidget(self.show_db_bt_list_staff_pass, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.lineEdit_searcher_list_staff_pass = QLineEdit(self.list_staff_pass)
        self.lineEdit_searcher_list_staff_pass.setObjectName(u"lineEdit_searcher_list_staff_pass")
        self.lineEdit_searcher_list_staff_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.lineEdit_searcher_list_staff_pass, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_18, 0, 3, 1, 2)

        self.tabwidget_operate_list_staff_pass = QTabWidget(self.list_staff_pass)
        self.tabwidget_operate_list_staff_pass.setObjectName(u"tabwidget_operate_list_staff_pass")
        sizePolicy2.setHeightForWidth(self.tabwidget_operate_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.tabwidget_operate_list_staff_pass.setSizePolicy(sizePolicy2)
        self.tab_download_to_db_list_staff_pass = QWidget()
        self.tab_download_to_db_list_staff_pass.setObjectName(u"tab_download_to_db_list_staff_pass")
        self.gridLayout_3 = QGridLayout(self.tab_download_to_db_list_staff_pass)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pass_number_list_staff_pass = QLineEdit(self.tab_download_to_db_list_staff_pass)
        self.pass_number_list_staff_pass.setObjectName(u"pass_number_list_staff_pass")
        sizePolicy2.setHeightForWidth(self.pass_number_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.pass_number_list_staff_pass.setSizePolicy(sizePolicy2)
        self.pass_number_list_staff_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pass_number_list_staff_pass, 2, 0, 1, 1)

        self.label_download_to_db_list_staff_pass = QLabel(self.tab_download_to_db_list_staff_pass)
        self.label_download_to_db_list_staff_pass.setObjectName(u"label_download_to_db_list_staff_pass")
        sizePolicy2.setHeightForWidth(self.label_download_to_db_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.label_download_to_db_list_staff_pass.setSizePolicy(sizePolicy2)
        self.label_download_to_db_list_staff_pass.setFrameShape(QFrame.NoFrame)
        self.label_download_to_db_list_staff_pass.setAlignment(Qt.AlignCenter)
        self.label_download_to_db_list_staff_pass.setWordWrap(True)

        self.gridLayout.addWidget(self.label_download_to_db_list_staff_pass, 0, 0, 1, 1)

        self.add_to_db_list_staff_pass = QPushButton(self.tab_download_to_db_list_staff_pass)
        self.add_to_db_list_staff_pass.setObjectName(u"add_to_db_list_staff_pass")
        sizePolicy2.setHeightForWidth(self.add_to_db_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.add_to_db_list_staff_pass.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.add_to_db_list_staff_pass, 4, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabwidget_operate_list_staff_pass.addTab(self.tab_download_to_db_list_staff_pass, "")
        self.tab_delete_position_list_staff_pass = QWidget()
        self.tab_delete_position_list_staff_pass.setObjectName(u"tab_delete_position_list_staff_pass")
        self.gridLayout_5 = QGridLayout(self.tab_delete_position_list_staff_pass)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_delete_position_list_staff_pass = QLabel(self.tab_delete_position_list_staff_pass)
        self.label_delete_position_list_staff_pass.setObjectName(u"label_delete_position_list_staff_pass")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_delete_position_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.label_delete_position_list_staff_pass.setSizePolicy(sizePolicy3)
        self.label_delete_position_list_staff_pass.setFrameShape(QFrame.NoFrame)
        self.label_delete_position_list_staff_pass.setTextFormat(Qt.AutoText)
        self.label_delete_position_list_staff_pass.setAlignment(Qt.AlignCenter)
        self.label_delete_position_list_staff_pass.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_delete_position_list_staff_pass, 0, 0, 1, 1)

        self.button_delete_position_list_staff_pass = QPushButton(self.tab_delete_position_list_staff_pass)
        self.button_delete_position_list_staff_pass.setObjectName(u"button_delete_position_list_staff_pass")
        sizePolicy2.setHeightForWidth(self.button_delete_position_list_staff_pass.sizePolicy().hasHeightForWidth())
        self.button_delete_position_list_staff_pass.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.button_delete_position_list_staff_pass, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.tabwidget_operate_list_staff_pass.addTab(self.tab_delete_position_list_staff_pass, "")

        self.gridLayout_4.addWidget(self.tabwidget_operate_list_staff_pass, 2, 0, 1, 1)

        self.tabWidget.addTab(self.list_staff_pass, "")
        self.temporary_staff_pass = QWidget()
        self.temporary_staff_pass.setObjectName(u"temporary_staff_pass")
        self.gridLayout_11 = QGridLayout(self.temporary_staff_pass)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.lineEdit_searcher_temporary_staff_pass = QLineEdit(self.temporary_staff_pass)
        self.lineEdit_searcher_temporary_staff_pass.setObjectName(u"lineEdit_searcher_temporary_staff_pass")
        self.lineEdit_searcher_temporary_staff_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.lineEdit_searcher_temporary_staff_pass, 0, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_19, 0, 1, 1, 1)

        self.button_show_db_temporary_staff_pass = QPushButton(self.temporary_staff_pass)
        self.button_show_db_temporary_staff_pass.setObjectName(u"button_show_db_temporary_staff_pass")

        self.gridLayout_11.addWidget(self.button_show_db_temporary_staff_pass, 0, 0, 1, 1)

        self.tabwidget_operate_temporary_staff_pass = QTabWidget(self.temporary_staff_pass)
        self.tabwidget_operate_temporary_staff_pass.setObjectName(u"tabwidget_operate_temporary_staff_pass")
        sizePolicy2.setHeightForWidth(self.tabwidget_operate_temporary_staff_pass.sizePolicy().hasHeightForWidth())
        self.tabwidget_operate_temporary_staff_pass.setSizePolicy(sizePolicy2)
        self.tab_download_to_db_temporary_staff_pass = QWidget()
        self.tab_download_to_db_temporary_staff_pass.setObjectName(u"tab_download_to_db_temporary_staff_pass")
        self.gridLayout_7 = QGridLayout(self.tab_download_to_db_temporary_staff_pass)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.edit_pass_number_temporary_staff_pass = QLineEdit(self.tab_download_to_db_temporary_staff_pass)
        self.edit_pass_number_temporary_staff_pass.setObjectName(u"edit_pass_number_temporary_staff_pass")
        self.edit_pass_number_temporary_staff_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.edit_pass_number_temporary_staff_pass, 2, 0, 1, 1)

        self.label_download_to_db_temporary_staff_pass = QLabel(self.tab_download_to_db_temporary_staff_pass)
        self.label_download_to_db_temporary_staff_pass.setObjectName(u"label_download_to_db_temporary_staff_pass")
        self.label_download_to_db_temporary_staff_pass.setFrameShape(QFrame.NoFrame)
        self.label_download_to_db_temporary_staff_pass.setAlignment(Qt.AlignCenter)
        self.label_download_to_db_temporary_staff_pass.setWordWrap(False)

        self.gridLayout_8.addWidget(self.label_download_to_db_temporary_staff_pass, 0, 0, 1, 1)

        self.button_add_to_db_temporary_staff_pass = QPushButton(self.tab_download_to_db_temporary_staff_pass)
        self.button_add_to_db_temporary_staff_pass.setObjectName(u"button_add_to_db_temporary_staff_pass")

        self.gridLayout_8.addWidget(self.button_add_to_db_temporary_staff_pass, 4, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.tabwidget_operate_temporary_staff_pass.addTab(self.tab_download_to_db_temporary_staff_pass, "")
        self.tab_delete_position_temporary_staff_pass = QWidget()
        self.tab_delete_position_temporary_staff_pass.setObjectName(u"tab_delete_position_temporary_staff_pass")
        self.gridLayout_9 = QGridLayout(self.tab_delete_position_temporary_staff_pass)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.button_delete_position_temporary_staff_pass = QPushButton(self.tab_delete_position_temporary_staff_pass)
        self.button_delete_position_temporary_staff_pass.setObjectName(u"button_delete_position_temporary_staff_pass")

        self.gridLayout_10.addWidget(self.button_delete_position_temporary_staff_pass, 1, 0, 1, 1)

        self.label_delete_position_temporary_staff_pass = QLabel(self.tab_delete_position_temporary_staff_pass)
        self.label_delete_position_temporary_staff_pass.setObjectName(u"label_delete_position_temporary_staff_pass")
        self.label_delete_position_temporary_staff_pass.setFrameShape(QFrame.NoFrame)
        self.label_delete_position_temporary_staff_pass.setTextFormat(Qt.AutoText)
        self.label_delete_position_temporary_staff_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_delete_position_temporary_staff_pass, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.tabwidget_operate_temporary_staff_pass.addTab(self.tab_delete_position_temporary_staff_pass, "")

        self.gridLayout_11.addWidget(self.tabwidget_operate_temporary_staff_pass, 1, 0, 1, 1)

        self.tableWidget_temporary_staff_pass = QTableWidget(self.temporary_staff_pass)
        if (self.tableWidget_temporary_staff_pass.columnCount() < 17):
            self.tableWidget_temporary_staff_pass.setColumnCount(17)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setText(u"1. ID");
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(11, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(12, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(13, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(14, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(15, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_temporary_staff_pass.setHorizontalHeaderItem(16, __qtablewidgetitem28)
        self.tableWidget_temporary_staff_pass.setObjectName(u"tableWidget_temporary_staff_pass")
        self.tableWidget_temporary_staff_pass.setMinimumSize(QSize(100, 100))
        self.tableWidget_temporary_staff_pass.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_temporary_staff_pass.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_temporary_staff_pass.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_temporary_staff_pass.setDragEnabled(True)
        self.tableWidget_temporary_staff_pass.setDragDropMode(QAbstractItemView.DropOnly)
        self.tableWidget_temporary_staff_pass.setAlternatingRowColors(False)
        self.tableWidget_temporary_staff_pass.setGridStyle(Qt.SolidLine)
        self.tableWidget_temporary_staff_pass.setWordWrap(True)
        self.tableWidget_temporary_staff_pass.setColumnCount(17)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setVisible(True)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setHighlightSections(True)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_temporary_staff_pass.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_temporary_staff_pass.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_temporary_staff_pass.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_temporary_staff_pass.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_temporary_staff_pass.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_temporary_staff_pass.verticalHeader().setStretchLastSection(False)

        self.gridLayout_11.addWidget(self.tableWidget_temporary_staff_pass, 1, 1, 2, 1)

        self.tabWidget.addTab(self.temporary_staff_pass, "")
        self.tab_list_transport_pass = QWidget()
        self.tab_list_transport_pass.setObjectName(u"tab_list_transport_pass")
        self.gridLayout_16 = QGridLayout(self.tab_list_transport_pass)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.button_show_db_list_transport_pass = QPushButton(self.tab_list_transport_pass)
        self.button_show_db_list_transport_pass.setObjectName(u"button_show_db_list_transport_pass")

        self.gridLayout_16.addWidget(self.button_show_db_list_transport_pass, 0, 0, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.lineEdit_searcher_list_transport_pass = QLineEdit(self.tab_list_transport_pass)
        self.lineEdit_searcher_list_transport_pass.setObjectName(u"lineEdit_searcher_list_transport_pass")
        self.lineEdit_searcher_list_transport_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lineEdit_searcher_list_transport_pass, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_20, 0, 1, 1, 1)

        self.tabwidget_operate_list_transport_pass = QTabWidget(self.tab_list_transport_pass)
        self.tabwidget_operate_list_transport_pass.setObjectName(u"tabwidget_operate_list_transport_pass")
        sizePolicy2.setHeightForWidth(self.tabwidget_operate_list_transport_pass.sizePolicy().hasHeightForWidth())
        self.tabwidget_operate_list_transport_pass.setSizePolicy(sizePolicy2)
        self.tab_download_to_db_list_transport_pass = QWidget()
        self.tab_download_to_db_list_transport_pass.setObjectName(u"tab_download_to_db_list_transport_pass")
        self.gridLayout_12 = QGridLayout(self.tab_download_to_db_list_transport_pass)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.edit_pass_number_list_transport_pass = QLineEdit(self.tab_download_to_db_list_transport_pass)
        self.edit_pass_number_list_transport_pass.setObjectName(u"edit_pass_number_list_transport_pass")
        self.edit_pass_number_list_transport_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.edit_pass_number_list_transport_pass, 2, 0, 1, 1)

        self.label_download_to_db_list_transport_pass = QLabel(self.tab_download_to_db_list_transport_pass)
        self.label_download_to_db_list_transport_pass.setObjectName(u"label_download_to_db_list_transport_pass")
        self.label_download_to_db_list_transport_pass.setFrameShape(QFrame.NoFrame)
        self.label_download_to_db_list_transport_pass.setAlignment(Qt.AlignCenter)
        self.label_download_to_db_list_transport_pass.setWordWrap(False)

        self.gridLayout_13.addWidget(self.label_download_to_db_list_transport_pass, 0, 0, 1, 1)

        self.button_add_to_db_list_transport_pass = QPushButton(self.tab_download_to_db_list_transport_pass)
        self.button_add_to_db_list_transport_pass.setObjectName(u"button_add_to_db_list_transport_pass")

        self.gridLayout_13.addWidget(self.button_add_to_db_list_transport_pass, 4, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.tabwidget_operate_list_transport_pass.addTab(self.tab_download_to_db_list_transport_pass, "")
        self.tab_delete_position_list_transport_pass = QWidget()
        self.tab_delete_position_list_transport_pass.setObjectName(u"tab_delete_position_list_transport_pass")
        self.gridLayout_14 = QGridLayout(self.tab_delete_position_list_transport_pass)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.button_delete_position_list_transport_pass = QPushButton(self.tab_delete_position_list_transport_pass)
        self.button_delete_position_list_transport_pass.setObjectName(u"button_delete_position_list_transport_pass")

        self.gridLayout_15.addWidget(self.button_delete_position_list_transport_pass, 1, 0, 1, 1)

        self.label_delete_position_list_transport_pass = QLabel(self.tab_delete_position_list_transport_pass)
        self.label_delete_position_list_transport_pass.setObjectName(u"label_delete_position_list_transport_pass")
        self.label_delete_position_list_transport_pass.setFrameShape(QFrame.NoFrame)
        self.label_delete_position_list_transport_pass.setTextFormat(Qt.AutoText)
        self.label_delete_position_list_transport_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_delete_position_list_transport_pass, 0, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.tabwidget_operate_list_transport_pass.addTab(self.tab_delete_position_list_transport_pass, "")

        self.gridLayout_16.addWidget(self.tabwidget_operate_list_transport_pass, 1, 0, 1, 1)

        self.tableWidget_list_transport_pass = QTableWidget(self.tab_list_transport_pass)
        if (self.tableWidget_list_transport_pass.columnCount() < 13):
            self.tableWidget_list_transport_pass.setColumnCount(13)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setText(u"1. ID");
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font);
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(9, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(10, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(11, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_list_transport_pass.setHorizontalHeaderItem(12, __qtablewidgetitem41)
        self.tableWidget_list_transport_pass.setObjectName(u"tableWidget_list_transport_pass")
        self.tableWidget_list_transport_pass.setMinimumSize(QSize(100, 100))
        self.tableWidget_list_transport_pass.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_list_transport_pass.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_list_transport_pass.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_list_transport_pass.setDragEnabled(True)
        self.tableWidget_list_transport_pass.setDragDropMode(QAbstractItemView.DropOnly)
        self.tableWidget_list_transport_pass.setAlternatingRowColors(False)
        self.tableWidget_list_transport_pass.setGridStyle(Qt.SolidLine)
        self.tableWidget_list_transport_pass.setWordWrap(True)
        self.tableWidget_list_transport_pass.setColumnCount(13)
        self.tableWidget_list_transport_pass.horizontalHeader().setVisible(True)
        self.tableWidget_list_transport_pass.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_list_transport_pass.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_list_transport_pass.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_list_transport_pass.horizontalHeader().setHighlightSections(True)
        self.tableWidget_list_transport_pass.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_list_transport_pass.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_list_transport_pass.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_list_transport_pass.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_list_transport_pass.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_list_transport_pass.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_list_transport_pass.verticalHeader().setStretchLastSection(False)

        self.gridLayout_16.addWidget(self.tableWidget_list_transport_pass, 1, 1, 2, 1)

        self.tabWidget.addTab(self.tab_list_transport_pass, "")
        self.tab_temporary_transport_pass = QWidget()
        self.tab_temporary_transport_pass.setObjectName(u"tab_temporary_transport_pass")
        self.gridLayout_30 = QGridLayout(self.tab_temporary_transport_pass)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.button_show_db_temporary_transport_pass = QPushButton(self.tab_temporary_transport_pass)
        self.button_show_db_temporary_transport_pass.setObjectName(u"button_show_db_temporary_transport_pass")

        self.gridLayout_30.addWidget(self.button_show_db_temporary_transport_pass, 0, 0, 1, 1)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.lineEdit_searcher_temporary_transport_pass = QLineEdit(self.tab_temporary_transport_pass)
        self.lineEdit_searcher_temporary_transport_pass.setObjectName(u"lineEdit_searcher_temporary_transport_pass")
        self.lineEdit_searcher_temporary_transport_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.lineEdit_searcher_temporary_transport_pass, 0, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_26, 0, 1, 1, 1)

        self.tabwidget_operate_temporary_transport_pass = QTabWidget(self.tab_temporary_transport_pass)
        self.tabwidget_operate_temporary_transport_pass.setObjectName(u"tabwidget_operate_temporary_transport_pass")
        sizePolicy2.setHeightForWidth(self.tabwidget_operate_temporary_transport_pass.sizePolicy().hasHeightForWidth())
        self.tabwidget_operate_temporary_transport_pass.setSizePolicy(sizePolicy2)
        self.tab_download_to_db_temporary_transport_pass = QWidget()
        self.tab_download_to_db_temporary_transport_pass.setObjectName(u"tab_download_to_db_temporary_transport_pass")
        self.gridLayout_17 = QGridLayout(self.tab_download_to_db_temporary_transport_pass)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.edit_pass_number_temporary_transport_pass = QLineEdit(self.tab_download_to_db_temporary_transport_pass)
        self.edit_pass_number_temporary_transport_pass.setObjectName(u"edit_pass_number_temporary_transport_pass")
        self.edit_pass_number_temporary_transport_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.edit_pass_number_temporary_transport_pass, 2, 0, 1, 1)

        self.label_download_to_db_temporary_transport_pass = QLabel(self.tab_download_to_db_temporary_transport_pass)
        self.label_download_to_db_temporary_transport_pass.setObjectName(u"label_download_to_db_temporary_transport_pass")
        self.label_download_to_db_temporary_transport_pass.setFrameShape(QFrame.NoFrame)
        self.label_download_to_db_temporary_transport_pass.setAlignment(Qt.AlignCenter)
        self.label_download_to_db_temporary_transport_pass.setWordWrap(False)

        self.gridLayout_21.addWidget(self.label_download_to_db_temporary_transport_pass, 0, 0, 1, 1)

        self.button_add_to_db_temporary_transport_pass = QPushButton(self.tab_download_to_db_temporary_transport_pass)
        self.button_add_to_db_temporary_transport_pass.setObjectName(u"button_add_to_db_temporary_transport_pass")

        self.gridLayout_21.addWidget(self.button_add_to_db_temporary_transport_pass, 4, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_21, 0, 0, 1, 1)

        self.tabwidget_operate_temporary_transport_pass.addTab(self.tab_download_to_db_temporary_transport_pass, "")
        self.tab_delete_position_temporary_transport_pass = QWidget()
        self.tab_delete_position_temporary_transport_pass.setObjectName(u"tab_delete_position_temporary_transport_pass")
        self.gridLayout_22 = QGridLayout(self.tab_delete_position_temporary_transport_pass)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.button_delete_position_temporary_transport_pass = QPushButton(self.tab_delete_position_temporary_transport_pass)
        self.button_delete_position_temporary_transport_pass.setObjectName(u"button_delete_position_temporary_transport_pass")

        self.gridLayout_23.addWidget(self.button_delete_position_temporary_transport_pass, 1, 0, 1, 1)

        self.label_delete_position_temporary_transport_pass = QLabel(self.tab_delete_position_temporary_transport_pass)
        self.label_delete_position_temporary_transport_pass.setObjectName(u"label_delete_position_temporary_transport_pass")
        self.label_delete_position_temporary_transport_pass.setFrameShape(QFrame.NoFrame)
        self.label_delete_position_temporary_transport_pass.setTextFormat(Qt.AutoText)
        self.label_delete_position_temporary_transport_pass.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_delete_position_temporary_transport_pass, 0, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_23, 0, 0, 1, 1)

        self.tabwidget_operate_temporary_transport_pass.addTab(self.tab_delete_position_temporary_transport_pass, "")

        self.gridLayout_30.addWidget(self.tabwidget_operate_temporary_transport_pass, 1, 0, 1, 1)

        self.tableWidget_temporary_transport_pass = QTableWidget(self.tab_temporary_transport_pass)
        if (self.tableWidget_temporary_transport_pass.columnCount() < 13):
            self.tableWidget_temporary_transport_pass.setColumnCount(13)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setText(u"1. ID");
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font);
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(6, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(7, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(8, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(9, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(10, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(11, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_temporary_transport_pass.setHorizontalHeaderItem(12, __qtablewidgetitem54)
        self.tableWidget_temporary_transport_pass.setObjectName(u"tableWidget_temporary_transport_pass")
        self.tableWidget_temporary_transport_pass.setMinimumSize(QSize(100, 100))
        self.tableWidget_temporary_transport_pass.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_temporary_transport_pass.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_temporary_transport_pass.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_temporary_transport_pass.setDragEnabled(True)
        self.tableWidget_temporary_transport_pass.setDragDropMode(QAbstractItemView.DropOnly)
        self.tableWidget_temporary_transport_pass.setAlternatingRowColors(False)
        self.tableWidget_temporary_transport_pass.setGridStyle(Qt.SolidLine)
        self.tableWidget_temporary_transport_pass.setWordWrap(True)
        self.tableWidget_temporary_transport_pass.setColumnCount(13)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setVisible(True)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setHighlightSections(True)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_temporary_transport_pass.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_temporary_transport_pass.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_temporary_transport_pass.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_temporary_transport_pass.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_temporary_transport_pass.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_temporary_transport_pass.verticalHeader().setStretchLastSection(False)

        self.gridLayout_30.addWidget(self.tableWidget_temporary_transport_pass, 1, 1, 2, 1)

        self.tabWidget.addTab(self.tab_temporary_transport_pass, "")
        self.tab_consignment_note = QWidget()
        self.tab_consignment_note.setObjectName(u"tab_consignment_note")
        self.gridLayout_32 = QGridLayout(self.tab_consignment_note)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.tabwidget_operate_consignment_note = QTabWidget(self.tab_consignment_note)
        self.tabwidget_operate_consignment_note.setObjectName(u"tabwidget_operate_consignment_note")
        sizePolicy2.setHeightForWidth(self.tabwidget_operate_consignment_note.sizePolicy().hasHeightForWidth())
        self.tabwidget_operate_consignment_note.setSizePolicy(sizePolicy2)
        self.tab_download_to_db_consignment_note = QWidget()
        self.tab_download_to_db_consignment_note.setObjectName(u"tab_download_to_db_consignment_note")
        self.gridLayout_24 = QGridLayout(self.tab_download_to_db_consignment_note)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.edit_pass_number_consignment_note = QLineEdit(self.tab_download_to_db_consignment_note)
        self.edit_pass_number_consignment_note.setObjectName(u"edit_pass_number_consignment_note")
        self.edit_pass_number_consignment_note.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.edit_pass_number_consignment_note, 2, 0, 1, 1)

        self.label_download_to_db_consignment_note = QLabel(self.tab_download_to_db_consignment_note)
        self.label_download_to_db_consignment_note.setObjectName(u"label_download_to_db_consignment_note")
        self.label_download_to_db_consignment_note.setFrameShape(QFrame.NoFrame)
        self.label_download_to_db_consignment_note.setAlignment(Qt.AlignCenter)
        self.label_download_to_db_consignment_note.setWordWrap(False)

        self.gridLayout_27.addWidget(self.label_download_to_db_consignment_note, 0, 0, 1, 1)

        self.button_add_to_db_consignment_note = QPushButton(self.tab_download_to_db_consignment_note)
        self.button_add_to_db_consignment_note.setObjectName(u"button_add_to_db_consignment_note")

        self.gridLayout_27.addWidget(self.button_add_to_db_consignment_note, 4, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_27, 0, 0, 1, 1)

        self.tabwidget_operate_consignment_note.addTab(self.tab_download_to_db_consignment_note, "")
        self.tab_delete_position_consignment_note = QWidget()
        self.tab_delete_position_consignment_note.setObjectName(u"tab_delete_position_consignment_note")
        self.gridLayout_28 = QGridLayout(self.tab_delete_position_consignment_note)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.button_delete_position_consignment_note = QPushButton(self.tab_delete_position_consignment_note)
        self.button_delete_position_consignment_note.setObjectName(u"button_delete_position_consignment_note")

        self.gridLayout_29.addWidget(self.button_delete_position_consignment_note, 1, 0, 1, 1)

        self.label_delete_position_consignment_note = QLabel(self.tab_delete_position_consignment_note)
        self.label_delete_position_consignment_note.setObjectName(u"label_delete_position_consignment_note")
        self.label_delete_position_consignment_note.setFrameShape(QFrame.NoFrame)
        self.label_delete_position_consignment_note.setTextFormat(Qt.AutoText)
        self.label_delete_position_consignment_note.setAlignment(Qt.AlignCenter)

        self.gridLayout_29.addWidget(self.label_delete_position_consignment_note, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_29, 0, 0, 1, 1)

        self.tabwidget_operate_consignment_note.addTab(self.tab_delete_position_consignment_note, "")

        self.gridLayout_32.addWidget(self.tabwidget_operate_consignment_note, 1, 0, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.lineEdit_searcher_consignment_note = QLineEdit(self.tab_consignment_note)
        self.lineEdit_searcher_consignment_note.setObjectName(u"lineEdit_searcher_consignment_note")
        self.lineEdit_searcher_consignment_note.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.lineEdit_searcher_consignment_note, 0, 0, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_31, 0, 1, 1, 1)

        self.button_show_db_consignment_note = QPushButton(self.tab_consignment_note)
        self.button_show_db_consignment_note.setObjectName(u"button_show_db_consignment_note")

        self.gridLayout_32.addWidget(self.button_show_db_consignment_note, 0, 0, 1, 1)

        self.tableWidget_consignment_note = QTableWidget(self.tab_consignment_note)
        if (self.tableWidget_consignment_note.columnCount() < 10):
            self.tableWidget_consignment_note.setColumnCount(10)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setText(u"1. ID");
        self.tableWidget_consignment_note.setHorizontalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setFont(font);
        self.tableWidget_consignment_note.setHorizontalHeaderItem(1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(6, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(7, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(8, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_consignment_note.setHorizontalHeaderItem(9, __qtablewidgetitem64)
        self.tableWidget_consignment_note.setObjectName(u"tableWidget_consignment_note")
        self.tableWidget_consignment_note.setMinimumSize(QSize(100, 100))
        self.tableWidget_consignment_note.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_consignment_note.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_consignment_note.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_consignment_note.setDragEnabled(True)
        self.tableWidget_consignment_note.setDragDropMode(QAbstractItemView.DropOnly)
        self.tableWidget_consignment_note.setAlternatingRowColors(False)
        self.tableWidget_consignment_note.setGridStyle(Qt.SolidLine)
        self.tableWidget_consignment_note.setWordWrap(True)
        self.tableWidget_consignment_note.setColumnCount(10)
        self.tableWidget_consignment_note.horizontalHeader().setVisible(True)
        self.tableWidget_consignment_note.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_consignment_note.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_consignment_note.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_consignment_note.horizontalHeader().setHighlightSections(True)
        self.tableWidget_consignment_note.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_consignment_note.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_consignment_note.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_consignment_note.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_consignment_note.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget_consignment_note.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_consignment_note.verticalHeader().setStretchLastSection(False)

        self.gridLayout_32.addWidget(self.tableWidget_consignment_note, 1, 1, 2, 1)

        self.tabWidget.addTab(self.tab_consignment_note, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabwidget_operate_list_staff_pass.setCurrentIndex(0)
        self.tabwidget_operate_temporary_staff_pass.setCurrentIndex(0)
        self.tabwidget_operate_list_transport_pass.setCurrentIndex(0)
        self.tabwidget_operate_temporary_transport_pass.setCurrentIndex(0)
        self.tabwidget_operate_consignment_note.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043f\u0443\u0441\u043a\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.label_photo_from_db_list_staff_pass.setText("")
        self.button_path_update_photo_list_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044e", None))
        ___qtablewidgetitem = self.tableWidget_list_staff_pass.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"2. \u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None));
        ___qtablewidgetitem1 = self.tableWidget_list_staff_pass.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"3. \u0424.\u0418.\u041e.", None));
        ___qtablewidgetitem2 = self.tableWidget_list_staff_pass.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"4. \u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem3 = self.tableWidget_list_staff_pass.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"5. \u0421\u0442\u0440\u0430\u043d\u0430 \u043f\u0440\u0435\u0431\u044b\u0432\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.tableWidget_list_staff_pass.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"6. \u041f\u0430\u0441\u043f\u043e\u0440\u0442 (\u0441\u0435\u0440\u0438\u044f, \u043d\u043e\u043c\u0435\u0440)", None));
        ___qtablewidgetitem5 = self.tableWidget_list_staff_pass.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"7.\u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u043e\u0434\u0440\u044f\u0434\u0447\u0438\u043a", None));
        ___qtablewidgetitem6 = self.tableWidget_list_staff_pass.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"8. \u0421\u0443\u0431\u043f\u043e\u0434\u0440\u044f\u0434\u0447\u0438\u043a", None));
        ___qtablewidgetitem7 = self.tableWidget_list_staff_pass.horizontalHeaderItem(8)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"9. \u041c\u0435\u0441\u0442\u043e\u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem8 = self.tableWidget_list_staff_pass.horizontalHeaderItem(9)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"10. \u0414\u0430\u0442\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0441", None));
        ___qtablewidgetitem9 = self.tableWidget_list_staff_pass.horizontalHeaderItem(10)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11. \u0414\u0430\u0442\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0434\u043e", None));
        ___qtablewidgetitem10 = self.tableWidget_list_staff_pass.horizontalHeaderItem(11)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"12. \u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None));
        self.show_db_bt_list_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c DB", None))
        self.lineEdit_searcher_list_staff_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.pass_number_list_staff_pass.setText("")
        self.pass_number_list_staff_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label_download_to_db_list_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 XLSX \u0432 DB", None))
        self.add_to_db_list_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 DB", None))
        self.tabwidget_operate_list_staff_pass.setTabText(self.tabwidget_operate_list_staff_pass.indexOf(self.tab_download_to_db_list_staff_pass), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_delete_position_list_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.button_delete_position_list_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 DB", None))
        self.tabwidget_operate_list_staff_pass.setTabText(self.tabwidget_operate_list_staff_pass.indexOf(self.tab_delete_position_list_staff_pass), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.list_staff_pass), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b \u043f\u043e \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043c", None))
        self.lineEdit_searcher_temporary_staff_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.button_show_db_temporary_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c DB", None))
        self.edit_pass_number_temporary_staff_pass.setText("")
        self.edit_pass_number_temporary_staff_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label_download_to_db_temporary_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 XLSX \u0432 DB", None))
        self.button_add_to_db_temporary_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 DB", None))
        self.tabwidget_operate_temporary_staff_pass.setTabText(self.tabwidget_operate_temporary_staff_pass.indexOf(self.tab_download_to_db_temporary_staff_pass), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.button_delete_position_temporary_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 DB", None))
        self.label_delete_position_temporary_staff_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.tabwidget_operate_temporary_staff_pass.setTabText(self.tabwidget_operate_temporary_staff_pass.indexOf(self.tab_delete_position_temporary_staff_pass), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem11 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2. \u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None));
        ___qtablewidgetitem12 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"3. \u0424.\u0418.\u041e.", None));
        ___qtablewidgetitem13 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"4. \u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem14 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"5. \u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u043e\u0434\u0440\u044f\u0434\u0447\u0438\u043a", None));
        ___qtablewidgetitem15 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"6. \u0421\u0443\u0431\u043f\u043e\u0434\u0440\u044f\u0434\u0447\u0438\u043a", None));
        ___qtablewidgetitem16 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"7. \u041d\u043e\u043c\u0435\u0440 \u0433\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem17 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"8. \u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430 \u0441\u0443\u0431\u043f\u043e\u0434\u0440\u044f\u0434\u0430", None));
        ___qtablewidgetitem18 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"9. \u041c\u0435\u0441\u0442\u043e \u0438 \u0434\u0430\u0442\u0430", None));
        ___qtablewidgetitem19 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"10. \u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem20 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"11. \u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem21 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"12. \u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem22 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(12)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"13. \u0421\u0435\u0440\u0438\u044f, \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None));
        ___qtablewidgetitem23 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(13)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"14. \u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d \u043f\u0430\u0441\u043f\u043e\u0440\u0442", None));
        ___qtablewidgetitem24 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(14)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"15. \u0413\u0440\u0430\u0436\u0434\u0430\u043d\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem25 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(15)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"16. \u0418\u041d\u041d", None));
        ___qtablewidgetitem26 = self.tableWidget_temporary_staff_pass.horizontalHeaderItem(16)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"17. \u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.temporary_staff_pass), QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u043c \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043c", None))
        self.button_show_db_list_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c DB", None))
        self.lineEdit_searcher_list_transport_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.edit_pass_number_list_transport_pass.setText("")
        self.edit_pass_number_list_transport_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label_download_to_db_list_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 XLSX \u0432 DB", None))
        self.button_add_to_db_list_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 DB", None))
        self.tabwidget_operate_list_transport_pass.setTabText(self.tabwidget_operate_list_transport_pass.indexOf(self.tab_download_to_db_list_transport_pass), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.button_delete_position_list_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 DB", None))
        self.label_delete_position_list_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.tabwidget_operate_list_transport_pass.setTabText(self.tabwidget_operate_list_transport_pass.indexOf(self.tab_delete_position_list_transport_pass), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem27 = self.tableWidget_list_transport_pass.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2. \u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None));
        ___qtablewidgetitem28 = self.tableWidget_list_transport_pass.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"3. \u041c\u043e\u0434\u0435\u043b\u044c \u0422\u0421", None));
        ___qtablewidgetitem29 = self.tableWidget_list_transport_pass.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"4. \u0422\u0438\u043f \u0422\u0421", None));
        ___qtablewidgetitem30 = self.tableWidget_list_transport_pass.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"5. \u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0422\u0421", None));
        ___qtablewidgetitem31 = self.tableWidget_list_transport_pass.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"6. \u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442", None));
        ___qtablewidgetitem32 = self.tableWidget_list_transport_pass.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"7. \u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u043e\u0434\u0440\u044f\u0434\u0447\u0438\u043a", None));
        ___qtablewidgetitem33 = self.tableWidget_list_transport_pass.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"8. \u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem34 = self.tableWidget_list_transport_pass.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"9. \u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem35 = self.tableWidget_list_transport_pass.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"10. \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a \u0422\u0421", None));
        ___qtablewidgetitem36 = self.tableWidget_list_transport_pass.horizontalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"11. \u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem37 = self.tableWidget_list_transport_pass.horizontalHeaderItem(11)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"12. \u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem38 = self.tableWidget_list_transport_pass.horizontalHeaderItem(12)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"13. \u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_list_transport_pass), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442 \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0430\u043c", None))
        self.button_show_db_temporary_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c DB", None))
        self.lineEdit_searcher_temporary_transport_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.edit_pass_number_temporary_transport_pass.setText("")
        self.edit_pass_number_temporary_transport_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label_download_to_db_temporary_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 XLSX \u0432 DB", None))
        self.button_add_to_db_temporary_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 DB", None))
        self.tabwidget_operate_temporary_transport_pass.setTabText(self.tabwidget_operate_temporary_transport_pass.indexOf(self.tab_download_to_db_temporary_transport_pass), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.button_delete_position_temporary_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 DB", None))
        self.label_delete_position_temporary_transport_pass.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.tabwidget_operate_temporary_transport_pass.setTabText(self.tabwidget_operate_temporary_transport_pass.indexOf(self.tab_delete_position_temporary_transport_pass), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem39 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"2. \u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None));
        ___qtablewidgetitem40 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"3. \u041c\u043e\u0434\u0435\u043b\u044c \u0422\u0421", None));
        ___qtablewidgetitem41 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"4. \u0422\u0438\u043f \u0422\u0421", None));
        ___qtablewidgetitem42 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"5. \u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u0422\u0421", None));
        ___qtablewidgetitem43 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"6. \u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442", None));
        ___qtablewidgetitem44 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"7. \u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u043e\u0434\u0440\u044f\u0434\u0447\u0438\u043a", None));
        ___qtablewidgetitem45 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"8. \u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem46 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(8)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"9. \u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem47 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(9)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"10. \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a \u0422\u0421", None));
        ___qtablewidgetitem48 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(10)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"11. \u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem49 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(11)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"12. \u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem50 = self.tableWidget_temporary_transport_pass.horizontalHeaderItem(12)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"13. \u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_temporary_transport_pass), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442 \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u043c \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u043c", None))
        self.edit_pass_number_consignment_note.setText("")
        self.edit_pass_number_consignment_note.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.label_download_to_db_consignment_note.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 XLSX \u0432 DB", None))
        self.button_add_to_db_consignment_note.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432 DB", None))
        self.tabwidget_operate_consignment_note.setTabText(self.tabwidget_operate_consignment_note.indexOf(self.tab_download_to_db_consignment_note), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.button_delete_position_consignment_note.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 DB", None))
        self.label_delete_position_consignment_note.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.tabwidget_operate_consignment_note.setTabText(self.tabwidget_operate_consignment_note.indexOf(self.tab_delete_position_consignment_note), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.lineEdit_searcher_consignment_note.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.button_show_db_consignment_note.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c DB", None))
        ___qtablewidgetitem51 = self.tableWidget_consignment_note.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"2. \u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u044f\u0432\u043a\u0438", None));
        ___qtablewidgetitem52 = self.tableWidget_consignment_note.horizontalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"3. \u0413\u0440\u0443\u0437\u043e\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem53 = self.tableWidget_consignment_note.horizontalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"4. \u0413\u0440\u0443\u0437\u043e\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem54 = self.tableWidget_consignment_note.horizontalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"5. \u0424.\u0418.\u041e. \u041c\u041e\u041b", None));
        ___qtablewidgetitem55 = self.tableWidget_consignment_note.horizontalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"6. \u041f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a", None));
        ___qtablewidgetitem56 = self.tableWidget_consignment_note.horizontalHeaderItem(6)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"7. \u041f\u0435\u0440\u0435\u0432\u043e\u0437\u0438\u043c\u044b\u0435 \u0422\u041c\u0426", None));
        ___qtablewidgetitem57 = self.tableWidget_consignment_note.horizontalHeaderItem(7)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"8. \u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem58 = self.tableWidget_consignment_note.horizontalHeaderItem(8)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"9. \u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem59 = self.tableWidget_consignment_note.horizontalHeaderItem(9)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"10. \u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_consignment_note), QCoreApplication.translate("MainWindow", u"\u0422\u0422\u041d", None))
    # retranslateUi

