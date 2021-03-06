from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from api.views import all_patients
from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from api.serializers import FacilitySerializer
from api.models import Patient, Facility
from .helpers.org_units import get_org_units
from .forms import ClientForm, SearchForm
from api.models import Patient, Facility
from datetime import datetime, date
from .documents import PatientDocument
from .helpers.elastic_search import get_search_query
from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required(login_url='login')
def dashboard(request):
    if request.method=='GET':
        return render(request,'home.html')
    
@login_required(login_url='login')
def new_client(request):
    if request.method=='GET':
        form = ClientForm()
        # org_unit = get_org_units()
        import pdb
        
        context = {
            'form': form,
            # 'org_unit': org_unit
        }
        return render(request, "new_client.html", context)
    
    else:
        form = ClientForm(request.POST)
        import pdb
        # pdb.set_trace()
        if form.is_valid():
            first_name = request.POST.get('first_name')
            second_name = request.POST.get('second_name')
            surname = request.POST.get('surname')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            county = request.POST.get('county')
            sub_county = request.POST.get('sub_county')
            ward = request.POST.get('ward')
            national_id = request.POST.get('national_id')
            phone_number = request.POST.get('phone_number')
            ccc_number = request.POST.get('ccc_number')
            village = request.POST.get('village')
            date_created = date.today()
            # facility = request.POST.get('facility')
            

            patient = Patient(
                first_name=first_name,
                second_name=second_name, 
                surname=surname,
                gender=gender, 
                dob=dob, 
                county=county,
                sub_county=sub_county, 
                ward=ward, 
                national_id=national_id,
                ccc_number=ccc_number, 
                date_created=date_created, 
                village=village,
                # facility=facility,
                phone_number=phone_number
                )
            patient.save()

            return redirect('add_new_client')

        return render(request, "new_client.html", {'form': form})

@login_required(login_url='login')
def list_clients(request):
    all_patients=""

    if "all_patients" not in cache:
        print("--------------->>>>>>>>>> ")
        all_patients = Patient.objects.all()

        cache.set("all_patients",all_patients, timeout=settings.CACHE_TIME_OUT)
    else:
        all_patients = cache.get("all_patients")

    paginator = Paginator(all_patients, 40)


    if request.method == 'GET':
        page = request.GET.get('page', 1)
        try:
            patients = paginator.page(page)
        except PageNotAnInteger:
            patients = paginator.page(1)
        except EmptyPage:
            patients = paginator.page(paginator.num_pages)
        context = {
            'patients': patients,
        }
        return render(request, 'all_patients.html', context)


@login_required(login_url='login')
def main_search(request):
    # https://apirobot.me/posts/django-elasticsearch-searching-for-awesome-ted-talks

    if request.method == 'GET':
        form = SearchForm()
        messages.success(request, 'Zero records Found!')

        return render(request, 'search.html',{'form': form})
    else:
        keyword=request.POST.get("keyword")
        patients_deatils = get_search_query(keyword).to_queryset()

        context = {
            'patients':patients_deatils,
        }

        return render(request, 'search.html', context)


@api_view(['GET'])
def fetch_sub_counties(request):
    if request.method == 'GET':
       county_name = request.GET['county_name']
       sub_counties_details = Facility.objects.filter(county=county_name).values('sub_county').distinct()
       serializer = FacilitySerializer(sub_counties_details, many=True)
       sub_counties_array = []
       for sub_county in serializer.data:
            sub_county = sub_county['sub_county']
            sub_counties_array.append(sub_county)

       return_message = {
                "data": sub_counties_array
            }

       return Response(return_message, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_wards(request):
    if request.method == 'GET':
       sub_county_name = request.GET['sub_county_name']
       sub_counties_details = Facility.objects.filter(sub_county=sub_county_name).values('ward').distinct()
       serializer = FacilitySerializer(sub_counties_details, many=True)
       wards_array = []
       import pdb
       for single_wards in serializer.data:
           
            wards = single_wards['ward']
            wards_array.append(wards)
    #    pdb.set_trace()
       return_message = {
                "data": wards_array
            }

       return Response(return_message, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_facility(request):
    if request.method == 'GET':
       ward_name = request.GET['ward']
       sub_counties_details = Facility.objects.filter(ward=ward_name).values('name').distinct()
       serializer = FacilitySerializer(sub_counties_details, many=True)
       facility_array = []
       import pdb
       for facility in serializer.data:
           
            wards = facility['name']
            facility_array.append(wards)
       return_message = {
                "data": facility_array
            }

       return Response(return_message, status=status.HTTP_200_OK)


from django.contrib.auth import get_user_model

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # import pdb
        # pdb.set_trace()
        if user is not None:
            login(request, user)
            messages.success(request, 'logged in successfully')
            return redirect('home')
        else:
            messages.success(request, 'Incorect username/password')
            return redirect('login')

    else:  # Get method ->
        # check if test user exists
        User = get_user_model()
        if User.objects.filter(username='test').exists():
            return render(request, 'accounts/login.html')
        # if test user does not exist, create user
        else:
            user = User.objects.create_user(
                first_name='test',
                last_name='user',
                username='test',
                password='test',
                email='test@covid.com',
                facility_code=10017,
                is_staff=True,
                is_admin=True,
            )
            user.save()
            return render(request, 'accounts/login.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request, 'logged out successfully!')
    return redirect('login')

@login_required(login_url='login')
def edit_patient(request, pk):
    if request.method == 'GET':
        patient = Patient.objects.get(id=pk)

        context = {'patient': patient}
        import pdb
        return render(request, 'edit_patient.html', context)

    else:
        form = ClientForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            second_name = request.POST.get('second_name')
            surname = request.POST.get('surname')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            county = request.POST.get('county')
            sub_county = request.POST.get('sub_county')
            ward = request.POST.get('ward')
            national_id = request.POST.get('national_id')
            phone_number = request.POST.get('phone_number')
            ccc_number = request.POST.get('ccc_number')
            village = request.POST.get('village')
            date_created = date.today()
            

            patient = Patient(
                first_name=first_name,
                second_name=second_name, 
                surname=surname,
                gender=gender, 
                dob=dob, 
                county=county,
                sub_county=sub_county, 
                ward=ward, 
                national_id=national_id,
                ccc_number=ccc_number, 
                date_created=date_created, 
                village=village)
            patient.save()
        messages.success(request, 'Patient transfered successfully.')
        return redirect('all')