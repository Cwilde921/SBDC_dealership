from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random

from .models import Car

# Create your views here.
def index(request):
    if len(Car.objects.all()) == 0:
        make_dummy_cars(3)
    context = {
        "cars": Car.objects.all(),
    }
    template = loader.get_template("dealership/index.html")
    return HttpResponse(template.render(context, request))

def make_dummy_cars(num_cars):
    c = Car(make="Ford", model="F150", color="grey", price=50000.00)
    c.save()
    for i in range(num_cars):
        c = Car(make="Ford", model="F150", color="grey", price=random.randint(40000, 75000))
        c.save()