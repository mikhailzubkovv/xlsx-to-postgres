import time

from sqlalchemy import Column, Integer, String

from models.connect_to_db import connect_db, Base, read_config
from models.read_xlsx import xlsx_to_dict


class ConsignmentNote(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'consignment_note'

    id_position = Column(Integer, primary_key=True)
    number_of_pass = Column(String(250))
    shipper = Column(String(250))
    consignee = Column(String(250))
    materially_responsible_person = Column(String(250))
    carrier = Column(String(250))
    material_values = Column(String(250))
    valid_from_date = Column(String(250))
    valid_till_date = Column(String(250))
    history = Column(String)

    def __init__(self, number_of_pass, shipper, consignee, materially_responsible_person, carrier, material_values,
                 valid_from_date, valid_till_date, history):
        self.number_of_pass = number_of_pass
        self.shipper = shipper
        self.consignee = consignee
        self.materially_responsible_person = materially_responsible_person
        self.carrier = carrier
        self.material_values = material_values
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.history = history

    @classmethod
    def __dir__(cls):
        return [[0, 'id_position'], [1, 'number_of_pass'], [2, 'shipper'], [3, 'consignee'],
                [4, 'materially_responsible_person'], [5, 'carrier'], [6, 'material_values'], [7, 'valid_from_date'],
                [8, 'valid_till_date'], [9, 'history']]


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
            if info[3] == 'None':
                pass
            else:
                staff = ConsignmentNote(
                    number_of_pass=pass_number,
                    shipper=name,
                    consignee=info[0],
                    materially_responsible_person=info[1],
                    carrier=info[2],
                    material_values=info[3],
                    valid_from_date=info[4][0:10],
                    valid_till_date=info[5][0:10],
                    history=f'User: {username}\nDate: {time.ctime()}'
                )
                if (staff.number_of_pass, staff.material_values) in \
                        list(session.query(ConsignmentNote.number_of_pass,
                                           ConsignmentNote.material_values)):
                    pass
                else:
                    session.add(staff)
    session.commit()


if __name__ == '__main__':
    path = '/home/mikhail/Рабочий стол/Coding/my_projects/xlsx_to_postgres/samples/ТТН.xlsx'
    add_to_db(
        path=path,
        pass_number='7')
