from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, PointOfInterestClass
from models import PointOfInterestConditionsClass
from models import PointOfInterestTypeClass
from models import Condition
import csv


connection_db = "postgresql://jeff:***@localhost/sqlalchemy"

engine = create_engine(connection_db, echo=True)

print(engine)

print("Creating tables")
Base.metadata.create_all(bind=engine)
print("Done")

with Session(engine) as session:
    point_of_interest_type = PointOfInterestTypeClass(
        name="Bridge",
        notes="Brown gate",
        image=""
        )

    condition = Condition(
        notes="Bad",
        image=""
        )

    point_of_interest = PointOfInterestClass(
        notes="",
        image="",
        height_m=2,
        # installation_date = "",
        # is_date_estimated = True,
        geometry="POINT(-1.5 36.3)"
        )

    point_of_interest_condtions = PointOfInterestConditionsClass(
        notes="Good",
        image="")

# session.expunge_all()
# session.add(point_of_interest_type)
# session.add(condition)
# session.add(point_of_interest)
# session.add(point_of_interest_condtions)

session.commit()


# query last 10 records
def show_last_10_records(session):

    last_10_records = session.query(
        PointOfInterestClass).order_by(
            PointOfInterestClass.id.desc()).limit(10).all()
    print("id, notes, image, height_m")
    for record in last_10_records:
        print(
            f"{record.id}, {record.notes}, {record.image}, {record.height_m}")


# record to update
def update_record(session):
    record_to_update = session.query(
        PointOfInterestClass).filter_by(id=2).first()
    if record_to_update:
        record_to_update.notes = "Updated note"
        session.commit()
    print("Record updated successfully.")


# delete record
def delete_record(session):
    record_to_delete = session.query(
        PointOfInterestClass).filter_by(id=1).first()
    if record_to_delete:
        session.delete(record_to_delete)
        session.commit()
    print("Record deleted successfully.")


# export as csv
def export_to_csv(session, file_path):
    records = session.query(PointOfInterestClass).all()
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'notes', 'image', 'height_m'])
        for record in records:
            writer.writerow(
                [record.id, record.notes, record.image, record.height_m])
    print("Export completed successfully.")


# import as csv
def import_from_csv(session, file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_record = PointOfInterestClass(
                notes=row['notes'],
                image=row['image'],
                height_m=float(row['height_m'])
                )
            session.add(new_record)
    session.commit()
    print("Import completed successfully.")


"""Function calls: remove '#' to use"""
# show_last_10_records(session)
# update_record(session)
# delete_record(session)
# export_to_csv(session, "output.csv")
# import_from_csv(session, "input.csv")
