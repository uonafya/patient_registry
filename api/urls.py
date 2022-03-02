from django.urls import path
from . import views

urlpatterns = [
    path('test',views.fetch_kenyaemr, name='test'),
]