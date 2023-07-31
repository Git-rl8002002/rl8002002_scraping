# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import scraping_icon_rc

class Ui_Scraping(object):
    def setupUi(self, Scraping):
        if not Scraping.objectName():
            Scraping.setObjectName(u"Scraping")
        Scraping.resize(926, 617)
        icon = QIcon()
        icon.addFile(u"C:/Users/Jason_Hung/medicine/icon/icons8-load-from-file-48.png", QSize(), QIcon.Normal, QIcon.Off)
        Scraping.setWindowIcon(icon)
        Scraping.setStyleSheet(u"\n"
"#line_notify , #line_notify_goods , #line_notify_ming , #money_record_add_date , #money_record_add_kind , #money_record_add_money , #money_record_add_content , #money_record_set_date , #money_record_set_kind{\n"
"border-radius:10px;\n"
"height:31px;\n"
"}\n"
"\n"
"#btn_duck_film_chart:hover , #btn_et_news_chart:hover , #btn_tech_news_chart:hover , #btn_analysis_total:hover , #btn_udn_news_chart:hover, #btn_et_news_statistics:hover , #btn_tech_news_statistics:hover , #btn_udn_news_statistics:hover , #btn_pc_diy_statistics:hover , #btn_total_statistics:hover , #btn_work_calendar_month_statistics:hover , #btn_work_calendar_year_statistics:hover , #btn_money_record_kind_list:hover , #btn_money_record_detail_list:hover , #btn_money_record_month_list:hover , #btn_money_record_day_list:hover  , #btn_send_line_notify:hover , #btn_send_line_notify_2:hover , #btn_send_line_notify_3:hover , #btn_money_record_submit:hover , #btn_money_record_del:hover , #btn_ddos_analysis_submit:hover , #analysis_ddos_address:hover ,"
                        " #btn_refresh_ddos_statistics:hover , #sell_time:hover , #sell_time_selected:hover , #sell_kind:hover , #sell_kind_selected:hover , #sell_trade_time:hover , #sell_trade_time_selected:hover , #sell_trade_place:hover , #sell_trade_place_selected:hover , #sell_amount:hover , #sell_price:hover , #sell_total_price:hover , #btn_sell_submit:hover , #btn_sell_cancel:hover , #sell_name:hover , #sell_phone:hover , #sell_comment:hover , #btn_sell_alter:hover{\n"
"background-color:gray;\n"
"color:white;\n"
"}\n"
"\n"
"#btn_duck_film_chart , #btn_et_news_chart , #btn_tech_news_chart , #btn_analysis_total , #btn_udn_news_chart , #btn_et_news_statistics , #btn_tech_news_statistics , #btn_udn_news_statistics , #btn_pc_diy_statistics , #btn_total_statistics , #btn_work_calendar_year_statistics , #btn_work_calendar_month_statistics , #btn_money_record_kind_list , #btn_money_record_detail_list , #btn_money_record_month_list , #btn_money_record_day_list , #btn_send_line_notify , #btn_send_line_notify_2 , #btn_send_line_notify_3 ,"
                        " #btn_money_record_submit , #btn_money_record_del , #btn_ddos_analysis_submit , #analysis_ddos_address , #btn_refresh_ddos_statistics , #sell_time , #sell_time_selected , #sell_kind , #sell_kind_selected , #sell_trade_time , #sell_trade_time_selected , #sell_trade_place , #sell_trade_place_selected , #sell_amount , #sell_price , #sell_total_price , #btn_sell_submit , #btn_sell_cancel , #sell_name , #sell_phone , #sell_comment , #btn_sell_alter{\n"
"padding:5px 5px;\n"
"background-color:#cccccc;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.action_film = QAction(Scraping)
        self.action_film.setObjectName(u"action_film")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-video-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_film.setIcon(icon1)
        self.action_news = QAction(Scraping)
        self.action_news.setObjectName(u"action_news")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-news-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_news.setIcon(icon2)
        self.action_log = QAction(Scraping)
        self.action_log.setObjectName(u"action_log")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-write-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_log.setIcon(icon3)
        self.action_work_record = QAction(Scraping)
        self.action_work_record.setObjectName(u"action_work_record")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-write-60 (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_work_record.setIcon(icon4)
        self.action_work_calendar = QAction(Scraping)
        self.action_work_calendar.setObjectName(u"action_work_calendar")
        icon5 = QIcon()
        icon5.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-writing-down-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_work_calendar.setIcon(icon5)
        self.action_money_record = QAction(Scraping)
        self.action_money_record.setObjectName(u"action_money_record")
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-accounts-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_money_record.setIcon(icon6)
        self.action_close = QAction(Scraping)
        self.action_close.setObjectName(u"action_close")
        self.action_close.setCheckable(True)
        icon7 = QIcon()
        icon7.addFile(u"C:/Users/Jason_Hung/medicine/icon/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_close.setIcon(icon7)
        self.action_sell_record = QAction(Scraping)
        self.action_sell_record.setObjectName(u"action_sell_record")
        icon8 = QIcon()
        icon8.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-sell-stock-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_sell_record.setIcon(icon8)
        self.action_line_notify = QAction(Scraping)
        self.action_line_notify.setObjectName(u"action_line_notify")
        icon9 = QIcon()
        icon9.addFile(u"C:/Users/Jason_Hung/medicine/icon/icons8-mail-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_line_notify.setIcon(icon9)
        self.action_DDos = QAction(Scraping)
        self.action_DDos.setObjectName(u"action_DDos")
        icon10 = QIcon()
        icon10.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-load-balancer-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_DDos.setIcon(icon10)
        self.action_stocks = QAction(Scraping)
        self.action_stocks.setObjectName(u"action_stocks")
        icon11 = QIcon()
        icon11.addFile(u"C:/Users/Jason_Hung/tinfar_test/icon/icons8-accounting-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_stocks.setIcon(icon11)
        self.centralwidget = QWidget(Scraping)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_title = QWidget()
        self.page_title.setObjectName(u"page_title")
        self.verticalLayout_2 = QVBoxLayout(self.page_title)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_title = QLabel(self.page_title)
        self.main_title.setObjectName(u"main_title")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(48)
        self.main_title.setFont(font)
        self.main_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.main_title)

        self.stackedWidget.addWidget(self.page_title)
        self.page_news = QWidget()
        self.page_news.setObjectName(u"page_news")
        self.gridLayout = QGridLayout(self.page_news)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.page_news)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.pc_diy_list = QTreeWidget(self.groupBox_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.pc_diy_list.setHeaderItem(__qtreewidgetitem)
        self.pc_diy_list.setObjectName(u"pc_diy_list")
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei"])
        font1.setPointSize(12)
        self.pc_diy_list.setFont(font1)
        self.pc_diy_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pc_diy_list)


        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.page_news)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.udn_news_list = QTreeWidget(self.groupBox_8)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.udn_news_list.setHeaderItem(__qtreewidgetitem1)
        self.udn_news_list.setObjectName(u"udn_news_list")
        self.udn_news_list.setFont(font1)
        self.udn_news_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.udn_news_list)


        self.gridLayout.addWidget(self.groupBox_8, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_news)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.tech_news_list = QTreeWidget(self.groupBox_2)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.tech_news_list.setHeaderItem(__qtreewidgetitem2)
        self.tech_news_list.setObjectName(u"tech_news_list")
        self.tech_news_list.setFont(font1)
        self.tech_news_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.tech_news_list)


        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.page_news)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.et_news_list = QTreeWidget(self.groupBox)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.et_news_list.setHeaderItem(__qtreewidgetitem3)
        self.et_news_list.setObjectName(u"et_news_list")
        self.et_news_list.setFont(font1)
        self.et_news_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.et_news_list)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.page_news)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(1, 1, 1, 1)
        self.btn_et_news_statistics = QPushButton(self.groupBox_11)
        self.btn_et_news_statistics.setObjectName(u"btn_et_news_statistics")
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei"])
        font2.setPointSize(15)
        self.btn_et_news_statistics.setFont(font2)
        self.btn_et_news_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u"C:/Users/Jason_Hung/.designer/icon/bullet-list2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_et_news_statistics.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.btn_et_news_statistics)

        self.btn_udn_news_statistics = QPushButton(self.groupBox_11)
        self.btn_udn_news_statistics.setObjectName(u"btn_udn_news_statistics")
        self.btn_udn_news_statistics.setFont(font2)
        self.btn_udn_news_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_udn_news_statistics.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.btn_udn_news_statistics)

        self.btn_tech_news_statistics = QPushButton(self.groupBox_11)
        self.btn_tech_news_statistics.setObjectName(u"btn_tech_news_statistics")
        self.btn_tech_news_statistics.setFont(font2)
        self.btn_tech_news_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tech_news_statistics.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.btn_tech_news_statistics)

        self.btn_pc_diy_statistics = QPushButton(self.groupBox_11)
        self.btn_pc_diy_statistics.setObjectName(u"btn_pc_diy_statistics")
        self.btn_pc_diy_statistics.setFont(font2)
        self.btn_pc_diy_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pc_diy_statistics.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.btn_pc_diy_statistics)

        self.btn_total_statistics = QPushButton(self.groupBox_11)
        self.btn_total_statistics.setObjectName(u"btn_total_statistics")
        self.btn_total_statistics.setFont(font2)
        self.btn_total_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_total_statistics.setIcon(icon12)

        self.verticalLayout_13.addWidget(self.btn_total_statistics)


        self.gridLayout.addWidget(self.groupBox_11, 0, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_news)
        self.page_line_notify = QWidget()
        self.page_line_notify.setObjectName(u"page_line_notify")
        self.gridLayout_8 = QGridLayout(self.page_line_notify)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_22 = QGroupBox(self.page_line_notify)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.line_notify_ming_msg = QLabel(self.groupBox_22)
        self.line_notify_ming_msg.setObjectName(u"line_notify_ming_msg")

        self.verticalLayout_26.addWidget(self.line_notify_ming_msg)

        self.line_notify_ming = QLineEdit(self.groupBox_22)
        self.line_notify_ming.setObjectName(u"line_notify_ming")
        self.line_notify_ming.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_26.addWidget(self.line_notify_ming)

        self.btn_send_line_notify_2 = QPushButton(self.groupBox_22)
        self.btn_send_line_notify_2.setObjectName(u"btn_send_line_notify_2")
        self.btn_send_line_notify_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u"C:/Users/Jason_Hung/money_manager/icon/icons8-mail-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_line_notify_2.setIcon(icon13)

        self.verticalLayout_26.addWidget(self.btn_send_line_notify_2)


        self.gridLayout_8.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.groupBox_25 = QGroupBox(self.page_line_notify)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(2, 2, 2, 2)
        self.treeWidget_2 = QTreeWidget(self.groupBox_25)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.treeWidget_2.setHeaderItem(__qtreewidgetitem4)
        self.treeWidget_2.setObjectName(u"treeWidget_2")

        self.verticalLayout_27.addWidget(self.treeWidget_2)


        self.gridLayout_8.addWidget(self.groupBox_25, 1, 1, 1, 1)

        self.groupBox_26 = QGroupBox(self.page_line_notify)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_26)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(2, 2, 2, 2)
        self.treeWidget_3 = QTreeWidget(self.groupBox_26)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, u"1");
        self.treeWidget_3.setHeaderItem(__qtreewidgetitem5)
        self.treeWidget_3.setObjectName(u"treeWidget_3")

        self.verticalLayout_25.addWidget(self.treeWidget_3)


        self.gridLayout_8.addWidget(self.groupBox_26, 2, 1, 1, 1)

        self.groupBox_24 = QGroupBox(self.page_line_notify)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.verticalLayout = QVBoxLayout(self.groupBox_24)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.line_notify_msg = QLabel(self.groupBox_24)
        self.line_notify_msg.setObjectName(u"line_notify_msg")

        self.verticalLayout.addWidget(self.line_notify_msg)

        self.line_notify = QLineEdit(self.groupBox_24)
        self.line_notify.setObjectName(u"line_notify")
        self.line_notify.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.line_notify)

        self.btn_send_line_notify = QPushButton(self.groupBox_24)
        self.btn_send_line_notify.setObjectName(u"btn_send_line_notify")
        self.btn_send_line_notify.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_line_notify.setIcon(icon13)

        self.verticalLayout.addWidget(self.btn_send_line_notify)


        self.gridLayout_8.addWidget(self.groupBox_24, 2, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.page_line_notify)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_23)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.line_notify_goods_msg = QLabel(self.groupBox_23)
        self.line_notify_goods_msg.setObjectName(u"line_notify_goods_msg")

        self.verticalLayout_24.addWidget(self.line_notify_goods_msg)

        self.line_notify_goods = QLineEdit(self.groupBox_23)
        self.line_notify_goods.setObjectName(u"line_notify_goods")
        self.line_notify_goods.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.line_notify_goods)

        self.btn_send_line_notify_3 = QPushButton(self.groupBox_23)
        self.btn_send_line_notify_3.setObjectName(u"btn_send_line_notify_3")
        self.btn_send_line_notify_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_line_notify_3.setIcon(icon13)

        self.verticalLayout_24.addWidget(self.btn_send_line_notify_3)


        self.gridLayout_8.addWidget(self.groupBox_23, 1, 0, 1, 1)

        self.groupBox_27 = QGroupBox(self.page_line_notify)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_27)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(2, 2, 2, 2)
        self.treeWidget = QTreeWidget(self.groupBox_27)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem6)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_28.addWidget(self.treeWidget)


        self.gridLayout_8.addWidget(self.groupBox_27, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_line_notify)
        self.page_sell_record = QWidget()
        self.page_sell_record.setObjectName(u"page_sell_record")
        self.gridLayout_7 = QGridLayout(self.page_sell_record)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_31 = QGroupBox(self.page_sell_record)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sell_time = QLineEdit(self.groupBox_31)
        self.sell_time.setObjectName(u"sell_time")
        self.sell_time.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.sell_time)

        self.sell_time_selected = QDateEdit(self.groupBox_31)
        self.sell_time_selected.setObjectName(u"sell_time_selected")
        self.sell_time_selected.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.sell_time_selected)


        self.verticalLayout_32.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.sell_name = QLineEdit(self.groupBox_31)
        self.sell_name.setObjectName(u"sell_name")
        self.sell_name.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.sell_name)

        self.sell_phone = QLineEdit(self.groupBox_31)
        self.sell_phone.setObjectName(u"sell_phone")
        self.sell_phone.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.sell_phone)


        self.verticalLayout_32.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sell_kind = QLineEdit(self.groupBox_31)
        self.sell_kind.setObjectName(u"sell_kind")
        self.sell_kind.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.sell_kind)

        self.sell_kind_selected = QComboBox(self.groupBox_31)
        self.sell_kind_selected.setObjectName(u"sell_kind_selected")
        self.sell_kind_selected.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.sell_kind_selected)


        self.verticalLayout_32.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sell_amount = QLineEdit(self.groupBox_31)
        self.sell_amount.setObjectName(u"sell_amount")
        self.sell_amount.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.sell_amount)

        self.label_5 = QLabel(self.groupBox_31)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.sell_price = QLineEdit(self.groupBox_31)
        self.sell_price.setObjectName(u"sell_price")
        self.sell_price.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.sell_price)

        self.label_4 = QLabel(self.groupBox_31)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.sell_total_price = QLineEdit(self.groupBox_31)
        self.sell_total_price.setObjectName(u"sell_total_price")
        self.sell_total_price.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_12.addWidget(self.sell_total_price)

        self.label_3 = QLabel(self.groupBox_31)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_12.addWidget(self.label_3)


        self.verticalLayout_32.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sell_trade_time = QLineEdit(self.groupBox_31)
        self.sell_trade_time.setObjectName(u"sell_trade_time")
        self.sell_trade_time.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.sell_trade_time)

        self.sell_trade_time_selected = QDateTimeEdit(self.groupBox_31)
        self.sell_trade_time_selected.setObjectName(u"sell_trade_time_selected")
        self.sell_trade_time_selected.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.sell_trade_time_selected)


        self.verticalLayout_32.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.sell_trade_place = QLineEdit(self.groupBox_31)
        self.sell_trade_place.setObjectName(u"sell_trade_place")

        self.horizontalLayout_11.addWidget(self.sell_trade_place)

        self.sell_trade_place_selected = QComboBox(self.groupBox_31)
        self.sell_trade_place_selected.setObjectName(u"sell_trade_place_selected")
        self.sell_trade_place_selected.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.sell_trade_place_selected)


        self.verticalLayout_32.addLayout(self.horizontalLayout_11)

        self.sell_comment = QTextEdit(self.groupBox_31)
        self.sell_comment.setObjectName(u"sell_comment")
        self.sell_comment.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_32.addWidget(self.sell_comment)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_sell_submit = QPushButton(self.groupBox_31)
        self.btn_sell_submit.setObjectName(u"btn_sell_submit")
        self.btn_sell_submit.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-edit-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sell_submit.setIcon(icon14)

        self.horizontalLayout_13.addWidget(self.btn_sell_submit)

        self.btn_sell_cancel = QPushButton(self.groupBox_31)
        self.btn_sell_cancel.setObjectName(u"btn_sell_cancel")
        self.btn_sell_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-close-window-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sell_cancel.setIcon(icon15)

        self.horizontalLayout_13.addWidget(self.btn_sell_cancel)

        self.btn_sell_alter = QPushButton(self.groupBox_31)
        self.btn_sell_alter.setObjectName(u"btn_sell_alter")
        self.btn_sell_alter.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-signing-a-document-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sell_alter.setIcon(icon16)

        self.horizontalLayout_13.addWidget(self.btn_sell_alter)


        self.verticalLayout_32.addLayout(self.horizontalLayout_13)


        self.gridLayout_7.addWidget(self.groupBox_31, 1, 0, 2, 1)

        self.groupBox_20 = QGroupBox(self.page_sell_record)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.sell_record_mother_kind_list = QTreeWidget(self.groupBox_20)
        __qtreewidgetitem7 = QTreeWidgetItem()
        __qtreewidgetitem7.setText(0, u"1");
        self.sell_record_mother_kind_list.setHeaderItem(__qtreewidgetitem7)
        self.sell_record_mother_kind_list.setObjectName(u"sell_record_mother_kind_list")
        self.sell_record_mother_kind_list.setFont(font1)

        self.verticalLayout_21.addWidget(self.sell_record_mother_kind_list)


        self.gridLayout_7.addWidget(self.groupBox_20, 2, 1, 1, 1)

        self.groupBox_19 = QGroupBox(self.page_sell_record)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_19)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(1, 1, 1, 1)
        self.sell_record_mother_year_list = QTreeWidget(self.groupBox_19)
        self.sell_record_mother_year_list.setObjectName(u"sell_record_mother_year_list")
        self.sell_record_mother_year_list.setFont(font1)

        self.verticalLayout_22.addWidget(self.sell_record_mother_year_list)


        self.gridLayout_7.addWidget(self.groupBox_19, 0, 1, 1, 1)

        self.groupBox_18 = QGroupBox(self.page_sell_record)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(1, 1, 1, 1)
        self.sell_record_mother_list = QTreeWidget(self.groupBox_18)
        __qtreewidgetitem8 = QTreeWidgetItem()
        __qtreewidgetitem8.setText(0, u"1");
        self.sell_record_mother_list.setHeaderItem(__qtreewidgetitem8)
        self.sell_record_mother_list.setObjectName(u"sell_record_mother_list")
        self.sell_record_mother_list.setFont(font1)

        self.verticalLayout_20.addWidget(self.sell_record_mother_list)


        self.gridLayout_7.addWidget(self.groupBox_18, 0, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.page_sell_record)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.sell_record_mother_month_list = QTreeWidget(self.groupBox_21)
        __qtreewidgetitem9 = QTreeWidgetItem()
        __qtreewidgetitem9.setText(0, u"1");
        self.sell_record_mother_month_list.setHeaderItem(__qtreewidgetitem9)
        self.sell_record_mother_month_list.setObjectName(u"sell_record_mother_month_list")
        self.sell_record_mother_month_list.setFont(font1)

        self.verticalLayout_23.addWidget(self.sell_record_mother_month_list)


        self.gridLayout_7.addWidget(self.groupBox_21, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_sell_record)
        self.page_money_record = QWidget()
        self.page_money_record.setObjectName(u"page_money_record")
        self.gridLayout_6 = QGridLayout(self.page_money_record)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_17 = QGroupBox(self.page_money_record)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_17)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.money_record_year_statistics_list = QTreeWidget(self.groupBox_17)
        __qtreewidgetitem10 = QTreeWidgetItem()
        __qtreewidgetitem10.setText(0, u"1");
        self.money_record_year_statistics_list.setHeaderItem(__qtreewidgetitem10)
        self.money_record_year_statistics_list.setObjectName(u"money_record_year_statistics_list")
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font3.setPointSize(9)
        self.money_record_year_statistics_list.setFont(font3)

        self.verticalLayout_18.addWidget(self.money_record_year_statistics_list)

        self.money_record_month_statistics_list = QTreeWidget(self.groupBox_17)
        __qtreewidgetitem11 = QTreeWidgetItem()
        __qtreewidgetitem11.setText(0, u"1");
        self.money_record_month_statistics_list.setHeaderItem(__qtreewidgetitem11)
        self.money_record_month_statistics_list.setObjectName(u"money_record_month_statistics_list")
        self.money_record_month_statistics_list.setFont(font3)

        self.verticalLayout_18.addWidget(self.money_record_month_statistics_list)

        self.money_record_day_statistics_list = QTreeWidget(self.groupBox_17)
        __qtreewidgetitem12 = QTreeWidgetItem()
        __qtreewidgetitem12.setText(0, u"1");
        self.money_record_day_statistics_list.setHeaderItem(__qtreewidgetitem12)
        self.money_record_day_statistics_list.setObjectName(u"money_record_day_statistics_list")
        self.money_record_day_statistics_list.setFont(font3)

        self.verticalLayout_18.addWidget(self.money_record_day_statistics_list)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_money_record_detail_list = QPushButton(self.groupBox_17)
        self.btn_money_record_detail_list.setObjectName(u"btn_money_record_detail_list")
        self.btn_money_record_detail_list.setFont(font3)
        self.btn_money_record_detail_list.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u"C:/Users/Jason_Hung/medicine/icon/bullet-list2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_money_record_detail_list.setIcon(icon17)

        self.horizontalLayout_5.addWidget(self.btn_money_record_detail_list)

        self.btn_money_record_month_list = QPushButton(self.groupBox_17)
        self.btn_money_record_month_list.setObjectName(u"btn_money_record_month_list")
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        self.btn_money_record_month_list.setFont(font4)
        self.btn_money_record_month_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_money_record_month_list.setIcon(icon17)

        self.horizontalLayout_5.addWidget(self.btn_money_record_month_list)

        self.btn_money_record_day_list = QPushButton(self.groupBox_17)
        self.btn_money_record_day_list.setObjectName(u"btn_money_record_day_list")
        self.btn_money_record_day_list.setFont(font4)
        self.btn_money_record_day_list.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_money_record_day_list.setIcon(icon17)

        self.horizontalLayout_5.addWidget(self.btn_money_record_day_list)


        self.verticalLayout_18.addLayout(self.horizontalLayout_5)


        self.gridLayout_6.addWidget(self.groupBox_17, 0, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.page_money_record)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.money_record_list = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem13 = QTreeWidgetItem()
        __qtreewidgetitem13.setText(0, u"1");
        self.money_record_list.setHeaderItem(__qtreewidgetitem13)
        self.money_record_list.setObjectName(u"money_record_list")
        self.money_record_list.setFont(font3)

        self.verticalLayout_19.addWidget(self.money_record_list)

        self.money_record_kind_list = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem14 = QTreeWidgetItem()
        __qtreewidgetitem14.setText(0, u"1");
        self.money_record_kind_list.setHeaderItem(__qtreewidgetitem14)
        self.money_record_kind_list.setObjectName(u"money_record_kind_list")
        self.money_record_kind_list.setFont(font3)

        self.verticalLayout_19.addWidget(self.money_record_kind_list)

        self.money_record_detail_list = QTreeWidget(self.groupBox_16)
        __qtreewidgetitem15 = QTreeWidgetItem()
        __qtreewidgetitem15.setText(0, u"1");
        self.money_record_detail_list.setHeaderItem(__qtreewidgetitem15)
        self.money_record_detail_list.setObjectName(u"money_record_detail_list")
        self.money_record_detail_list.setFont(font3)

        self.verticalLayout_19.addWidget(self.money_record_detail_list)

        self.groupBox_28 = QGroupBox(self.groupBox_16)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_28)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.money_record_add_date = QLineEdit(self.groupBox_28)
        self.money_record_add_date.setObjectName(u"money_record_add_date")
        self.money_record_add_date.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.money_record_add_date)

        self.money_record_set_date = QDateEdit(self.groupBox_28)
        self.money_record_set_date.setObjectName(u"money_record_set_date")
        self.money_record_set_date.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.money_record_set_date)


        self.verticalLayout_29.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.money_record_add_kind = QLineEdit(self.groupBox_28)
        self.money_record_add_kind.setObjectName(u"money_record_add_kind")
        self.money_record_add_kind.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.money_record_add_kind)

        self.money_record_set_kind = QComboBox(self.groupBox_28)
        self.money_record_set_kind.setObjectName(u"money_record_set_kind")

        self.horizontalLayout_4.addWidget(self.money_record_set_kind)


        self.verticalLayout_29.addLayout(self.horizontalLayout_4)

        self.money_record_add_money = QLineEdit(self.groupBox_28)
        self.money_record_add_money.setObjectName(u"money_record_add_money")
        self.money_record_add_money.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.money_record_add_money)

        self.money_record_add_content = QLineEdit(self.groupBox_28)
        self.money_record_add_content.setObjectName(u"money_record_add_content")
        self.money_record_add_content.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.money_record_add_content)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_money_record_submit = QPushButton(self.groupBox_28)
        self.btn_money_record_submit.setObjectName(u"btn_money_record_submit")
        self.btn_money_record_submit.setFont(font4)
        self.btn_money_record_submit.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-new-copy-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_money_record_submit.setIcon(icon18)

        self.horizontalLayout_3.addWidget(self.btn_money_record_submit)

        self.btn_money_record_del = QPushButton(self.groupBox_28)
        self.btn_money_record_del.setObjectName(u"btn_money_record_del")
        self.btn_money_record_del.setFont(font4)
        self.btn_money_record_del.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_money_record_del.setIcon(icon15)

        self.horizontalLayout_3.addWidget(self.btn_money_record_del)


        self.verticalLayout_29.addLayout(self.horizontalLayout_3)


        self.verticalLayout_19.addWidget(self.groupBox_28)


        self.gridLayout_6.addWidget(self.groupBox_16, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_money_record)
        self.page_work_record = QWidget()
        self.page_work_record.setObjectName(u"page_work_record")
        self.gridLayout_5 = QGridLayout(self.page_work_record)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_12 = QGroupBox(self.page_work_record)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.work_record_tb_list = QTreeWidget(self.groupBox_12)
        __qtreewidgetitem16 = QTreeWidgetItem()
        __qtreewidgetitem16.setText(0, u"1");
        self.work_record_tb_list.setHeaderItem(__qtreewidgetitem16)
        self.work_record_tb_list.setObjectName(u"work_record_tb_list")
        self.work_record_tb_list.setFont(font4)

        self.verticalLayout_14.addWidget(self.work_record_tb_list)


        self.gridLayout_5.addWidget(self.groupBox_12, 0, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.page_work_record)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.work_record_kind_list = QTreeWidget(self.groupBox_14)
        __qtreewidgetitem17 = QTreeWidgetItem()
        __qtreewidgetitem17.setText(0, u"1");
        self.work_record_kind_list.setHeaderItem(__qtreewidgetitem17)
        self.work_record_kind_list.setObjectName(u"work_record_kind_list")
        font5 = QFont()
        font5.setFamilies([u"Microsoft JhengHei"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.work_record_kind_list.setFont(font5)

        self.verticalLayout_15.addWidget(self.work_record_kind_list)


        self.gridLayout_5.addWidget(self.groupBox_14, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_work_record)
        self.page_work_calendar = QWidget()
        self.page_work_calendar.setObjectName(u"page_work_calendar")
        self.gridLayout_4 = QGridLayout(self.page_work_calendar)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_13 = QGroupBox(self.page_work_calendar)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.work_calendar_list = QTreeWidget(self.groupBox_13)
        __qtreewidgetitem18 = QTreeWidgetItem()
        __qtreewidgetitem18.setText(0, u"1");
        self.work_calendar_list.setHeaderItem(__qtreewidgetitem18)
        self.work_calendar_list.setObjectName(u"work_calendar_list")
        self.work_calendar_list.setFont(font1)

        self.verticalLayout_16.addWidget(self.work_calendar_list)


        self.gridLayout_4.addWidget(self.groupBox_13, 0, 0, 1, 1)

        self.groupBox_15 = QGroupBox(self.page_work_calendar)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 1, 1, 1)
        self.work_calendar_year_list = QTreeWidget(self.groupBox_15)
        __qtreewidgetitem19 = QTreeWidgetItem()
        __qtreewidgetitem19.setText(0, u"1");
        self.work_calendar_year_list.setHeaderItem(__qtreewidgetitem19)
        self.work_calendar_year_list.setObjectName(u"work_calendar_year_list")
        self.work_calendar_year_list.setFont(font1)

        self.verticalLayout_17.addWidget(self.work_calendar_year_list)

        self.work_calendar_month_list = QTreeWidget(self.groupBox_15)
        __qtreewidgetitem20 = QTreeWidgetItem()
        __qtreewidgetitem20.setText(0, u"1");
        self.work_calendar_month_list.setHeaderItem(__qtreewidgetitem20)
        self.work_calendar_month_list.setObjectName(u"work_calendar_month_list")
        self.work_calendar_month_list.setFont(font1)

        self.verticalLayout_17.addWidget(self.work_calendar_month_list)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_work_calendar_month_statistics = QPushButton(self.groupBox_15)
        self.btn_work_calendar_month_statistics.setObjectName(u"btn_work_calendar_month_statistics")
        font6 = QFont()
        font6.setFamilies([u"Microsoft JhengHei"])
        font6.setPointSize(13)
        self.btn_work_calendar_month_statistics.setFont(font6)
        self.btn_work_calendar_month_statistics.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.btn_work_calendar_month_statistics)

        self.btn_work_calendar_year_statistics = QPushButton(self.groupBox_15)
        self.btn_work_calendar_year_statistics.setObjectName(u"btn_work_calendar_year_statistics")
        self.btn_work_calendar_year_statistics.setFont(font6)
        self.btn_work_calendar_year_statistics.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.btn_work_calendar_year_statistics)


        self.verticalLayout_17.addLayout(self.horizontalLayout_6)


        self.gridLayout_4.addWidget(self.groupBox_15, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_work_calendar)
        self.page_film = QWidget()
        self.page_film.setObjectName(u"page_film")
        self.gridLayout_2 = QGridLayout(self.page_film)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_5 = QGroupBox(self.page_film)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.duck_teleplay_list = QTreeWidget(self.groupBox_5)
        __qtreewidgetitem21 = QTreeWidgetItem()
        __qtreewidgetitem21.setText(0, u"1");
        self.duck_teleplay_list.setHeaderItem(__qtreewidgetitem21)
        self.duck_teleplay_list.setObjectName(u"duck_teleplay_list")
        self.duck_teleplay_list.setFont(font1)

        self.verticalLayout_7.addWidget(self.duck_teleplay_list)


        self.gridLayout_2.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_film)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.duck_film_list = QTreeWidget(self.groupBox_4)
        __qtreewidgetitem22 = QTreeWidgetItem()
        __qtreewidgetitem22.setText(0, u"1");
        self.duck_film_list.setHeaderItem(__qtreewidgetitem22)
        self.duck_film_list.setObjectName(u"duck_film_list")
        self.duck_film_list.setFont(font1)

        self.verticalLayout_6.addWidget(self.duck_film_list)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.page_film)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.duck_comic_list = QTreeWidget(self.groupBox_9)
        __qtreewidgetitem23 = QTreeWidgetItem()
        __qtreewidgetitem23.setText(0, u"1");
        self.duck_comic_list.setHeaderItem(__qtreewidgetitem23)
        self.duck_comic_list.setObjectName(u"duck_comic_list")
        self.duck_comic_list.setFont(font1)

        self.verticalLayout_12.addWidget(self.duck_comic_list)


        self.gridLayout_2.addWidget(self.groupBox_9, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.page_film)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.listWidget = QListWidget(self.groupBox_10)
        self.listWidget.setObjectName(u"listWidget")
        font7 = QFont()
        font7.setPointSize(12)
        self.listWidget.setFont(font7)

        self.verticalLayout_11.addWidget(self.listWidget)


        self.gridLayout_2.addWidget(self.groupBox_10, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_film)
        self.page_log = QWidget()
        self.page_log.setObjectName(u"page_log")
        self.gridLayout_3 = QGridLayout(self.page_log)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_6 = QGroupBox(self.page_log)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.scraping_record_list = QTreeWidget(self.groupBox_6)
        __qtreewidgetitem24 = QTreeWidgetItem()
        __qtreewidgetitem24.setText(0, u"1");
        self.scraping_record_list.setHeaderItem(__qtreewidgetitem24)
        self.scraping_record_list.setObjectName(u"scraping_record_list")
        self.scraping_record_list.setFont(font3)

        self.verticalLayout_8.addWidget(self.scraping_record_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_et_news_chart = QPushButton(self.groupBox_6)
        self.btn_et_news_chart.setObjectName(u"btn_et_news_chart")
        self.btn_et_news_chart.setFont(font3)
        self.btn_et_news_chart.setIcon(icon17)

        self.horizontalLayout.addWidget(self.btn_et_news_chart)

        self.btn_tech_news_chart = QPushButton(self.groupBox_6)
        self.btn_tech_news_chart.setObjectName(u"btn_tech_news_chart")
        self.btn_tech_news_chart.setFont(font3)
        self.btn_tech_news_chart.setIcon(icon17)

        self.horizontalLayout.addWidget(self.btn_tech_news_chart)

        self.btn_udn_news_chart = QPushButton(self.groupBox_6)
        self.btn_udn_news_chart.setObjectName(u"btn_udn_news_chart")
        self.btn_udn_news_chart.setFont(font3)
        self.btn_udn_news_chart.setIcon(icon17)

        self.horizontalLayout.addWidget(self.btn_udn_news_chart)

        self.btn_duck_film_chart = QPushButton(self.groupBox_6)
        self.btn_duck_film_chart.setObjectName(u"btn_duck_film_chart")
        self.btn_duck_film_chart.setFont(font3)
        self.btn_duck_film_chart.setIcon(icon17)

        self.horizontalLayout.addWidget(self.btn_duck_film_chart)


        self.verticalLayout_8.addLayout(self.horizontalLayout)


        self.gridLayout_3.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_log)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.scraping_analysis_list = QTreeWidget(self.groupBox_7)
        __qtreewidgetitem25 = QTreeWidgetItem()
        __qtreewidgetitem25.setText(0, u"1");
        self.scraping_analysis_list.setHeaderItem(__qtreewidgetitem25)
        self.scraping_analysis_list.setObjectName(u"scraping_analysis_list")
        self.scraping_analysis_list.setFont(font3)

        self.verticalLayout_9.addWidget(self.scraping_analysis_list)

        self.btn_analysis_total = QPushButton(self.groupBox_7)
        self.btn_analysis_total.setObjectName(u"btn_analysis_total")
        self.btn_analysis_total.setFont(font3)
        self.btn_analysis_total.setIcon(icon17)

        self.verticalLayout_9.addWidget(self.btn_analysis_total)


        self.gridLayout_3.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_log)
        self.page_DDos = QWidget()
        self.page_DDos.setObjectName(u"page_DDos")
        self.gridLayout_10 = QGridLayout(self.page_DDos)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_29 = QGroupBox(self.page_DDos)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_29)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.analysis_ddos_address = QLineEdit(self.groupBox_29)
        self.analysis_ddos_address.setObjectName(u"analysis_ddos_address")
        self.analysis_ddos_address.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.analysis_ddos_address)

        self.btn_ddos_analysis_submit = QPushButton(self.groupBox_29)
        self.btn_ddos_analysis_submit.setObjectName(u"btn_ddos_analysis_submit")
        self.btn_ddos_analysis_submit.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-graph-report-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ddos_analysis_submit.setIcon(icon19)

        self.horizontalLayout_7.addWidget(self.btn_ddos_analysis_submit)


        self.verticalLayout_30.addLayout(self.horizontalLayout_7)

        self.label = QLabel(self.groupBox_29)
        self.label.setObjectName(u"label")

        self.verticalLayout_30.addWidget(self.label)

        self.ddos_attack_ip_list = QTreeWidget(self.groupBox_29)
        __qtreewidgetitem26 = QTreeWidgetItem()
        __qtreewidgetitem26.setText(0, u"1");
        self.ddos_attack_ip_list.setHeaderItem(__qtreewidgetitem26)
        self.ddos_attack_ip_list.setObjectName(u"ddos_attack_ip_list")
        self.ddos_attack_ip_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_30.addWidget(self.ddos_attack_ip_list)


        self.gridLayout_10.addWidget(self.groupBox_29, 0, 0, 1, 1)

        self.groupBox_30 = QGroupBox(self.page_DDos)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_30)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(1, 1, 1, 1)
        self.btn_refresh_ddos_statistics = QPushButton(self.groupBox_30)
        self.btn_refresh_ddos_statistics.setObjectName(u"btn_refresh_ddos_statistics")
        self.btn_refresh_ddos_statistics.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u"C:/Users/Jason_Hung/.designer/icon/icons8-search-64 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh_ddos_statistics.setIcon(icon20)

        self.verticalLayout_31.addWidget(self.btn_refresh_ddos_statistics)

        self.label_2 = QLabel(self.groupBox_30)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_31.addWidget(self.label_2)

        self.ddos_statistics_list = QTreeWidget(self.groupBox_30)
        __qtreewidgetitem27 = QTreeWidgetItem()
        __qtreewidgetitem27.setText(0, u"1");
        self.ddos_statistics_list.setHeaderItem(__qtreewidgetitem27)
        self.ddos_statistics_list.setObjectName(u"ddos_statistics_list")
        self.ddos_statistics_list.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.ddos_statistics_list)


        self.gridLayout_10.addWidget(self.groupBox_30, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_DDos)

        self.gridLayout_9.addWidget(self.stackedWidget, 0, 1, 1, 1)

        Scraping.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Scraping)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_7 = QMenu(self.menubar)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_8 = QMenu(self.menubar)
        self.menu_8.setObjectName(u"menu_8")
        Scraping.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menu.addAction(self.action_news)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menu_2.addAction(self.action_film)
        self.menu_3.addAction(self.action_log)
        self.menu_4.addAction(self.action_work_record)
        self.menu_4.addAction(self.action_work_calendar)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_line_notify)
        self.menu_5.addAction(self.action_money_record)
        self.menu_6.addAction(self.action_sell_record)
        self.menu_7.addAction(self.action_DDos)
        self.menu_8.addAction(self.action_stocks)

        self.retranslateUi(Scraping)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Scraping)
    # setupUi

    def retranslateUi(self, Scraping):
        Scraping.setWindowTitle(QCoreApplication.translate("Scraping", u"Scraping", None))
        self.action_film.setText(QCoreApplication.translate("Scraping", u"\u5c0f\u9d28\u5f71\u97f3", None))
