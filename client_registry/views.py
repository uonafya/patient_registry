from django.shortcuts import render
# import 

def dashboard(request):
    if request.method=='GET':
        return render(request,'base.html')
    

def new_client(request):
    if request.method=='GET':
        return render(request,'new_client.html')

    else:
        pass