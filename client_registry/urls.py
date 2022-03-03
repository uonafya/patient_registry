from django.urls import path
from . import views

urlpatterns = [
    path('home',views.dashboard, name='home'),
    path('client/add/client', views.new_client, name="add_new_client")
]