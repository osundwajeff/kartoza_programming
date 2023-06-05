#!/usr/bin/python3
"""Geomtetry point validator function"""


#initialize empty list
data = []

def geom_validator(lat, lon):
    """validates if geometry is valid"""

    status = False
    reason = """Latitude and Longitude must be within valid range, (Latitude[-90 to 90] and Longitude[-180 to 180])."""

    if (-90 <= lat <= 90) and (-180 <= lon <=180):
        status = True
        reason = "Latitude and Longitude is within valid range."

    if status:
        print("Point is valid")
        print(reason)
    else:
        print("Point is invalid")
        print(reason)

    data.append([lat, lon, status, reason])

def check_history():
    """returns history"""
    
    if not data:
        print("""
            ---------------
            No history yet!
            ---------------""")
    else:
        print(data)

def end_session():
    """to end the session"""
    pass

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
        #input
        print("""
            ------------------------------------
            Enter Latitude and Longitude values!
            ------------------------------------""")
        lat = float(input("Enter Latitude: "))
        lon = float(input("Enter Longitude: "))
        print("""
            ---------
            Execution!
            ---------""")
        geom_validator(lat, lon)
    elif choice == 2:
        print("""
            ------------------
            Retrieving history!
            ------------------""")
        check_history()
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
