
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from ..models import Patient, Facility


def mysql_connection():
    kenya_emr_db = mysql.connector.connect(host="127.0.0.1",  # your host
                     user="root",  # username
                     passwd="test",  # password
                     db="kenyaemr")  # db name
    try:
        connection = kenya_emr_db.cursor()
        kenya_emr_data = fetch_kenyaemr_patients(connection)
        
        return kenya_emr_data


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def fetch_kenyaemr_patients(connection):
    '''
    function to fetch data from emr
    '''
    lastupdate=None

    with open('/home/moha/healthIT/patient_registry/synch.properties', 'r') as file:
        data = file.read().replace('\n', '')
        try:
            prop=data.split("=")[0]
            if(prop=="lastupdate"):
                lastupdate=datetime.strptime(data.split("=")[1], '%Y-%m-%d %H:%M:%S')

            get_query = ''' SELECT prsn.gender, prsn.birthdate, prsn.date_changed, pname.given_name as gname,pname.middle_name mname,pname.family_name as fname,
                                                    pt.date_created,pt.voided,pt.patient_id, paddress.country, paddress.city_village, ccc.identifier
                                                    FROM person prsn inner join person_name pname on pname.person_id=prsn.person_id
                                                    inner join patient pt on pt.patient_id=prsn.person_id inner join person_address paddress on paddress.person_id=prsn.person_id 
                                                    inner join patient_identifier ccc on ccc.patient_id=prsn.person_id '''
            connection.execute(get_query)
            data = connection.fetchall()
            
            return data
        except Exception as e:
            print(e)
    

def  update_db(connection, data):
    '''
    function to update data to client registry from emr
    '''
    try:
        import pdb
        # pdb.set_trace()
        for row in data: 
            p = Patient.objects.create(gender=row[0],dob=row[1],date_updated=row[2],first_name=row[3],second_name=row[4],surname=row[5],date_created=row[6], voided=row[7],patient_id=row[8]) 
            p.save()
    except Exception as e:

        print(e)
    pass


def store_facilities(facilities_details):
    for facility in facilities_details:
        name = facility.get("official_name")
        mfl_code = facility.get("code")
        county = facility.get("county")
        sub_county = facility.get("sub_county_name")
        ward = facility.get("ward_name")
        facility_type = facility.get("facility_type_name")

        facility = Facility.objects.create(name=name,mfl_code=mfl_code,county=county,sub_county=sub_county,ward=ward,facility_type=facility_type)
        facility.save()