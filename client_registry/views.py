from django.shortcuts import render
# import 

def dashboard(request):
    if request.method=='GET':
        return render(request,'base.html')
    