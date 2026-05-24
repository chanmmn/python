from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Boolean
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.sql import func
from datetime import date

DATABASE_URL = "postgresql+psycopg2://postgres:Abcd@localhost/mybank"

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    __table_args__ = {"schema": "public"}

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    id_number = Column(String(50), nullable=True, unique=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_default=func.now(), nullable=True)
    is_active = Column(Boolean, default=True, nullable=True)


def insert_customer(session: Session, **kwargs) -> Customer:
    customer = Customer(**kwargs)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


if __name__ == "__main__":
    with Session(engine) as session:
        new_customer = insert_customer(
            session,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="555-1234",
            address="123 Main St, Springfield",
            date_of_birth=date(1990, 5, 15),
            id_number="ID-987654",
            is_active=True,
        )
        print(f"Inserted customer with ID: {new_customer.customer_id}")
