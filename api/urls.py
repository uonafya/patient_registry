from django.urls import path
from . import views

urlpatterns = [
    path('test',views.fetch_kenyaemr, name='test'),
    path('all/patients',views.all_patients, name='patients'),
    path('fetch/kmhfl/facilities',views.fetch_mfl_facilities, name='get_facilities'),
    path('all/facilities',views.share_facilities, name='kmfl'),
    path('clear/cache', views.clear_cache, name='clear_cache'),
    path('subcounty/<slug:county_name>/', views.fetch_counties, name='sub_counties'),

]