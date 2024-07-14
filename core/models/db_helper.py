# from sqlalchemy.ext.asyncio import (
#     AsyncSession,
#     create_async_engine,
#     async_sessionmaker,
#     async_scoped_session,
# )
# from ..config import settings
# from sqlalchemy.orm import sessionmaker
# from asyncio import current_task
# from contextlib import asynccontextmanager
#
#
# class DatabaseHelper:
#     def __init__(self, url: str, echo: bool = False):
#         self.engine = create_async_engine(url=url, echo=echo)
#
#         self.session_factory = async_sessionmaker(
#             bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
#         )
#
#     def get_scoped_session(self):
#         session = async_scoped_session(
#             session_factory=self.session_factory,
#             scopefunc=current_task,
#         )
#         return session
#
#     # async def session_dependency(self) -> AsyncSession:
#     #     async with self.get_scoped_session() as session:
#     #         yield session
#     #         await session.remove()
#
#     @asynccontextmanager
#     async def session_dependency(self) -> AsyncSession:
#         session = self.get_scoped_session()
#         try:
#             yield session
#         finally:
#             await session.remove()
#
#
# db_helper = DatabaseHelper(
#     url=settings.db_url,
#     echo=settings.echo,
# )
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker
from asyncio import current_task
from contextlib import asynccontextmanager
from ..config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )

    @asynccontextmanager
    async def session_dependency(self):
        session = self.session_factory()  # создаем сессию
        try:
            yield session
        finally:
            await session.close()  # закрываем сессию в конце


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.echo,
)
