from django.urls import path
from . import views

urlpatterns = [
    path('test',views.fetch_kenyaemr, name='test'),
    path('all/patients',views.all_patients, name='patients'),
    path('auth/kmhfl',views.fetch_facilities, name='kmfl'),
]