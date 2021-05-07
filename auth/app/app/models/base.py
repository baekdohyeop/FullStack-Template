import re

from sqlalchemy import Column, func
from sqlalchemy.types import Boolean, Integer, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Column = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    deleted = Column(
        Boolean,
        index=True,
        default=False
    )
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.Now()
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.Now(),
        server_onupdate=func.Now()
    )

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()
