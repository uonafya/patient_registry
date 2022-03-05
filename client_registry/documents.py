from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from api.models import Patient,Facility

@registry.register_document
class PatientDocument(Document):
    class Index:
        name = 'patient'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Patient
         fields = [
             'first_name',
             'second_name',
             'ccc_number',
             'county',
             'sub_county'
         ]