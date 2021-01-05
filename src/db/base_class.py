from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    id: int
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()


class BaseModel(Base):
    __abstract__ = True

    id: int = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
        unique=True,
    )
    created_at: int = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: int = Column(DateTime, nullable=True, default=None, onupdate=datetime.utcnow)
