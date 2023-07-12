# This Python file uses the following encoding: utf-8
import os
import sys
import time
from typing import Callable

import PIL.Image
import psycopg.errors
import sqlalchemy.exc
from PIL.ImageQt import ImageQt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QLineEdit, QTableWidget, QWidget
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from gui.main_window.ui_form import Ui_MainWindow

import models.list_staff_pass
import models.temporary_staff_pass
import models.list_transport_pass
import models.temporary_transport_pass
import models.consignment_note
from models.connect_to_db import connect_db, read_config, change_config
from models.read_xlsx import read_binary_photo, photo_change

# Important:
# You need to run the following command to generate the authorization.py file
#     pyside6-uic form.ui -o authorization.py
from gui.authorization_window.authorization import Ui_Widget


class Authorization(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.lineEdit_username_authorization.setText(read_config()[0])
        self.ui.lineEdit_host_settings.setText(read_config()[2])
        self.ui.lineEdit_port_settings.setText(read_config()[3])
        self.ui.lineEdit_DBname_settings.setText(read_config()[4])
        self.ui.pushButton_enter_authorization.clicked.connect(lambda: self.check_access())

    def check_access(self):
        change_config(
            username=self.ui.lineEdit_username_authorization.text(),
            password=self.ui.lineEdit_password_authorization.text(),
            host=self.ui.lineEdit_host_settings.text(),
            port=self.ui.lineEdit_port_settings.text(),
            database=self.ui.lineEdit_DBname_settings.text()
        )

        try:
            connect_db()
            main_window = MainWindow()
            main_window.show()
            authorization.close()
        except sqlalchemy.exc.OperationalError:
            self.ui.label_message_authorization.setText('Проверьте имя пользователя и пароль / настройки входа')


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.session = connect_db()

        # ------------------------------------------------------------------------------------------------------
        # LIST STAFF PASS
        # button to download XLSX list to Postgres. ListStaffPass
        self.ui.tableWidget_list_staff_pass.resizeColumnsToContents()
        button_add_list_staff_pass = self.ui.add_to_db_list_staff_pass
        button_add_list_staff_pass.clicked.connect(lambda: models.list_staff_pass.add_to_db(
            path=self.open_dialog_box(),
            pass_number=self.ui.pass_number_list_staff_pass.text()))
        button_add_list_staff_pass.clicked.connect(lambda: self.ui.pass_number_list_staff_pass.clear())
        button_add_list_staff_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_list_staff_pass,
            model=models.list_staff_pass.ListStaffPass
        ))

        # button SHOW DB. ListStaffPass
        button_show_list_staff_pass = self.ui.show_db_bt_list_staff_pass
        button_show_list_staff_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_list_staff_pass,
            model=models.list_staff_pass.ListStaffPass
        ))

        # SHOW photo by cell clicked. ListStaffPass
        self.ui.tableWidget_list_staff_pass.cellPressed.connect(lambda: self.read_photo_from_db())

        # update photo in clicked cell. ListStaffPass
        button_update_photo_list_staff_pass = self.ui.button_path_update_photo_list_staff_pass
        button_update_photo_list_staff_pass.clicked.connect(lambda: self.update_photo_in_db())

        # update info in DB. ListStaffPass
        self.ui.tableWidget_list_staff_pass.cellChanged.connect(lambda: self.update_by_change(
            table=self.ui.tableWidget_list_staff_pass,
            model=models.list_staff_pass.ListStaffPass
        ))

        # button to delete position from DB. ListStaffPass
        button_delete_list_staff_pass = self.ui.button_delete_position_list_staff_pass
        button_delete_list_staff_pass.clicked.connect(lambda: self.delete_from_db(
            table=self.ui.tableWidget_list_staff_pass,
            model=models.list_staff_pass.ListStaffPass
        ))

        button_delete_list_staff_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_list_staff_pass,
            model=models.list_staff_pass.ListStaffPass
        ))
        # searcher. ListStaffPass
        self.ui.lineEdit_searcher_list_staff_pass.textEdited.connect(lambda: self.filter_for_table(
            search_text=self.ui.lineEdit_searcher_list_staff_pass,
            table=self.ui.tableWidget_list_staff_pass
        ))

        # ------------------------------------------------------------------------------------------------------
        # TEMPORARY STAFF PASS
        # button to download XLSX list to Postgres. TemporaryStaffPass
        self.ui.tableWidget_temporary_staff_pass.resizeColumnsToContents()
        button_add_temporary_staff_pass = self.ui.button_add_to_db_temporary_staff_pass
        button_add_temporary_staff_pass.clicked.connect(lambda: models.temporary_staff_pass.add_to_db(
            path=self.open_dialog_box(),
            pass_number=self.ui.edit_pass_number_temporary_staff_pass.text()))
        button_add_temporary_staff_pass.clicked.connect(lambda: self.ui.edit_pass_number_temporary_staff_pass.clear())
        button_add_temporary_staff_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_temporary_staff_pass,
            model=models.temporary_staff_pass.TemporaryStaffPass
        ))

        # button SHOW DB. TemporaryStaffPass
        button_show_temporary_staff_pass = self.ui.button_show_db_temporary_staff_pass
        button_show_temporary_staff_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_temporary_staff_pass,
            model=models.temporary_staff_pass.TemporaryStaffPass
        ))

        # update info in DB. TemporaryStaffPass
        self.ui.tableWidget_temporary_staff_pass.cellChanged.connect(lambda: self.update_by_change(
            table=self.ui.tableWidget_temporary_staff_pass,
            model=models.temporary_staff_pass.TemporaryStaffPass
        ))

        # button to delete position from DB. TemporaryStaffPass
        button_delete_temporary_staff_pass = self.ui.button_delete_position_temporary_staff_pass
        button_delete_temporary_staff_pass.clicked.connect(lambda: self.delete_from_db(
            table=self.ui.tableWidget_temporary_staff_pass,
            model=models.temporary_staff_pass.TemporaryStaffPass
        ))

        button_delete_temporary_staff_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_temporary_staff_pass,
            model=models.temporary_staff_pass.TemporaryStaffPass
        ))

        # searcher. TemporaryStaffPass
        self.ui.lineEdit_searcher_temporary_staff_pass.textEdited.connect(lambda: self.filter_for_table(
            search_text=self.ui.lineEdit_searcher_temporary_staff_pass,
            table=self.ui.tableWidget_temporary_staff_pass
        ))

        # ------------------------------------------------------------------------------------------------------
        # LIST TRANSPORT PASS
        # button to download XLSX list to Postgres. ListTransportPass
        self.ui.tableWidget_list_transport_pass.resizeColumnsToContents()
        button_add_list_transport_pass = self.ui.button_add_to_db_list_transport_pass
        button_add_list_transport_pass.clicked.connect(lambda: models.list_transport_pass.add_to_db(
            path=self.open_dialog_box(),
            pass_number=self.ui.edit_pass_number_list_transport_pass.text()))
        button_add_list_transport_pass.clicked.connect(lambda: self.ui.edit_pass_number_list_transport_pass.clear())
        button_add_list_transport_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_list_transport_pass,
            model=models.list_transport_pass.ListTransportPass
        ))

        # button SHOW DB. ListTransportPass
        button_show_list_transport_pass = self.ui.button_show_db_list_transport_pass
        button_show_list_transport_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_list_transport_pass,
            model=models.list_transport_pass.ListTransportPass
        ))

        # update info in DB. ListTransportPass
        self.ui.tableWidget_list_transport_pass.cellChanged.connect(lambda: self.update_by_change(
            table=self.ui.tableWidget_list_transport_pass,
            model=models.list_transport_pass.ListTransportPass
        ))

        # button to delete position from DB. ListTransportPass
        button_delete_list_transport_pass = self.ui.button_delete_position_list_transport_pass
        button_delete_list_transport_pass.clicked.connect(lambda: self.delete_from_db(
            table=self.ui.tableWidget_list_transport_pass,
            model=models.list_transport_pass.ListTransportPass
        ))

        button_delete_list_transport_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_list_transport_pass,
            model=models.list_transport_pass.ListTransportPass
        ))

        # searcher. ListTransportPass
        self.ui.lineEdit_searcher_list_transport_pass.textEdited.connect(lambda: self.filter_for_table(
            search_text=self.ui.lineEdit_searcher_list_transport_pass,
            table=self.ui.tableWidget_list_transport_pass
        ))

        # ------------------------------------------------------------------------------------------------------
        # TEMPORARY TRANSPORT PASS
        # button to download XLSX list to Postgres. TemporaryTransportPass
        self.ui.tableWidget_temporary_transport_pass.resizeColumnsToContents()
        button_add_temporary_transport_pass = self.ui.button_add_to_db_temporary_transport_pass
        button_add_temporary_transport_pass.clicked.connect(lambda: models.temporary_transport_pass.add_to_db(
            path=self.open_dialog_box(),
            pass_number=self.ui.edit_pass_number_temporary_transport_pass.text()))
        button_add_temporary_transport_pass.clicked.connect(lambda: self.ui.edit_pass_number_temporary_transport_pass.clear())
        button_add_temporary_transport_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_temporary_transport_pass,
            model=models.temporary_transport_pass.TemporaryTransportPass
        ))

        # button SHOW DB. TemporaryTransportPass
        button_show_temporary_transport_pass = self.ui.button_show_db_temporary_transport_pass
        button_show_temporary_transport_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_temporary_transport_pass,
            model=models.temporary_transport_pass.TemporaryTransportPass
        ))

        # update info in DB. TemporaryTransportPass
        self.ui.tableWidget_temporary_transport_pass.cellChanged.connect(lambda: self.update_by_change(
            table=self.ui.tableWidget_temporary_transport_pass,
            model=models.temporary_transport_pass.TemporaryTransportPass
        ))

        # button to delete position from DB. TemporaryTransportPass
        button_delete_temporary_transport_pass = self.ui.button_delete_position_temporary_transport_pass
        button_delete_temporary_transport_pass.clicked.connect(lambda: self.delete_from_db(
            table=self.ui.tableWidget_temporary_transport_pass,
            model=models.temporary_transport_pass.TemporaryTransportPass
        ))

        button_delete_temporary_transport_pass.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_temporary_transport_pass,
            model=models.temporary_transport_pass.TemporaryTransportPass
        ))

        # searcher. TemporaryTransportPass
        self.ui.lineEdit_searcher_temporary_transport_pass.textEdited.connect(lambda: self.filter_for_table(
            search_text=self.ui.lineEdit_searcher_temporary_transport_pass,
            table=self.ui.tableWidget_temporary_transport_pass
        ))

        # ------------------------------------------------------------------------------------------------------
        # CONSIGNMENT NOTE
        # button to download XLSX list to Postgres. ConsignmentNote
        self.ui.tableWidget_consignment_note.resizeColumnsToContents()
        button_add_consignment_note = self.ui.button_add_to_db_consignment_note
        button_add_consignment_note.clicked.connect(lambda: models.consignment_note.add_to_db(
            path=self.open_dialog_box(),
            pass_number=self.ui.edit_pass_number_consignment_note.text()))
        button_add_consignment_note.clicked.connect(
            lambda: self.ui.edit_pass_number_consignment_note.clear())
        button_add_consignment_note.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_consignment_note,
            model=models.consignment_note.ConsignmentNote
        ))

        # button SHOW DB. ConsignmentNote
        button_show_consignment_note = self.ui.button_show_db_consignment_note
        button_show_consignment_note.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_consignment_note,
            model=models.consignment_note.ConsignmentNote
        ))

        # update info in DB. ConsignmentNote
        self.ui.tableWidget_consignment_note.cellChanged.connect(lambda: self.update_by_change(
            table=self.ui.tableWidget_consignment_note,
            model=models.consignment_note.ConsignmentNote
        ))

        # button to delete position from DB. ConsignmentNote
        button_delete_consignment_note = self.ui.button_delete_position_consignment_note
        button_delete_consignment_note.clicked.connect(lambda: self.delete_from_db(
            table=self.ui.tableWidget_consignment_note,
            model=models.consignment_note.ConsignmentNote
        ))

        button_delete_consignment_note.clicked.connect(lambda: self.read_data_from_db(
            table=self.ui.tableWidget_consignment_note,
            model=models.consignment_note.ConsignmentNote
        ))

        # searcher. ConsignmentNote
        self.ui.lineEdit_searcher_consignment_note.textEdited.connect(lambda: self.filter_for_table(
            search_text=self.ui.lineEdit_searcher_consignment_note,
            table=self.ui.tableWidget_consignment_note
        ))
        
    # common function. All tables available.
    def open_dialog_box(self):
        """
        Open dialog box to choose an XLSX file.

        :return: path to a file
        :rtype: str
        """
        filename = QFileDialog.getOpenFileName(self)
        return filename[0]

    def update_by_change(self, table: QTableWidget, model):
        """
        Update values of QTableWidgetItem by changed cell and upload to DataBase.

        :param table: name of QTableWidget.
        :type table: QTableWidget
        :param model: class uses to connect SQL and Python's class object
        :type model: Any(Base)
        :return: None
        """
        username = read_config()[0]
        row_index = table.currentIndex().row()
        col_index = table.currentIndex().column()
        try:
            id_position = table.item(row_index, 0).text()
            new_data = table.item(row_index, col_index).text()
            content_from_db = self.session.query(model).get(id_position)
            content = dir(content_from_db)
            setattr(content_from_db, content[col_index][1], new_data)
            setattr(content_from_db, content[-1][1], f'User: {username}\nDate: {time.ctime()}')
            self.session.add(content_from_db)
            self.session.commit()
        except AttributeError:
            pass

    def read_data_from_db(self, table: QTableWidget, model):
        """
        Read all data from DataBase to QTableWidget (to UI).

        :param table: name of QTableWidget.
        :type table: QTableWidget
        :param model: class uses to connect SQL and Python's class object
        :type model: Any(Base)
        :return: None
        """
        all_row = table.rowCount()
        while all_row > 0:
            table.removeRow(all_row - 1)
            all_row = table.rowCount()

        try:

            all_data = self.session.query(model).all()

            for data in all_data:
                row = table.rowCount()
                table.insertRow(row)
                content = dir(data)
                for col_index in range(len(content)):
                    table.setItem(row, col_index, QTableWidgetItem(f'{getattr(data, content[col_index][1])}'))
                    table.resizeColumnsToContents()

        except (psycopg.errors.UndefinedTable, sqlalchemy.exc.ProgrammingError):
            pass

    @classmethod
    def find_position(cls, text, table: QTableWidget):
        """
        Searching text in table and hide by it (if the search is *not* in the item's text *do not hide* the row)

        :param text: text to search
        :type text: str
        :param table: table to search in UI
        :type table: QTableWidget
        :return: None
        """
        for row in range(table.rowCount()):
            searcher = []
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if text not in item.text().lower():
                    searcher.append(1)
                else:
                    searcher.append(0)
            if all(searcher):
                table.setRowHidden(row, True)

    def filter_for_table(self, search_text: QLineEdit, table: QTableWidget, text_len: list = [0]):
        """
        Make method *find_position* a dynamic filter

        :param search_text: text input field
        :type search_text: QLineEdit
        :param table: table to search in UI
        :type table: QTableWidget
        :param text_len: length of text in the search_text
        :type text_len: list
        :return: None
        """
        text = search_text.text().lower()
        if text_len[0] < len(text):
            text_len[0] = len(text)
            self.find_position(text, table)
        else:
            text_len[0] = len(text)
            for row in range(table.rowCount()):
                table.setRowHidden(row, False)
            self.find_position(text, table)

    def delete_from_db(self, table: QTableWidget, model):
        """
        Delete position in DataBase in clicked cell by ID.

        :param table: name of QTableWidget.
        :type table: QTableWidget
        :param model: class uses to connect SQL and Python's class object
        :type model: Any(Base)
        :return: None
        """
        row_index = table.currentIndex().row()

        id_position = table.item(row_index, 0).text()
        content_from_db = self.session.query(model).get(id_position)

        self.session.delete(content_from_db)
        self.session.commit()

    # local function. For ListStaffPass
    def update_photo_in_db(self):
        username = read_config()[0]
        row_index = self.ui.tableWidget_list_staff_pass.currentIndex().row()
        id_position = self.ui.tableWidget_list_staff_pass.item(row_index, 0).text()
        session = connect_db()
        person = session.query(models.list_staff_pass.ListStaffPass).get(id_position)

        photo_path = self.open_dialog_box()
        photo = PIL.Image.open(photo_path)
        photo = photo_change(image=photo)
        person.photo = photo
        person.history = f'User: {username}\nDate: {time.ctime()}'

        session.add(person)
        session.commit()

    def read_photo_from_db(self):
        try:
            row_index = self.ui.tableWidget_list_staff_pass.currentIndex().row()
            id_position = self.ui.tableWidget_list_staff_pass.item(row_index, 0).text()
            session = connect_db()
            person = session.query(models.list_staff_pass.ListStaffPass).get(id_position)
            photo = read_binary_photo(person.photo)
            photo.save(fp='photo', format='PNG')
            self.ui.label_photo_from_db_list_staff_pass.setPixmap(QPixmap('photo'))
            os.remove(path='photo')
        except PIL.UnidentifiedImageError:
            self.ui.label_photo_from_db_list_staff_pass.setPixmap(QPixmap(
                '/home/mikhail/Рабочий стол/Coding/my_projects/xlsx_to_postgres/gui/id-photo-design-illustration-isolated-on-white-background-free-vector.png'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    authorization = Authorization()
    authorization.show()
    sys.exit(app.exec())
