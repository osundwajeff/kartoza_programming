#!/usr/bin/python3
"""Geometry validator class"""


class ValidatorClass():
    """Validator class"""
    def __init__(self, lat, lon, data = []):
        self.lat = lat
        self.lon = lon
        self.data = data
        
        
    def geom_validator(self, status, reason):
        self.status = status
        self.reason = reason
        
        status = False
        reason = """Latitude and Longitude must be within valid range (Latitude[-90 to 90] and Longitude[-180 to 180])"""

        if (-90 <= self.lat <= 90) and (-180 <= self.lon <= 180):
            status = True
            reason = "Latitude and Longitude is within valid range"

        if status:
            print("Point is valid")
            print(reason)
        else:
            print("Point is invalid")
            print(reason)

        self.data.append([self.lat, self.lon, status, reason])
    
    def check_history(self):
        """returns history"""

        if not self.data:
            print("""
                ---------------
                No history yet!
                ---------------""")
        else:
            no_of_items = len(self.data)
            print(f"Number of points: {no_of_items}")
            for y in self.data:
                print(y)
    
    
active_session = True
while active_session:
    print("""
            ------------------
            |      Menu      |
            ------------------
            1. Validate Point
            2. Check History
            3. End
            """)
    choice = int(input("Enter choice:"))

    if choice == 1:
        # input
        print("""
            ------------------------------------
            Enter Latitude and Longitude values!
            ------------------------------------""")
        lat = float(input("Enter Latitude: "))
        lon = float(input("Enter Longitude: "))
            
        validator = ValidatorClass(lat, lon)
            
        print("""
            ---------
            Execution!
            ---------""")
        validator.geom_validator(True, "Valid")
    elif choice == 2:
        print("""
            ------------------
            Retrieving history!
            ------------------""")
        validator.check_history()
    elif choice == 3:
        print("""
            ---------------
            Ending session!
            ---------------""")
        break
    else:
        print("""
            -----------------------
            Command does not exist!
            -----------------------""")


#lat = float(input("Enter Latitude:"))
#lon = float(input("Enter Longitude:"))

#validator = ValidatorClass(lat, lon)

#validator.geom_validator(True, "Valid point")

#validator.check_history()

