import time

from sqlalchemy import Column, Integer, String

from models.connect_to_db import connect_db, Base, read_config
from models.read_xlsx import xlsx_to_dict


class TemporaryTransportPass(Base):
    """
    Create table in DB with Column below.
    """
    __tablename__ = 'temporary_transport_pass'

    id_position = Column(Integer, primary_key=True)
    number_of_pass = Column(String(250))
    model = Column(String(250))
    type_ts = Column(String(250))
    registration_number = Column(String(250), nullable=False)
    place = Column(String(250))
    general_contractor = Column(String(250))
    valid_from_date = Column(String(250))
    valid_till_date = Column(String(250))
    owner = Column(String(250))
    general_contractor_id = Column(String(250))
    additional = Column(String)
    history = Column(String)

    def __init__(self, number_of_pass, model, type_ts, registration_number, place, general_contractor,
                 valid_from_date, valid_till_date, owner, general_contractor_id, additional, history):
        self.number_of_pass = number_of_pass
        self.model = model
        self.type_ts = type_ts
        self.registration_number = registration_number
        self.place = place
        self.general_contractor = general_contractor
        self.valid_from_date = valid_from_date
        self.valid_till_date = valid_till_date
        self.owner = owner
        self.general_contractor_id = general_contractor_id
        self.additional = additional
        self.history = history

    @classmethod
    def __dir__(cls):
        return [[0, 'id_position'], [1, 'number_of_pass'], [2, 'model'], [3, 'type_ts'], [4, 'registration_number'],
                [5, 'place'], [6, 'general_contractor'], [7, 'valid_from_date'], [8, 'valid_till_date'],
                [9, 'owner'], [10, 'general_contractor_id'], [11, 'additional'], [12, 'history']]


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
            if info[1] == 'None':
                pass
            else:
                staff = TemporaryTransportPass(
                    number_of_pass=pass_number,
                    model=name,
                    type_ts=info[0],
                    registration_number=info[1],
                    place=info[2],
                    general_contractor=info[3],
                    valid_from_date=info[4][0:10],
                    valid_till_date=info[5][0:10],
                    owner=info[6],
                    general_contractor_id=info[7],
                    additional=info[8],
                    history=f'User: {username}\nDate: {time.ctime()}'
                )
                if (staff.number_of_pass, staff.registration_number) in \
                        list(session.query(TemporaryTransportPass.number_of_pass,
                                           TemporaryTransportPass.registration_number)):
                    pass
                else:
                    session.add(staff)
    session.commit()


if __name__ == '__main__':
    pass
