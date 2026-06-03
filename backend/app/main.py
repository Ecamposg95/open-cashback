from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth, blockchain, branches, campaigns, cashback, customers, organizations, redemptions, reports, sales, wallets
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(title=settings.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_prefix = "/api/v1"
app.include_router(auth.router, prefix=api_prefix)
app.include_router(organizations.router, prefix=api_prefix)
app.include_router(branches.router, prefix=api_prefix)
app.include_router(customers.router, prefix=api_prefix)
app.include_router(sales.router, prefix=api_prefix)
app.include_router(wallets.router, prefix=api_prefix)
app.include_router(cashback.router, prefix=api_prefix)
app.include_router(campaigns.router, prefix=api_prefix)
app.include_router(redemptions.router, prefix=api_prefix)
app.include_router(reports.router, prefix=api_prefix)
app.include_router(blockchain.router, prefix=api_prefix)


@app.get("/health")
def health():
    return {"status": "ok", "service": settings.app_name}
