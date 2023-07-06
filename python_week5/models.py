#!/usr/bin/python3
"""Models class"""

import sqlalchemy
from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey, String, Column, Integer, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from geoalchemy2 import Geometry
from sqlalchemy import UUID, Boolean, Date


class Base(DeclarativeBase):
    pass


class PointOfInterestTypeClass(Base):
    __tablename__ = "point_of_interest_type"
    
    id = Column(Integer, primary_key=True)
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
    
    def __init__(self, name,notes, image):
        """initialize function"""
        #self.id = id
        self.name = name
        self.notes = notes
        self.image = image
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    pass


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

    # many-to-many relationship to Condition,
    # bypassing the `PointOfInterestConditionsClass'
    condition_as: Mapped[List["Condition"]] = relationship(
        secondary="point_of_interest_conditions",
        back_populates="point_of_interest_as"
        )

    # association between PointOfInterestClass -> PointOfInterestConditionClass
    # -> PointOfInterestClass
    condition_association: Mapped[List["PointOfInterestConditionsClass"]] = relationship(
        "PointOfInterestConditionsClass",
        back_populates="point_of_interest"
        )

    """Points of interest class"""
    def __init__(self, notes,
                 height_m, image, geometry):
        """initialize function"""
        self.notes = notes
        self.height_m = height_m
        self.image = image
        self.geometry = geometry
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    pass


class Condition(Base):
    __tablename__ = "condition"
    
    #TODO class instances
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
    point_of_interest_association: Mapped[List["PointOfInterestConditionsClass"]] = relationship(
        "PointOfInterestConditionsClass",
        back_populates="condition"
        )

    def __init__(self,notes, image):
        """initialize function"""
        #self.id = id
        self.notes = notes
        self.image = image
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    pass


class PointOfInterestConditionsClass(Base):
    __tablename__ = "point_of_interest_conditions"
    
    date = Column(Date, primary_key=True)
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
    point_of_interest = relationship("PointOfInterestClass", back_populates="condition_association")
    # association between PointOfInterestConditions -> Condition
    condition = relationship("Condition", back_populates="point_of_interest_association")
    
    def __init__(self, notes, image):
        """initialize function"""
        #self.id = id
        self.notes = notes
        self.image = image
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    pass
