from datetime import datetime
import imp

import mysql.connector
from mysql.connector import Error

from random import randint

import pymysql

pymysql.install_as_MySQLdb()

def pull():
    db_kenya_emr = mysql.connector.connect(host="127.0.0.1",  
                     user="root",  
                     passwd="test",  
                     db="kenyaemr")  

    db_patient_registry = mysql.connector.connect(host="127.0.0.1",  # your host
                user="root",  # username
                passwd="test",  # password
                db="patient_registry")  # name of the database

    try:
        print("<<<<<< =================== Initiate connection ===================== >>>>>>>>>")

        cur_patient_registry = db_patient_registry.cursor()
        cur_kenya_emr = db_kenya_emr.cursor()

        records_to_transfer_sql = ''' SELECT prsn.gender, prsn.birthdate, prsn.date_changed, pname.given_name as gname,pname.middle_name mname,pname.family_name as fname,
                                                    pt.date_created,pt.voided,pt.patient_id, paddress.country, paddress.city_village, ccc.identifier, encounters.location_id
                                                    FROM person prsn inner join person_name pname on pname.person_id=prsn.person_id
                                                    inner join patient pt on pt.patient_id=prsn.person_id inner join person_address paddress on paddress.person_id=prsn.person_id 
                                                    inner join patient_identifier ccc on ccc.patient_id=prsn.person_id inner join kenyaemr.encounter encounters on encounters.patient_id=prsn.person_id '''
       
        cur_kenya_emr.execute(records_to_transfer_sql)

        data = cur_kenya_emr.fetchall()
        print("#################### insert data in client_registry ############################# ")
        for row in data:
            random_number = range(1, 100000)

            update_query="insert into api_patient(patient_id,gender,dob,first_name,second_name,surname,date_updated,voided,county,ccc_number,village,national_id,phone_number,sub_county,ward,date_created,mfl_code) VALUES ( %s,%s,%s, %s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s)"
            val =   (row[8], row[0], row[0], row[3], row[4], row[5],row[7],row[7], row[9],row[11],row[10],row[6],row[12],1, '07', 'sub_county','ward' )


            cur_patient_registry.execute(update_query,val)
            db_patient_registry.commit()




    except Exception as e:
        print(e)



pull()