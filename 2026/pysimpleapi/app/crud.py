from sqlalchemy.orm import Session

from app import models, schemas


def get_patient(db: Session, patient_id: int) -> models.Patient | None:
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()


def get_patient_by_mrn(db: Session, mrn: str) -> models.Patient | None:
    return db.query(models.Patient).filter(models.Patient.mrn == mrn).first()


def get_patients(db: Session, skip: int = 0, limit: int = 100) -> list[models.Patient]:
    return db.query(models.Patient).offset(skip).limit(limit).all()


def create_patient(db: Session, patient: schemas.PatientCreate) -> models.Patient:
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def update_patient(
    db: Session, db_patient: models.Patient, patient: schemas.PatientUpdate
) -> models.Patient:
    for field, value in patient.model_dump(exclude_unset=True).items():
        setattr(db_patient, field, value)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, db_patient: models.Patient) -> None:
    db.delete(db_patient)
    db.commit()
