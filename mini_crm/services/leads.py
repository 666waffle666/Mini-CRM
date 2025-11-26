from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from mini_crm.database.models import Lead


class LeadsService:
    async def get_lead_by_id(self, lead_id: str, session: AsyncSession):
        statement = select(Lead).where(Lead.external_id == lead_id)
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    async def create_new_lead(self, lead_id: str, session: AsyncSession):
        new_lead = Lead(external_id=lead_id)
        session.add(new_lead)
        await session.flush()
        await session.refresh(new_lead)
        return new_lead

    async def list_leads(self, session: AsyncSession):
        statement = select(Lead)
        result = await session.execute(statement)
        return result.scalars().all()
