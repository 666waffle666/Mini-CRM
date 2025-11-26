from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from mini_crm.database.database import get_session
from mini_crm.services import OperatorsService

operators_router = APIRouter(prefix="/operators")
operators_service = OperatorsService()


@operators_router.post("/")
async def create_operator(
    name: str, max_load: int = 5, session: AsyncSession = Depends(get_session)
):
    return await operators_service.create_operator(name, max_load, session)


@operators_router.get("/")
async def list_operators(session: AsyncSession = Depends(get_session)):
    return await operators_service.list_operators(session)


@operators_router.patch("/{op_id}")
async def update_operator(
    op_id: int,
    is_active: bool | None = None,
    max_load: int | None = None,
    session: AsyncSession = Depends(get_session),
):
    updated_operator = await operators_service.update_operator(
        op_id, is_active, max_load, session
    )

    return updated_operator
