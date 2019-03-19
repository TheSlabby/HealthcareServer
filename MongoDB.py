import pymongo 
import json

class Database(): 

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client["patientdatabase"]

    patientlist = [
        {
        "noah": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "High Blood Pressure",
        "Medications": "Adderall xr",
        "Blood Pressure": "98/72 mm Hg"
        },
        "sarah": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Diabetes: Type 2",
        "Medications": "Insulin",
        "Blood Pressure": "102/62 mm Hg"
        },
        "charles": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Diabetes: Type 1",
        "Medications": "Insulin",
        "Blood Pressure": "120/75 mm Hg"
        },
        "sam": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Cancer: Bone Cancer",
        "Medications": "None",
        "Blood Pressure": "82/96 mm Hg"
        },
        "john": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "High Blood Pressure",
        "Medications": "Adderall xr",
        "Blood Pressure": "130/80 mm Hg"
        },
        "sherry": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Hypertension",
        "Medications": "Diuretics",
        "Blood Pressure": "140/72 mm Hg"
        },
        "gerald": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Cancer: Leukemia",
        "Medications": "None",
        "Blood Pressure": "79/50 mm Hg"
        },
        "edna": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Cancer: Stomach, Clinical Depression",
        "Medications": "Zoloft",
        "Blood Pressure": "90/86 mm Hg"
        },
        "caroline": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Heart Attack, Cancer: Thyroid",
        "Medications": "None",
        "Blood Pressure": "99/92 mm Hg"
        },
        "fred": {
        "Doctor": "Dr. Mcgilvary",
        "Medical History": "Clotting Disorder: Deep Vein Thrombrosis",
        "Medications": "Warfarin",
        "Blood Pressure": "86/60 mm Hg"
        }
    }
    ]
    #records = collection.insert_many(patientlist)
    def getData(self):   #username
        return list(self.db.Patients.find())


            
            





        






