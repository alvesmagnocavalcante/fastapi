from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text, Numeric, Integer, func, Enum as SAEnum
from typing import Optional, TYPE_CHECKING
from datetime import datetime
from decimal import Decimal
from enum import Enum
from models.base import Base

if TYPE_CHECKING:
    from models.users import User


class TransmissionType(str, Enum):
    MANUAL = 'manual'
    AUTOMATIC = 'automatic'
    SEMI_AUTOMATIC = 'semi_automatic'
    CVT = 'cvt'


class FuelType(str, Enum):
    GASOLINE = 'gasoline'
    ETHANOL = 'ethanol'
    FLEX = 'flex'
    DIESEL = 'diesel'
    ELECTRIC = 'electric'
    HYBRID = 'hybrid'


class Brand(Base):
    __tablename__ = 'brands'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    is_active: Mapped[bool] = mapped_column(default=True)
    description: Mapped[Optional[str]] = mapped_column(Text)

    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

    cars: Mapped[list["Car"]] = relationship(
        "Car",
        back_populates="brand"
    )


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(100))

    factory_year: Mapped[int] = mapped_column(Integer)
    model_year: Mapped[int] = mapped_column(Integer)

    brand_id: Mapped[int] = mapped_column(
        ForeignKey('brands.id'),
        nullable=False
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )

    color: Mapped[str] = mapped_column(String(30))

    plate: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        index=True
    )

    transmission: Mapped[TransmissionType] = mapped_column(
        SAEnum(TransmissionType)
    )

    fuel_type: Mapped[FuelType] = mapped_column(
        SAEnum(FuelType)
    )

    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    description: Mapped[Optional[str]] = mapped_column(Text)

    is_available: Mapped[bool] = mapped_column(default=True)

    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

    brand: Mapped["Brand"] = relationship(
        "Brand",
        back_populates="cars"
    )

    owner: Mapped["User"] = relationship(
        "User",
        back_populates="cars"
    )
