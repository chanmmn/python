#!/usr/bin/env python3
"""Update one product row in PostgreSQL using SQLAlchemy."""

from __future__ import annotations

import argparse
from typing import Any

from sqlalchemy import MetaData, Table, create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

DB_HOST = "localhost"
DB_NAME = "northwind"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_PORT = 5432
TABLE_NAME = "products"


def get_engine():
    url = URL.create(
        drivername="postgresql+psycopg2",
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
    return create_engine(url, echo=False, future=True)


def get_table(engine, table_name: str) -> Table:
    metadata = MetaData()
    return Table(table_name, metadata, autoload_with=engine)


def get_primary_key_column_name(table: Table) -> str:
    pk_cols = list(table.primary_key.columns)
    if not pk_cols:
        raise ValueError(f"Table '{table.name}' has no primary key.")
    return pk_cols[0].name


def cast_value_by_column(table: Table, column: str, raw_value: str) -> Any:
    col = table.c[column]
    try:
        python_type = col.type.python_type
    except Exception:
        return raw_value

    if python_type is bool:
        return raw_value.lower() in {"1", "true", "yes", "y", "on"}

    try:
        return python_type(raw_value)
    except Exception:
        return raw_value


def parse_set_arguments(table: Table, set_args: list[str]) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for item in set_args:
        if "=" not in item:
            raise ValueError(f"Invalid --set value '{item}'. Use column=value.")
        key, raw_val = item.split("=", 1)
        key = key.strip()
        if key not in table.c:
            raise ValueError(f"Column '{key}' does not exist in table '{table.name}'.")
        values[key] = cast_value_by_column(table, key, raw_val.strip())
    return values


def main() -> None:
    parser = argparse.ArgumentParser(description="Update one row in products table")
    parser.add_argument("--id", required=True, help="Primary key value of row to update")
    parser.add_argument(
        "--set",
        dest="set_values",
        action="append",
        required=True,
        help="Column assignment in format column=value. Repeat for multiple fields.",
    )
    args = parser.parse_args()

    engine = get_engine()
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

    try:
        products = get_table(engine, TABLE_NAME)
        pk_name = get_primary_key_column_name(products)
        values = parse_set_arguments(products, args.set_values)
        if pk_name in values:
            raise ValueError("Updating the primary key is not allowed.")
    except (SQLAlchemyError, ValueError) as e:
        print(f"Setup error: {e}")
        return

    with SessionLocal() as session:
        try:
            stmt = products.update().where(products.c[pk_name] == args.id).values(**values)
            result = session.execute(stmt)
            session.commit()

            row = session.execute(
                select(products).where(products.c[pk_name] == args.id)
            ).mappings().first()
            print(f"UPDATE affected rows: {result.rowcount}")
            print(f"Updated row: {dict(row) if row else None}")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Database error: {e}")


if __name__ == "__main__":
    main()
