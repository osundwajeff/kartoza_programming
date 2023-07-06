from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, PointOfInterestClass
from models import PointOfInterestConditionsClass
from models import PointOfInterestTypeClass
from models import Condition


connection_db = "postgresql://jeff:***@localhost/sqlalchemy"

engine = create_engine(connection_db, echo=True)

print(engine)

print("Creating tables")
Base.metadata.create_all(bind=engine)
print("Done")

with Session(engine) as session:
    point_of_interest_type = PointOfInterestTypeClass(
        name = "Gate",
        notes = "Brown gate",
        image = ""
        )
    
    condition = Condition(
        notes = "Good",
        image = ""
        )
    
    point_of_interest = PointOfInterestClass(
        notes = "",
        image = "",
        height_m = 2,
        #installation_date = "",
        #is_date_estimated = True,
        geometry = "POINT(-1.4 36.3)"
        )

    
    point_of_interest_condtions = PointOfInterestConditionsClass(
        notes = "Good",
        image = "")

#session.expunge_all()
#session.add(point_of_interest_type)
#session.add(condition)
#session.add(point_of_interest)
#session.add(point_of_interest_condtions)

session.commit()
