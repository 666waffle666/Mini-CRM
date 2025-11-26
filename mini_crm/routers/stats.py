from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from sqlalchemy import select, func
from mini_crm.database.models import Operator, Contact
from mini_crm.database.database import get_session

stats_router = APIRouter(prefix="/stats")


@stats_router.get("/operators")
async def operator_stats(session: AsyncSession = Depends(get_session)):
    q = (
        select(Operator.name, func.count(Contact.id))
        .join(Contact, Contact.operator_id == Operator.id, isouter=True)
        .group_by(Operator.id)
    )

    rows = (await session.execute(q)).all()
    return [{"operator": name, "contacts": count} for name, count in rows]
