# mini_crm/API/leads.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from mini_crm.database.database import get_session
from mini_crm.services import LeadsService

leads_router = APIRouter()
leads_service = LeadsService()


@leads_router.get("/leads")
async def list_leads(session: AsyncSession = Depends(get_session)):
    return await leads_service.list_leads(session)
