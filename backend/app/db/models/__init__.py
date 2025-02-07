from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


dancer_nomination_association = Table(
    "dancer_nomination",
    Base.metadata,
    Column("dancer_id", Integer, ForeignKey("dancers.id")),
    Column("nomination_id", Integer, ForeignKey("nominations.id")),
)


class Dancer(Base):
    __tablename__ = "dancers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nominations = relationship(
        "Nomination", secondary=dancer_nomination_association, back_populates="dancers"
    )


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nominations = relationship("Nomination", back_populates="tournament")


class Nomination(Base):
    __tablename__ = "nominations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    tournament = relationship("Tournament", back_populates="nominations")
    dancers = relationship(
        "Dancer", secondary=dancer_nomination_association, back_populates="nominations"
    )
