from sqlalchemy.ext.asyncio import create_async_engine

from src.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)