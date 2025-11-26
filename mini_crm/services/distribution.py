import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from mini_crm.database.models import Operator, Contact, SourceConfig


async def choose_operator(source_id: int, session: AsyncSession) -> Operator | None:
    statement = (
        select(Operator, SourceConfig.weight)
        .join(SourceConfig, SourceConfig.operator_id == Operator.id)
        .where(SourceConfig.source_id == source_id, Operator.is_active)
    )
    result = await session.execute(statement)
    available_operators = result.all()

    if not available_operators:
        return None

    available = []
    for operator, weight in available_operators:
        statement2 = select(func.count(Contact.id)).where(
            Contact.operator_id == operator.id
        )
        count = (await session.execute(statement2)).scalar_one()

        if count < operator.limit:
            available.append((operator, weight))

    if not available:
        return None

    operators, weights = zip(*available)
    return random.choices(operators, weights=weights, k=1)[0]
