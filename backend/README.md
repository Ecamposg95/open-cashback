# Backend

FastAPI backend para Open Cashback.

## Local

```bash
cd backend
python -m pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

API: http://localhost:8000
OpenAPI: http://localhost:8000/docs
