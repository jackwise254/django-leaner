from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip
from .static import header
# Create your views here.

def index(request):
    context = {
        "trips": Trip.objects.all()
    }
    # echo 
    return render(request, 'trips/index.html', context)
