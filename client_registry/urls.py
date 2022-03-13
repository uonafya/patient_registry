from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home',views.dashboard, name='home'),
    path('client/add/client', views.new_client, name="add_new_client"),
    path('all/client/list', views.list_clients, name="list_clients"),
    path('search', views.main_search, name="main_search"),
    path('subcounty/<slug:county_name>/', views.fetch_sub_counties, name='sub_counties'),
    path('wards/<slug:sub_county_name>/', views.fetch_wards, name='wards'),
    path('facilities/<slug:ward_name>/', views.fetch_facility, name='facilities'),

    path('login/', views.user_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]