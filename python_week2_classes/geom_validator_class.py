#!/usr/bin/python3
"""Geometry validator class"""

import sys
import time
import random


class PointValidator():
    """Validator class"""
    def __init__(self, lat, lon, data=[]):
        self.lat = lat
        self.lon = lon
        self.data = data

    def geom_validator(self, status, reason):
        self.status = status
        self.reason = reason

        status = False
        reason = """Latitude and Longitude must be within valid range
        (Latitude[-90 to 90] and Longitude[-180 to 180])"""

        if (-90 <= self.lat <= 90) and (-180 <= self.lon <= 180):
            status = True
            reason = "Latitude and Longitude is within valid range"

        if status:
            slow_print("Point is valid")
            slow_print(reason)
        else:
            slow_print("Point is invalid")
            slow_print(reason)

        self.data.append([self.lat, self.lon, status, reason])

    def check_history(self):
        """returns history"""

        if not self.data:
            slow_print("""
                ---------------
                No history yet!
                ---------------""")
        else:
            no_of_items = len(self.data)
            slow_print(f"Number of points: {no_of_items}")
            for y in self.data:
                print(y)

    def export_history(self, filename):
        """exports history"""
        with open(filename, "w") as f:
            for y in self.data:
                f.write(str(y) + "\n")

    def read_history(self, filename):
        """reads history from file"""
        with open(filename, "r") as f:
            for line in f:
                slow_print(str(line))
                self.data.append(eval(line))


# custom print
typing_speed = 50  # wpm


def slow_print(t):
    """custom print function"""
    for ch in t:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')


active_session = True

while active_session:
    print("""
        ------------------
        |      Menu      |
        ------------------
            1. Validate Point
            2. Check History
            3. Export History
            4. Read History
            5. End
            """)
    try:
        choice = int(input("Enter choice:"))

        if choice == 1:
            # input
            print("""
                ------------------------------------
                Enter Latitude and Longitude values!
                ------------------------------------""")
            while True:
                try:
                    lat = float(input("Enter Latitude: "))
                    break
                except ValueError:
                    print("""
                        Kindly enter number only!""")
                continue

            while True:
                try:
                    lon = float(input("Enter Longitude: "))
                    break
                except ValueError:
                    print("""
                        Kindly enter number only!""")
                continue

            validator = PointValidator(lat, lon)

            slow_print("""
                ---------
                Execution!
                ---------""")
            validator.geom_validator(True, "Valid")

        elif choice == 2:
            slow_print("""
                ------------------
                Retrieving history!
                ------------------""")
            validator = PointValidator(lat=None, lon=None)
            validator.check_history()

        elif choice == 3:
            slow_print("""
                ------------------
                Exporting History To File!
                ------------------""")
            validator = PointValidator(lat, lon)
            now = time.localtime()
            filename = (f"point-{now.tm_year}.{now.tm_mon:02d}.{now.tm_mday}-{now.tm_hour:02d}.{now.tm_min:02d}.{now.tm_sec:02d}")
            validator.export_history(filename)
            slow_print(f"""
                Exported to File: {filename}""")

        elif choice == 4:
            slow_print("""
                ------------------
                Reading History From File!
                ------------------""")
            validator = PointValidator(lat=None, lon=None)
            filename = input("Enter filename: ")
            validator.read_history(filename)
            slow_print(f"""
            Read File: {filename}""")

        elif choice == 5:
            slow_print("""
                ---------------
                Ending session!
                ---------------""")
            break
        else:
            print("""
                -----------------------
                Command does not exist!
                -----------------------""")
    except ValueError:
        print("""
            Error! Input number.""")
