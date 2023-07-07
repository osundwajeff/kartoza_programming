#!/usr/bin/python3
"""Models class"""

import sqlalchemy
from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey, String, Column, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Date, UUID


class Base(DeclarativeBase):
    pass


class PointOfInterestTypeClass(Base):
    __tablename__ = "point_of_interest_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    notes = Column(String(255))
    image = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    uuid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=sqlalchemy.text("gen_random_uuid()"))

    point_of_interests = relationship(
        "PointOfInterestClass", back_populates="point_of_interest_types")


class PointOfInterestClass(Base):
    __tablename__ = "point_of_interest"

    id = Column(Integer, primary_key=True, autoincrement=True)
    notes = Column(String(255))
    image = Column(String(255))
    height_m = Column(Float)
    installation_date = Column(Date, nullable=True)
    is_date_estimated = Column(Boolean, default=False)
    geometry = Column(Geometry("POINT"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    uuid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=sqlalchemy.text("gen_random_uuid()"))
    point_of_interest_type_uuid = Column(
        UUID(as_uuid=True),
        ForeignKey("point_of_interest_type.uuid"),
        nullable=False)

    # one to many relationship
    point_of_interest_types = relationship(
        "PointOfInterestTypeClass", back_populates="point_of_interests")

    # many-to-many relationship to Condition,
    # bypassing the `PointOfInterestConditionsClass'
    condition_as: Mapped[List["Condition"]] = relationship(
        secondary="point_of_interest_conditions",
        back_populates="point_of_interest_as"
        )

    # association between PointOfInterestClass -> PointOfInterestConditionClass
    # -> PointOfInterestClass
    condition_association: Mapped[
        List["PointOfInterestConditionsClass"]] = relationship(
        "PointOfInterestConditionsClass",
        back_populates="point_of_interest"
        )


class Condition(Base):
    __tablename__ = "condition"

    id = Column(Integer, primary_key=True, autoincrement=True)
    notes = Column(String(255))
    image = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    uuid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=sqlalchemy.text("gen_random_uuid()"))

    # many-to-many relationship to PointOfInterestClass,
    # bypassing the `PointOfInterestConditionsClass'
    point_of_interest_as: Mapped[List["PointOfInterestClass"]] = relationship(
        secondary="point_of_interest_conditions",
        back_populates="condition_as"
        )

    # association between Condition -> PointOfInterestConditionClass
    # -> PointOfInterestClass
    point_of_interest_association: Mapped[
        List["PointOfInterestConditionsClass"]] = relationship(
        "PointOfInterestConditionsClass",
        back_populates="condition"
        )


class PointOfInterestConditionsClass(Base):
    __tablename__ = "point_of_interest_conditions"

    date = Column(DateTime, default=datetime.now(), primary_key=True)
    notes = Column(String(255))
    image = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    uuid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=sqlalchemy.text("gen_random_uuid()"))
    point_of_interest_uuid = Column(UUID(as_uuid=True),
                                    ForeignKey("point_of_interest.uuid"),
                                    primary_key=True,
                                    nullable=False)
    condition_uuid = Column(
        UUID(as_uuid=True),
        ForeignKey("condition.uuid"),
        primary_key=True,
        nullable=False)

    # association between PointOfInterestConditions -> PointOfInterest
    point_of_interest = relationship(
        "PointOfInterestClass", back_populates="condition_association")
    # association between PointOfInterestConditions -> Condition
    condition = relationship(
        "Condition", back_populates="point_of_interest_association")
