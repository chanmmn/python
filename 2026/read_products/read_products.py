#!/usr/bin/env python3
"""Read product rows from PostgreSQL using SQLAlchemy."""

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


def read_by_id(session, table: Table, product_id: Any) -> dict[str, Any] | None:
    pk_name = get_primary_key_column_name(table)
    stmt = select(table).where(table.c[pk_name] == product_id)
    row = session.execute(stmt).mappings().first()
    return dict(row) if row else None


def read_all(session, table: Table, limit: int) -> list[dict[str, Any]]:
    stmt = select(table).limit(limit)
    rows = session.execute(stmt).mappings().all()
    return [dict(r) for r in rows]


def main() -> None:
    parser = argparse.ArgumentParser(description="Read from products table")
    parser.add_argument("--id", dest="product_id", help="Primary key value to read one row")
    parser.add_argument("--limit", type=int, default=20, help="Max rows when reading all")
    args = parser.parse_args()

    engine = get_engine()
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

    try:
        products = get_table(engine, TABLE_NAME)
    except SQLAlchemyError as e:
        print(f"Setup error: {e}")
        return

    with SessionLocal() as session:
        try:
            if args.product_id is not None:
                row = read_by_id(session, products, args.product_id)
                print(row)
            else:
                rows = read_all(session, products, args.limit)
                print(rows)
        except (SQLAlchemyError, ValueError) as e:
            print(f"Database error: {e}")


if __name__ == "__main__":
    main()
