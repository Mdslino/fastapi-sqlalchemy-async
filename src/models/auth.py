from sqlalchemy import Column, String, Boolean, BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from src.db.base_class import BaseModel


class Group(BaseModel):
    name = Column(String, nullable=False, unique=True)
    groups = relationship("GroupPermission", lazy="joined")


class Permission(BaseModel):
    name = Column(String, nullable=False, unique=True)
    code = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False, unique=True)


class GroupPermission(BaseModel):
    __table_args__ = (UniqueConstraint("group_id", "permission_id", name="_group_permission_uc"),)
    group_id = Column(BigInteger, ForeignKey("group.id", ondelete="CASCADE"), index=True, nullable=False)
    permission_id = Column(BigInteger, ForeignKey("permission.id", ondelete="CASCADE"), index=True, nullable=False)


class User(BaseModel):
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    groups = relationship("UserGroup", lazy="joined")


class UserGroup(BaseModel):
    __table_args__ = (UniqueConstraint("user_id", "group_id", name="_user_group_uc"),)
    user_id = Column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), index=True, nullable=False)
    group_id = Column(BigInteger, ForeignKey("group.id", ondelete="CASCADE"), index=True, nullable=False)
