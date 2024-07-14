from .base import Base
from sqlalchemy.orm import Mapped


class Product(Base):
    name: Mapped[str] = "Name"
    description: Mapped[str] = "Description"
    price: Mapped[int] = "Price"
