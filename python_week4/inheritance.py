#!/usr/bin/env python3
"""Inheritance class"""
from datetime import datetime


class PointsOfInterest:
    "Points of interest class"
    def __init__(self, itemId, notes,
                 height_m, image, geometry,
                 points_of_interest_type):
        """initialize function"""
        self.itemId = itemId
        self.notes = notes
        self.height_m = height_m
        self.image = image
        self.geometry = geometry
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.points_of_interest_type = points_of_interest_type

    def __str__(self):
        """__str__ function"""
        return f"""Points of Interest:
'{self.points_of_interest_type}' {self.itemId}"""

    def get_details(self):
        """get_details function"""
        return {
            "itemId": self.itemId,
            "notes": self.notes,
            "height_m": self.height_m,
            "image": self.image,
            "geometry": self.geometry,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "points_of_interest_type": self.points_of_interest_type
        }


class Bridges(PointsOfInterest):
    """Bridges class, pulls from PointsOfInterest class"""
    def __init__(self, name, location, height_m, description, lanes, material):
        """initializer"""
        super().__init__(name, location, height_m, None, None, "bridge")

    def benefit(self):
        """benefits function"""
        print(f"{self.name} supports transport systems")


class Fences(PointsOfInterest):
    """Fences class, pulls from PointsOfInterest class"""
    def __init__(self, name, location, height_m, description, material):
        """__init__ function"""
        super().__init__(name, location, height_m, None, None, "fence")

    def purpose(self):
        print(f"{self.name} acts as a boundary")


bridge = Bridges("Nyali Bridge",
                 "Mombasa, KE",
                 1.7,
                 "A suspension bridge",
                 4,
                 "Steel")
print(bridge)
print("")
# Output: Points of Interest bridge 1

details = bridge.get_details()
print(details)
print("")


fence = Fences("State House Fence",
               "Nairobi",
               7.5,
               "A security fence",
               "Concrete and electric")
print(fence)
print("")
# Output: Points of Interest fence 2

details = fence.get_details()
print(details)
