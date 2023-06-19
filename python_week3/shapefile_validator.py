#!/usr/bin/python3
"""Shapefile Validator"""

import os
import csv
import fiona
from shapely.geometry import Point, MultiPoint, shape


class ShapefileValidatorClass:
    """shapefile validator class"""

    def __init__(self, shapefile_path):
        """initialize class"""

        self.shapefile_path = shapefile_path
        self.shapefile = fiona.open(shapefile_path)

    def validate_features(self):
        """validate features"""
        for feature in self.shapefile:
            if not isinstance(feature['geometry'], (Point, MultiPoint)):
                if not feature["geometry"]:
                    print(f"Feature {feature['id']} is invalid geometry.")
                else:
                    print(f"The geom of id {feature['id']} type is {feature['geometry'].type}.")
        pass

    def check_intersection(self):
        """Check for intersections"""

        geometry_type = self.shapefile.schema["geometry"]
        if geometry_type not in ("Point", "MultiPoint"):
            print("Intersection check is only applicable for Point or MultiPoint geometries")
            return

        intersecting_features = []
        for feature in self.shapefile:
            for other_feature in self.shapefile:
                if feature != other_feature:
                    if shape(feature["geometry"]).intersects(shape(other_feature['geometry'])):
                        intersecting_features.append(feature)

        print(f"Found {len(intersecting_features)} intersecting features")

    def remove_invalid_geometry(self, output_path):
        """Remove invalid geometry"""

        valid_features = []
        for feature in self.shapefile:
            if shape(feature["geometry"]).is_valid:
                valid_features.append(feature)

        with fiona.open(output_path, "w",
                        driver="ESRI Shapefile",
                        schema=self.shapefile.schema,
                        crs=self.shapefile.crs) as output_shapefile:
            for feature in valid_features:
                output_shapefile.write(feature)

        num_invalid_geometries = len(self.shapefile) - len(valid_features)
        print(f"Removed {num_invalid_geometries} invalid geometries")

    def remove_intersecting_geometry(self, output_path):
        """Remove intersecting geometry"""

        intersecting_features = []
        for feature in self.shapefile:
            for other_feature in self.shapefile:
                if feature["id"] != other_feature["id"]\
                    and shape(feature["geometry"])\
                        .intersects(shape(other_feature["geometry"])):
                    intersecting_features.append(feature)

        non_intersecting_features = []
        for feature in self.shapefile:
            if feature not in intersecting_features:
                non_intersecting_features.append(feature)

        with fiona.open(output_path, "w",
                        driver="ESRI Shapefile",
                        schema=self.shapefile.schema,
                        crs=self.shapefile.crs) as output_shapefile:
            for feature in non_intersecting_features:
                output_shapefile.write(feature)

        print(f"Removed {len(intersecting_features)} intersecting geometries")

    def convert_to_csv(self, output_path):
        """convert to csv"""

        if self.shapefile.schema["geometry"] != "Point":
            print("""Warning: shapefile geometry type is not Point,
                  so conversion to CSV is not applicable.""")
            return

        with open(output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for feature in self.shapefile:
                attributes = feature["properties"]
                geometry = shape(feature["geometry"])
                latitude, longitude = geometry.x, geometry.y

                writer.writerow([
                    attributes["TOWN_NAME"],
                    latitude,
                    longitude,
                    ] + list(attributes.values())[1:])

        print("Converted shapefile to CSV")


def main():
    while True:
        try:
            shapefile_path = input("\nEnter path to shapefile: ")
            shapefile_path = os.path.abspath(shapefile_path)
            shapefile_validator = ShapefileValidatorClass(shapefile_path)
            break
        except fiona.errors.DriverError:
            print("Shapefile Not Found! Please try again.\n")
            continue

    while True:
        print("""
        Menu
        1. Validate features
        2. Check intersection
        3. Remove invalid geometry
        4. Remove intersecting geometry
        5. Convert to CSV
        6. End session
        """)

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"choice: {choice}")
            shapefile_validator.validate_features()
            print("Done")
        elif choice == "2":
            print(f"choice: {choice}")
            shapefile_validator.check_intersection()
            pass
        elif choice == "3":
            print(f"choice: {choice}")
            output_path = input("Enter output: ")
            shapefile_validator.remove_invalid_geometry(output_path)
            pass
        elif choice == "4":
            print(f"choice: {choice}")
            output_path = input("Enter output: ")
            shapefile_validator.remove_intersecting_geometry(output_path)
            pass
        elif choice == "5":
            print(f"choice: {choice}")
            output_path = input("Enter output: ")
            shapefile_validator.convert_to_csv(output_path)
            pass
        elif choice == "6":
            break
        else:
            print(f"choice: {choice}")
            print("Invalid option!")


if __name__ == "__main__":
    main()
