from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from mini_crm.database.models import Operator


class OperatorsService:
    async def get_operator_by_id(self, operator_id: int, session: AsyncSession):
        statement = select(Operator).where(Operator.id == operator_id)
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    async def create_operator(self, name: str, max_load: int, session: AsyncSession):
        new_operator = Operator(name=name, max_load=max_load)
        session.add(new_operator)
        await session.commit()
        return new_operator

    async def list_operators(self, session: AsyncSession):
        result = await session.execute(select(Operator))
        return result.scalars().all()

    async def update_operator(
        self,
        op_id: int,
        is_active: bool | None,
        max_load: int | None,
        session: AsyncSession,
    ):
        operator = await self.get_operator_by_id(op_id, session)
        if not operator:
            return False

        if is_active is None:
            is_active = operator.is_active
        if max_load is None:
            max_load = operator.max_load

        operator.is_active = is_active
        operator.max_load = max_load

        await session.commit()
        return operator
