from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from mini_crm.database.database import get_session
from mini_crm.services.distribution import choose_operator
from mini_crm.services import ContactService, LeadsService

from sqlalchemy import select
from mini_crm.database.models import Contact

contact_router = APIRouter(prefix="/contacts")
contact_service = ContactService()
leads_service = LeadsService()


@contact_router.post("/")
async def create_contact(
    lead_id: str, source_id: int, msg: str, session: AsyncSession = Depends(get_session)
):
    lead = await leads_service.get_lead_by_id(lead_id, session)
    if not lead:
        lead = await leads_service.create_new_lead(lead_id, session)

    operator = await choose_operator(source_id, session)
    operator_id = operator.id if operator else None

    await contact_service.create_contact(lead_id, source_id, operator_id, msg, session)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"lead": lead.id, "operator": operator_id},
    )


@contact_router.get("/")
async def list_contacts(session: AsyncSession = Depends(get_session)):
    q = select(Contact)
    result = await session.execute(q)
    return result.scalars().all()
