from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String
from datetime import datetime
from typing import TYPE_CHECKING
from models.base import Base

if TYPE_CHECKING:
    from models.cars import Car


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    password: Mapped[str] = mapped_column(String)

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

    cars: Mapped[list["Car"]] = relationship(
        "Car",
        back_populates="owner"
    )
