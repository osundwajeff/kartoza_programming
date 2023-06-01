#!/usr/bin/python3
"""Geomtetry point validator function"""


lat = float(input("Enter Latitude: "))
lon = float(input("Enter Longitude: "))

def geom_validator(lat, lon):
    """validates if geometry is valid"""

    status = False

    if -90 <= lat <= 90 and -180 <= lon <=180:
        status = True

    if status:
        print("Point is valid")
    else:
        print("Point is invalid")
    

    print(status)

def check_history():
    """returns history"""
    pass

def end_session():
    """to end the session"""
    pass


geom_validator(lat, lon)
