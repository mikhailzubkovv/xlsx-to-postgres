import time

from sqlalchemy import Column, Integer, String

from models.connect_to_db import connect_db, Base, read_config
from models.read_xlsx import xlsx_to_dict


class ListStaffPass(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'list_staff_pass'

    id_position = Column(Integer, primary_key=True)
    number_of_pass = Column(String(250))
    name = Column(String(250), nullable=False)
    position = Column(String(250))
    country_in = Column(String(250))
    passport_id = Column(String(250), nullable=False)
    general_contractor = Column(String(250))
    subcontractor = Column(String(250))
    oilfield_name = Column(String(250))
    valid_from_date = Column(String(250))
    valid_till_date = Column(String(250))
    photo = Column(String)
    history = Column(String)

    def __init__(self, number_of_pass, name, position, country_in, passport_id, general_contractor, subcontractor,
                 oilfield_name, valid_from_date, valid_till_date, photo, history):
        self.number_of_pass = number_of_pass
        self.name = name
        self.position = position
        self.country_in = country_in
        self.passport_id = passport_id
        self.general_contractor = general_contractor
        self.subcontractor = subcontractor
        self.oilfield_name = oilfield_name
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.photo = photo
        self.history = history

    @classmethod
    def __dir__(cls):
        return [[0, 'id_position'], [1, 'number_of_pass'], [2, 'name'], [3, 'position'], [4, 'country_in'],
                [5, 'passport_id'], [6, 'general_contractor'], [7, 'subcontractor'], [8, 'oilfield_name'],
                [9, 'valid_from_date'], [10, 'valid_till_date'], [11, 'history']]


def add_to_db(path: str, pass_number: str) -> None:
    """
    Upload XLSX file to DB.
    """
    session = connect_db()
    username = read_config()[0]
    data = xlsx_to_dict(path)
    if data is None:
        pass
    else:
        for name, info in data.items():
            if name == 'None' or info[2] == 'None':
                pass
            else:
                staff = ListStaffPass(
                    number_of_pass=pass_number,
                    name=name,
                    position=info[0],
                    country_in=info[1],
                    passport_id=info[2],
                    general_contractor=info[3],
                    subcontractor=info[4],
                    oilfield_name=info[5],
                    valid_from_date=info[6][0:10],
                    valid_till_date=info[7][0:10],
                    photo=info[8],
                    history=f'User: {username}\nDate: {time.ctime()}'
                )
                if (staff.number_of_pass, staff.name, staff.passport_id) in \
                        list(session.query(ListStaffPass.number_of_pass, ListStaffPass.name,
                                           ListStaffPass.passport_id)):
                    pass
                else:
                    session.add(staff)
    session.commit()


if __name__ == '__main__':
    path = '/home/mikhail/Рабочий стол/Coding/my_projects/xlsx_to_postgres/samples/по спискам персонал.xlsx'
    add_to_db(
        path=path,
        pass_number='3')
