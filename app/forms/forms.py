from typing import List

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Merch(Base):
    __tablename__ = "merches"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


assoc_merch = Table(
    "assoc_merch",
    Base.metadata,
    Column("name_id", ForeignKey("shoplist.id")),
    Column("merch_id", ForeignKey("merches.id"))
)


class ShopList(Base):
    __tablename__ = "shoplist"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    merches: Mapped[List[Merch]] = relationship(secondary=assoc_merch)


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[int] = mapped_column()


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    grade_id: Mapped[int] = mapped_column(ForeignKey(Grade.id))
    text: Mapped[str] = mapped_column(String())
    grade: Mapped[Grade] = relationship()