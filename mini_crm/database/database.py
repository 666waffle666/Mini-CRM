from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./mini_crm.db"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSession = async_sessionmaker(
    autocommit=False, expire_on_commit=False, autoflush=False, bind=engine
)


async def get_session():
    async with AsyncSession() as session:
        try:
            yield session
        finally:
            await session.close()
