from sqlalchemy.ext.asyncio import AsyncSession
from mini_crm.database.models import Source, SourceConfig


class SourcesService:
    async def create_source(self, name: str, session: AsyncSession):
        source = Source(name=name)
        session.add(source)
        await session.commit()
        return source

    async def set_weights(
        self,
        source_id: int,
        operator_id: int,
        weight: int,
        session: AsyncSession,
    ):
        new_source_config = SourceConfig(
            source_id=source_id, operator_id=operator_id, weight=weight
        )
        session.add(new_source_config)
        await session.commit()
        return new_source_config