#if QT_CONFIG(tooltip)
        self.action_film.setToolTip(QCoreApplication.translate("Scraping", u"\u5c0f\u9d28\u5f71\u97f3", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_film.setShortcut(QCoreApplication.translate("Scraping", u"Alt+F", None))
#endif // QT_CONFIG(shortcut)
        self.action_news.setText(QCoreApplication.translate("Scraping", u"News", None))
#if QT_CONFIG(shortcut)
        self.action_news.setShortcut(QCoreApplication.translate("Scraping", u"Alt+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_log.setText(QCoreApplication.translate("Scraping", u"\u722c\u87f2\u8a18\u9304", None))
#if QT_CONFIG(tooltip)
        self.action_log.setToolTip(QCoreApplication.translate("Scraping", u"\u722c\u87f2\u8a18\u9304", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_log.setShortcut(QCoreApplication.translate("Scraping", u"Alt+L", None))
#endif // QT_CONFIG(shortcut)
        self.action_work_record.setText(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u8a18\u9304", None))
#if QT_CONFIG(tooltip)
        self.action_work_record.setToolTip(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u8a18\u9304", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_work_record.setShortcut(QCoreApplication.translate("Scraping", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_work_calendar.setText(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u65e5\u8a8c", None))
#if QT_CONFIG(tooltip)
        self.action_work_calendar.setToolTip(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u65e5\u8a8c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_work_calendar.setShortcut(QCoreApplication.translate("Scraping", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_money_record.setText(QCoreApplication.translate("Scraping", u"\u5e33\u52d9\u8a18\u9304", None))
#if QT_CONFIG(tooltip)
        self.action_money_record.setToolTip(QCoreApplication.translate("Scraping", u"\u5e33\u52d9\u8a18\u9304", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_money_record.setShortcut(QCoreApplication.translate("Scraping", u"Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.action_close.setText(QCoreApplication.translate("Scraping", u"\u95dc\u9589", None))
#if QT_CONFIG(tooltip)
        self.action_close.setToolTip(QCoreApplication.translate("Scraping", u"\u95dc\u9589", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_close.setShortcut(QCoreApplication.translate("Scraping", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_sell_record.setText(QCoreApplication.translate("Scraping", u"\u4e8c\u59e8\u679c\u5712", None))
#if QT_CONFIG(tooltip)
        self.action_sell_record.setToolTip(QCoreApplication.translate("Scraping", u"\u4e8c\u59e8\u679c\u5712", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_sell_record.setShortcut(QCoreApplication.translate("Scraping", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_line_notify.setText(QCoreApplication.translate("Scraping", u"Line notify", None))
#if QT_CONFIG(shortcut)
        self.action_line_notify.setShortcut(QCoreApplication.translate("Scraping", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_DDos.setText(QCoreApplication.translate("Scraping", u"DDos", None))
        self.action_stocks.setText(QCoreApplication.translate("Scraping", u"\u80a1\u7968", None))
#if QT_CONFIG(tooltip)
        self.action_stocks.setToolTip(QCoreApplication.translate("Scraping", u"\u80a1\u7968", None))
#endif // QT_CONFIG(tooltip)
        self.main_title.setText(QCoreApplication.translate("Scraping", u"Scraping Manager", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Scraping", u"PC DIY", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Scraping", u"UDN news", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Scraping", u"Tech News", None))
        self.groupBox.setTitle(QCoreApplication.translate("Scraping", u"ET News", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Scraping", u"Charts", None))
        self.btn_et_news_statistics.setText(QCoreApplication.translate("Scraping", u"ET news statistics", None))
        self.btn_udn_news_statistics.setText(QCoreApplication.translate("Scraping", u"UDN news statistics", None))
        self.btn_tech_news_statistics.setText(QCoreApplication.translate("Scraping", u"TECH news statistics", None))
        self.btn_pc_diy_statistics.setText(QCoreApplication.translate("Scraping", u" PC DIY statistics", None))
        self.btn_total_statistics.setText(QCoreApplication.translate("Scraping", u"News total statistics", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("Scraping", u"\u963f\u660e\u4e00\u5bb6", None))
        self.line_notify_ming_msg.setText(QCoreApplication.translate("Scraping", u"TextLabel", None))
        self.line_notify_ming.setPlaceholderText(QCoreApplication.translate("Scraping", u"msg", None))
        self.btn_send_line_notify_2.setText(QCoreApplication.translate("Scraping", u"Send", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("Scraping", u"\u597d\u5eb7\u5831\u5831 \u8a18\u9304\u6e05\u55ae", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("Scraping", u"1\u5c0d1 \u8a18\u9304\u6e05\u55ae", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("Scraping", u"1 \u5c0d 1", None))
        self.line_notify_msg.setText(QCoreApplication.translate("Scraping", u"TextLabel", None))
        self.line_notify.setPlaceholderText(QCoreApplication.translate("Scraping", u"msg", None))
        self.btn_send_line_notify.setText(QCoreApplication.translate("Scraping", u"Send", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Scraping", u"\u597d\u5eb7\u5831\u5831", None))
        self.line_notify_goods_msg.setText(QCoreApplication.translate("Scraping", u"TextLabel", None))
        self.line_notify_goods.setPlaceholderText(QCoreApplication.translate("Scraping", u"msg", None))
        self.btn_send_line_notify_3.setText(QCoreApplication.translate("Scraping", u"Send", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("Scraping", u"\u963f\u660e\u4e00\u5bb6 \u8a18\u9304\u6e05\u55ae", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("Scraping", u"\u65b0\u589e\u7db2\u62cd\u8a18\u9304", None))
        self.sell_time.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u65e5\u671f", None))
        self.sell_name.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u59d3\u540d", None))
        self.sell_phone.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u624b\u6a5f", None))
        self.sell_kind.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u7a2e\u985e", None))
        self.sell_amount.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u6578\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("Scraping", u"\u65a4 / \u9846", None))
        self.sell_price.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u55ae\u50f9", None))
        self.label_4.setText(QCoreApplication.translate("Scraping", u"\u5143", None))
        self.sell_total_price.setText("")
        self.sell_total_price.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u8a02\u8cfc\u7e3d\u50f9", None))
        self.label_3.setText(QCoreApplication.translate("Scraping", u"\u5143", None))
        self.sell_trade_time.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u9762\u4ea4\u65e5\u671f", None))
        self.sell_trade_place.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u9762\u4ea4\u5730\u9ede", None))
        self.sell_comment.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u5099\u8a3b", None))
        self.btn_sell_submit.setText(QCoreApplication.translate("Scraping", u"\u65b0\u589e", None))
        self.btn_sell_cancel.setText(QCoreApplication.translate("Scraping", u"\u53d6\u6d88", None))
        self.btn_sell_alter.setText(QCoreApplication.translate("Scraping", u"\u4fee\u6539", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Scraping", u"\u7db2\u62cd \u6e05\u55ae \u7d71\u8a08", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Scraping", u"\u7db2\u62cd \u5e74 \u7d71\u8a08", None))
        ___qtreewidgetitem = self.sell_record_mother_year_list.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Scraping", u"1", None));
        self.groupBox_18.setTitle(QCoreApplication.translate("Scraping", u"\u7db2\u62cd\u6e05\u55ae - \u4e8c\u59e8\u679c\u5712", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Scraping", u"\u7db2\u62cd \u6708 \u7d71\u8a08", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Scraping", u"\u5e33\u52d9 \u5e74 / \u6708 / \u65e5 \u7d71\u8a08", None))
        self.btn_money_record_detail_list.setText(QCoreApplication.translate("Scraping", u"\u5e74 \u7d71\u8a08", None))
        self.btn_money_record_month_list.setText(QCoreApplication.translate("Scraping", u"\u6708 \u7d71\u8a08", None))
        self.btn_money_record_day_list.setText(QCoreApplication.translate("Scraping", u"\u65e5 \u7d71\u8a08", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Scraping", u"\u5e33\u52d9\u6e05\u55ae", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("Scraping", u"\u65b0\u589e\u5e33\u52d9\u8a18\u9304", None))
        self.money_record_add_date.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u65e5\u671f", None))
        self.money_record_add_kind.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u7a2e\u985e", None))
        self.money_record_add_money.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u91d1\u984d", None))
        self.money_record_add_content.setPlaceholderText(QCoreApplication.translate("Scraping", u"\u5167\u5bb9", None))
        self.btn_money_record_submit.setText(QCoreApplication.translate("Scraping", u"\u65b0\u589e", None))
        self.btn_money_record_del.setText(QCoreApplication.translate("Scraping", u"\u522a\u9664", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u8a18\u9304", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u8a18\u9304 - \u7a2e\u985e\u7d71\u8a08", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u65e5\u8a8c", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c\u65e5\u8a8c \u5e74 , \u6708 \u7d71\u8a08", None))
        self.btn_work_calendar_month_statistics.setText(QCoreApplication.translate("Scraping", u"\u6708 \u7d71\u8a08", None))
        self.btn_work_calendar_year_statistics.setText(QCoreApplication.translate("Scraping", u"\u5e74 \u7d71\u8a08", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Scraping", u"\u5c0f\u9d28\u5f71\u97f3 - \u96fb\u8996\u5287", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Scraping", u"\u5c0f\u9d28\u5f71\u97f3", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Scraping", u"\u5c0f\u9d28\u5f71\u97f3 - \u52d5\u6f2b", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Scraping", u"\u5c0f\u9d28\u5f71\u97f3 - \u6210\u4eba", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Scraping", u"\u722c\u87f2\u8a18\u9304", None))
        self.btn_et_news_chart.setText(QCoreApplication.translate("Scraping", u"ET news", None))
        self.btn_tech_news_chart.setText(QCoreApplication.translate("Scraping", u"TECH news", None))
        self.btn_udn_news_chart.setText(QCoreApplication.translate("Scraping", u"UDN news", None))
        self.btn_duck_film_chart.setText(QCoreApplication.translate("Scraping", u"Duck Film", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Scraping", u"\u722c\u87f2\u5206\u6790", None))
        self.btn_analysis_total.setText(QCoreApplication.translate("Scraping", u"analysis total", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("Scraping", u"DDos \u89e3\u6790", None))
        self.analysis_ddos_address.setText("")
        self.btn_ddos_analysis_submit.setText(QCoreApplication.translate("Scraping", u"\u89e3\u6790", None))
        self.label.setText(QCoreApplication.translate("Scraping", u"DDos attack IP analysis list", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("Scraping", u"DDos \u7d71\u8a08", None))
        self.btn_refresh_ddos_statistics.setText(QCoreApplication.translate("Scraping", u"Refresh", None))
        self.label_2.setText(QCoreApplication.translate("Scraping", u"DDos statistics list", None))
        self.menu.setTitle(QCoreApplication.translate("Scraping", u"\u65b0\u805e", None))
        self.menu_2.setTitle(QCoreApplication.translate("Scraping", u"\u96fb\u5f71", None))
        self.menu_3.setTitle(QCoreApplication.translate("Scraping", u"\u65e5\u8a8c", None))
        self.menu_4.setTitle(QCoreApplication.translate("Scraping", u"\u5de5\u4f5c ", None))
        self.menu_5.setTitle(QCoreApplication.translate("Scraping", u"\u5e33\u52d9", None))
        self.menu_6.setTitle(QCoreApplication.translate("Scraping", u"\u7db2\u62cd", None))
        self.menu_7.setTitle(QCoreApplication.translate("Scraping", u"\u7db2\u8def\u8cc7\u5b89", None))
        self.menu_8.setTitle(QCoreApplication.translate("Scraping", u"\u6295\u8cc7\u7406\u8ca1", None))
    # retranslateUi

