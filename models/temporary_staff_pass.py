import time

from sqlalchemy import Column, Integer, String

from models.connect_to_db import connect_db, Base, read_config
from models.read_xlsx import xlsx_to_dict


class TemporaryStaffPass(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'temporary_staff_pass'

    id_position = Column(Integer, primary_key=True)
    number_of_pass = Column(String(250))
    name = Column(String(250))
    position = Column(String(250))
    general_contractor = Column(String(250))
    subcontractor = Column(String(250))
    id_general_contractor = Column(String(250))
    id_subcontractor = Column(String(250))
    time_place = Column(String)
    birth_date = Column(String(250))
    valid_from_time = Column(String(250))
    valid_till_time = Column(String(250))
    passport_id = Column(String(250), nullable=False)
    passport_issued = Column(String)
    citizenship = Column(String(250))
    tax_id = Column(String)
    history = Column(String)

    def __init__(self, number_of_pass, name, position, general_contractor, subcontractor, id_general_contractor,
                 id_subcontractor, time_place, birth_date, valid_from_time, valid_till_time, passport_id,
                 passport_issued, citizenship, tax_id, history):
        self.number_of_pass = number_of_pass
        self.name = name
        self.position = position
        self.general_contractor = general_contractor
        self.subcontractor = subcontractor
        self.id_general_contractor = id_general_contractor
        self.id_subcontractor = id_subcontractor
        self.time_place = time_place
        self.birth_date = birth_date
        self.valid_from_time = valid_from_time
        self.valid_till_time = valid_till_time
        self.passport_id = passport_id
        self.passport_issued = passport_issued
        self.citizenship = citizenship
        self.tax_id = tax_id
        self.history = history

    @classmethod
    def __dir__(cls):
        return [[0, 'id_position'], [1, 'number_of_pass'], [2, 'name'], [3, 'position'], [4, 'general_contractor'],
                [5, 'subcontractor'], [6, 'id_general_contractor'], [7, 'id_subcontractor'], [8, 'time_place'],
                [9, 'birth_date'], [10, 'valid_from_time'], [11, 'valid_till_time'], [12, 'passport_id'],
                [13, 'passport_issued'], [14, 'citizenship'], [15, 'tax_id'], [16, 'history']]


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
            if name == 'None' or info[9] == 'None':
                pass
            else:
                staff = TemporaryStaffPass(
                    number_of_pass=pass_number,
                    name=name,
                    position=info[0],
                    general_contractor=info[1],
                    subcontractor=info[2],
                    id_general_contractor=info[3],
                    id_subcontractor=info[4],
                    time_place=info[5],
                    birth_date=info[6],
                    valid_from_time=info[7],
                    valid_till_time=info[8],
                    passport_id=info[9],
                    passport_issued=info[10],
                    citizenship=info[11],
                    tax_id=info[12],
                    history=f'User: {username}\nDate: {time.ctime()}'
                )
                if (staff.number_of_pass, staff.name, staff.passport_id) in \
                        list(session.query(TemporaryStaffPass.number_of_pass, TemporaryStaffPass.name,
                                           TemporaryStaffPass.passport_id)):
                    pass
                else:
                    session.add(staff)
    session.commit()


if __name__ == '__main__':
    path = '/home/mikhail/Рабочий стол/Coding/my_projects/xlsx_to_postgres/samples/временные пропуска персонала.xlsx'
    add_to_db(
        path=path,
        pass_number='7')
