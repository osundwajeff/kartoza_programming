#!/usr/bin/python3
"""class representation of farm table"""

from datetime import datetime
import shapely.geometry


class FenceClass:
    """fence class"""

    def __init__(self, itemId, fence_type, notes, height_m, image, geometry, fence_type_itemId):
        self.itemId = itemId
        self.notes = notes
        self.height_m = height_m
        self.image = self.image
        self.geometry = geometry
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.fence_type_itemId = fence_type_itemId


class FenceTypeClass:
    """fence_type class"""

    def __init__(self, itemId, name, notes, image):
        self.itemId = itemId
        self.name = name
        self.notes = notes
        self.image = image
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class ConditionTypeClass:
    """condition_type class"""

    def __init__(self, itemId, condition, notes, image):
        self.itemId = itemId
        self.condition = condition
        self.notes = notes
        self.image = image
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class FenceCondtionsClass:
    """fence_condtions association class"""

    def __init__(self, fence_itemId, condition_type_itemId, date):
        self.fence_itemId = fence_itemId
        self.condition_type_itemId = condition_type_itemId
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
