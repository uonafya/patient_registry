from elasticsearch_dsl.query import Q, MultiMatch, SF
from ..documents import PatientDocument

def get_search_query(phrase):
    query = Q(
        'function_score',
        query=MultiMatch(
            fields=['first_name', 'county', 'national_id','sub_county'],
            query=phrase
        )
    )
    return PatientDocument.search().query(query)