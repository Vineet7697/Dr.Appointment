from django.shortcuts import render

# Create your views here.

def navbar(request):
    return render(request,'navbar.html')

def login(request):
    return render(request,'login.html')

def find_doctor(request):
    return render(request,'find_doctor.html')

def video_consult(request):
    return render(request,'video_consult.html')

def surgeries(request):
    return render(request,'surgeries.html')