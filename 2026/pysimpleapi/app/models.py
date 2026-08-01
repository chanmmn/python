from sqlalchemy import Column, Date, DateTime, Integer, String, func

from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column("patientid", Integer, primary_key=True)
    registered_by = Column("registeredby", String(10), nullable=False)
    mrn = Column("mrn", String(50), nullable=False, unique=True)
    full_name = Column("fullname", String(100), nullable=False)
    dob = Column("dob", Date, nullable=False)
    ic_num = Column("icnum", String(20), nullable=False)
    barcode = Column("barcode", String(100), nullable=False)
    registered_time = Column("registeredtime", DateTime, server_default=func.now())
    last_updated = Column("lastupdated", DateTime, server_default=func.now())
