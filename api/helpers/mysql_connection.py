
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime


def mysql_connection():
    kenya_emr_db = mysql.connector.connect(host="127.0.0.1",  # your host
                     user="root",  # username
                     passwd="test",  # password
                     db="kenyaemr")  # db name
    try:
        connection = kenya_emr_db.cursor()
        fetch_kenyaemr_patients(connection)
        # print("------------>>>>>> ",connection)


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def fetch_kenyaemr_patients(connection):
    lastupdate=None
    print("----------------->>>>>>>>>>> ")

    with open('/home/moha/healthIT/patient_registry/synch.properties', 'r') as file:
        data = file.read().replace('\n', '')
        try:
            print("----------------->>>>>>>>>>> ")
            prop=data.split("=")[0]
            print("888888888888888888",prop)
            if(prop=="lastupdate"):
                lastupdate=datetime.strptime(data.split("=")[1], '%Y-%m-%d %H:%M:%S')

            # max_lastupdate_timestamp_sql='''Select max(date_created) FROM person'''
    
            # print("==============>>> ", max_lastupdate_timestamp_sql)
            # # connection.execute(max_lastupdate_timestamp_sql)
            # for row in connection.fetchone():
            #     max_lastupdate_timestamp=row
            get_query = ''' SELECT prsn.gender, prsn.birthdate, prsn.date_changed, pname.given_name 
                                    as gname,pname.middle_name mname,pname.family_name as fname,
                                                    pt.date_changed,pt.date_created,pt.voided,pt.patient_id
                                                    FROM person prsn inner join person_name pname on pname.person_id=prsn.person_id
                                                    inner join patient pt on pt.patient_id=prsn.person_id '''
            connection.execute(get_query)
            data = connection.fetchall()
            for x in data:
                print("------------>>>> ",x)
            update_db()

            # print("==============>>>>>>> ",data)


        except Exception as e:
            print("+++++++++++++++ ",e)
    

def  update_db():
    pass