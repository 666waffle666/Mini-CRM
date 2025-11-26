from fastapi import FastAPI
from mini_crm.routers import (
    contact_router,
    leads_router,
    operators_router,
    sources_router,
    stats_router,
)

app = FastAPI(title="Mini CRM")

app.include_router(contact_router, tags=["Contacts"])
app.include_router(leads_router, tags=["Leads"])
app.include_router(operators_router, tags=["Operators"])
app.include_router(sources_router, tags=["Sources"])
app.include_router(stats_router, tags=["Stats"])
