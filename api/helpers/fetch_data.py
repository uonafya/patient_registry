from .mysql_connection import mysql_connection
from ..models import Patient




def fetch_data():
    data = mysql_connection()
    return data

def create_records(data):
    try:
        import pdb
        
        for row in data: 
            print("----------->>>>>>> ",row[11])
            
            p = Patient.objects.create(gender=row[0],dob=row[1],date_updated=row[2],first_name=row[3],second_name=row[4],surname=row[5],date_created=row[6], voided=row[7],patient_id=row[8], county=row[9],village=row[10],ccc_number=row[11]) 
            p.save()
    except Exception as e:
        print(e)
    pass
