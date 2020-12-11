from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.
def index(request):
    if len(Car.objects.all()) == 0:
        make_dummy_car()
    res = Car.objects.all()[0]
    return HttpResponse("car: {}".format(res))

def make_dummy_car():
    c = Car(make="Ford", model="F150", color="grey", price=50000.00)
    c.save()