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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(600, 387)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMaximumSize(QSize(600, 400))
        icon = QIcon()
        icon.addFile(u"../2588225-200.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(Widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget_authorization = QTabWidget(Widget)
        self.tabWidget_authorization.setObjectName(u"tabWidget_authorization")
        sizePolicy.setHeightForWidth(self.tabWidget_authorization.sizePolicy().hasHeightForWidth())
        self.tabWidget_authorization.setSizePolicy(sizePolicy)
        self.tabWidget_authorization.setMaximumSize(QSize(600, 400))
        self.tab_authorization = QWidget()
        self.tab_authorization.setObjectName(u"tab_authorization")
        self.gridLayout_2 = QGridLayout(self.tab_authorization)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_authorization_icon = QLabel(self.tab_authorization)
        self.label_authorization_icon.setObjectName(u"label_authorization_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_authorization_icon.sizePolicy().hasHeightForWidth())
        self.label_authorization_icon.setSizePolicy(sizePolicy1)
        self.label_authorization_icon.setPixmap(QPixmap(u"../2588225-200.png"))
        self.label_authorization_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_authorization_icon)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_username_authorization = QLineEdit(self.tab_authorization)
        self.lineEdit_username_authorization.setObjectName(u"lineEdit_username_authorization")
        self.lineEdit_username_authorization.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_username_authorization, 0, 0, 1, 1)

        self.lineEdit_password_authorization = QLineEdit(self.tab_authorization)
        self.lineEdit_password_authorization.setObjectName(u"lineEdit_password_authorization")
        self.lineEdit_password_authorization.setEchoMode(QLineEdit.Password)
        self.lineEdit_password_authorization.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_password_authorization, 1, 0, 1, 1)

        self.pushButton_enter_authorization = QPushButton(self.tab_authorization)
        self.pushButton_enter_authorization.setObjectName(u"pushButton_enter_authorization")

        self.gridLayout_4.addWidget(self.pushButton_enter_authorization, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.label_message_authorization = QLabel(self.tab_authorization)
        self.label_message_authorization.setObjectName(u"label_message_authorization")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_message_authorization.sizePolicy().hasHeightForWidth())
        self.label_message_authorization.setSizePolicy(sizePolicy2)
        self.label_message_authorization.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_message_authorization, 1, 0, 1, 1)

        self.tabWidget_authorization.addTab(self.tab_authorization, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.gridLayout_5 = QGridLayout(self.tab_settings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_port_settings = QLineEdit(self.tab_settings)
        self.lineEdit_port_settings.setObjectName(u"lineEdit_port_settings")
        self.lineEdit_port_settings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_port_settings, 1, 1, 1, 1)

        self.label_host_settings = QLabel(self.tab_settings)
        self.label_host_settings.setObjectName(u"label_host_settings")
        self.label_host_settings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_host_settings, 0, 0, 1, 1)

        self.lineEdit_host_settings = QLineEdit(self.tab_settings)
        self.lineEdit_host_settings.setObjectName(u"lineEdit_host_settings")
        self.lineEdit_host_settings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_host_settings, 0, 1, 1, 1)

        self.label_port_settings = QLabel(self.tab_settings)
        self.label_port_settings.setObjectName(u"label_port_settings")
        self.label_port_settings.setAlignment(Qt.AlignCenter)
        self.label_port_settings.setWordWrap(False)

        self.gridLayout.addWidget(self.label_port_settings, 1, 0, 1, 1)

        self.label_DBname_settings = QLabel(self.tab_settings)
        self.label_DBname_settings.setObjectName(u"label_DBname_settings")
        self.label_DBname_settings.setAlignment(Qt.AlignCenter)
        self.label_DBname_settings.setWordWrap(False)

        self.gridLayout.addWidget(self.label_DBname_settings, 2, 0, 1, 1)

        self.lineEdit_DBname_settings = QLineEdit(self.tab_settings)
        self.lineEdit_DBname_settings.setObjectName(u"lineEdit_DBname_settings")
        self.lineEdit_DBname_settings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_DBname_settings, 2, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget_authorization.addTab(self.tab_settings, "")

        self.gridLayout_3.addWidget(self.tabWidget_authorization, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget_authorization.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.label_authorization_icon.setText("")
        self.lineEdit_username_authorization.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.lineEdit_password_authorization.setInputMask("")
        self.lineEdit_password_authorization.setText("")
        self.lineEdit_password_authorization.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_enter_authorization.setText(QCoreApplication.translate("Widget", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_message_authorization.setText("")
        self.tabWidget_authorization.setTabText(self.tabWidget_authorization.indexOf(self.tab_authorization), QCoreApplication.translate("Widget", u"\u0412\u0445\u043e\u0434", None))
        self.lineEdit_port_settings.setPlaceholderText(QCoreApplication.translate("Widget", u"5432", None))
        self.label_host_settings.setText(QCoreApplication.translate("Widget", u"\u0425\u043e\u0441\u0442:", None))
        self.lineEdit_host_settings.setPlaceholderText(QCoreApplication.translate("Widget", u"127.0.0.1", None))
        self.label_port_settings.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0440\u0442:", None))
        self.label_DBname_settings.setText(QCoreApplication.translate("Widget", u"\u0418\u043c\u044f \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445:", None))
        self.lineEdit_DBname_settings.setPlaceholderText(QCoreApplication.translate("Widget", u"DB name", None))
        self.tabWidget_authorization.setTabText(self.tabWidget_authorization.indexOf(self.tab_settings), QCoreApplication.translate("Widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0432\u0445\u043e\u0434\u0430", None))
    # retranslateUi

