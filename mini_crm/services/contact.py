from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from mini_crm.database.models import Lead, Contact


class ContactService:
    async def create_contact(
        self,
        lead_id: str,
        source_id: int,
        operator_id: int | None,
        msg: str,
        session: AsyncSession,
    ):
        contact = Contact(
            lead_id=lead_id,
            source_id=source_id,
            operator_id=operator_id,
            message_data=msg,
        )
        session.add(contact)
        await session.commit()
