from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from mini_crm.database.database import get_session
from mini_crm.services import SourcesService

sources_router = APIRouter(prefix="/sources")
sources_service = SourcesService()


@sources_router.post("/")
async def create_source(name: str, session: AsyncSession = Depends(get_session)):
    return await sources_service.create_source(name, session)


@sources_router.post("/{source_id}/operators")
async def set_weights(
    source_id: int,
    operator_id: int,
    weight: int,
    session: AsyncSession = Depends(get_session),
):
    return await sources_service.set_weights(source_id, operator_id, weight, session)
