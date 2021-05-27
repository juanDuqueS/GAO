from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "buildingManagement/home.html")

def reports(request):
    return render(request, "buildingManagement/reports.html")