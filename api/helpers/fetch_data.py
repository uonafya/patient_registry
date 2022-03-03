from .mysql_connection import mysql_connection
from ..models import Patient
import requests
import json



def fetch_data():
    data = mysql_connection()
    return data

def fetch_kmhfl_facilities():
    kmhfl_token = fetch_kmhfl_token()
    print("===========>>> Tokenssssssss", kmhfl_token)
    facilities_details = get_facilities(kmhfl_token)

    store_facilities(facilities_details)

def store_facilities(facilities_details):
    for facility in facilities_details:
        county = facility.get("county")
        sub_county = facility.get("sub_county_name")
        ward = facility.get("ward_name")
        facility_name = facility.get("ward_name")
        mfl_code =

def get_facilities(kmhfl_token):
    url = "http://api.kmhfltest.health.go.ke/api/facilities/facilities/?format=json"

    payload={}
    headers = {
    'Authorization': f"Bearer {kmhfl_token}",
    'Cookie': 'csrftoken=Z1u6QtmPNZ4azfCkqaibucYj7mzhutJGDxeKzq3IZBjTHhY6yxSXlaZLBVIdNmQA'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_payload = json.loads(response.content)
    facilities_details = response_payload.get("results")

    print("###################### ",facilities_details)

    return facilities_details

def fetch_kmhfl_token():
    url = "http://api.kmhfltest.health.go.ke/o/token/"

    payload='grant_type=password&username=test%40testmail.com&password=Test%401234&scope=read&client_id=fuEOuyx3A0S3mGorbFKnuJbVliKhmsN7fbDMVQ7r&client_secret=NLOXxi7VYtrbu4RUWk0j77G9brxPPU7U4zZosnL3xhtIG1dd7usHZCWHabP9x2A6eWscU88RxcXnfHWmYFAPqhNdHl4BWe2AfaVno5r7RYXYpgQHcLu4dsQrr5TBST6w'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'csrftoken=Z1u6QtmPNZ4azfCkqaibucYj7mzhutJGDxeKzq3IZBjTHhY6yxSXlaZLBVIdNmQA'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_payload = json.loads(response.text)
    kmhf_access_token =response_payload.get("access_token")

    return kmhf_access_token



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
