# Patient API

A FastAPI web service backed by PostgreSQL, built against the `Patients` table
defined in [patient.sql](patient.sql).

## Project structure

```
app/
  main.py          FastAPI app entrypoint
  config.py        Settings loaded from .env
  database.py      SQLAlchemy engine/session
  models.py        Patient ORM model
  schemas.py       Pydantic request/response models
  crud.py          Database operations
  routers/
    patients.py    /patients endpoints
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure database connection in `.env`:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=simpleclinic
DB_USER=postgres
DB_PASSWORD=password
```

## Run

```bash
python -m uvicorn app.main:app --reload
```

Run as a module from the project root — running `app/main.py` directly as a
script fails with `ModuleNotFoundError: No module named 'app'`.

A VS Code debug config is also available: press F5 and choose **FastAPI: uvicorn**.

## Testing

### Swagger UI (easiest)

Open `http://127.0.0.1:8000/docs` for interactive forms for every endpoint.

### curl

```bash
# health check
curl http://127.0.0.1:8000/health

# list patients
curl http://127.0.0.1:8000/patients/

# get one
curl http://127.0.0.1:8000/patients/1

# create
curl -X POST http://127.0.0.1:8000/patients/ \
  -H "Content-Type: application/json" \
  -d '{"registered_by":"U001","mrn":"MRN-001","full_name":"Jane Doe","dob":"1990-05-20","ic_num":"900520-01-1234","barcode":"BC0001"}'

# update
curl -X PUT http://127.0.0.1:8000/patients/1 \
  -H "Content-Type: application/json" \
  -d '{"full_name":"Jane A. Doe"}'

# delete
curl -X DELETE http://127.0.0.1:8000/patients/1
```

### Note: `RegisteredBy` foreign key

`Patients.RegisteredBy` references `Users.UserID` in [patient.sql](patient.sql).
The `simpleclinic` database (used by default) has no `users` table, so this FK
isn't enforced there — any `registered_by` value is accepted. If you point the
API at a database that does enforce this FK (e.g. `middlewaredb`), a
`registered_by` with no matching `users.userid` row returns `409 Conflict`.
