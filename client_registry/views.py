from django.shortcuts import render
from .forms import ClientForm, SearchForm
from api.models import Patient
from datetime import datetime, date
from .documents import PatientDocument

def dashboard(request):
    if request.method=='GET':
        return render(request,'home.html')
    

def new_client(request):
    if request.method=='GET':
        form = ClientForm()
        return render(request, "new_client.html", {'form': form})
    
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
            

            patient = Patient(first_name=first_name,second_name=second_name, surname=surname,gender=gender, dob=dob, county=county,
                            sub_county=sub_county, ward=ward, national_id=national_id,ccc_number=ccc_number, date_created=date_created, village=village)
            patient.save()
        return render(request, "new_client.html", {'form': form})


def list_clients(request):
    patients = Patient.objects.all()

    if request.method == 'GET':
        context = {
            'patients': patients,
        }
        return render(request, 'all_patients.html', context)

def main_search(request):

    if request.method == 'GET':
        form = SearchForm()

        return render(request, 'search.html',{'form': form})
    else:
        import pdb
        
        keyword=request.POST.get("keyword")
        # second_name=request.POST.get("first_name")
        patients = PatientDocument.search().query("match", first_name=keyword)
        patients_deatils = patients.to_queryset()
        # pdb.set_trace()

        context = {
            'patients':patients_deatils,
        }

        return render(request, 'search.html', context)
