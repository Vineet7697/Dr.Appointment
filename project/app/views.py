from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def find_doctor(request):
    return render(request,'find_doctor.html')

def video_consult(request):
    return render(request,'video_consult.html')

def surgeries(request):
    return render(request,'surgeries.html')

def footer(request):
    return render(request,'footer.html')