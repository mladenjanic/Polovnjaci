from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegCarForm
from .models import *



def cars(request):
  return render(request, 'cars/car_lists.html', {})

def car(request, id):
  return render(request, 'cars/car_detail.html', {id:id})

def search(request):
  return render(request, 'cars/car_search.html', {})

def regcar(request):
  user = User.objects.get(id=1)
  if request.method == 'POST':
    car_form = RegCarForm(data=request.POST)
    

    if car_form.is_valid():
      cdata = car_form.cleaned_data.get
      car_selected = Car.objects.filter(name=cdata('car_select'))
      reg1 = Fleet(car_id=car_selected[0].id, obelezje=cdata('obelezje'))
      reg1.save()
    else:
      print('Invalid')
  else:
    car_form = RegCarForm(user)
  return render(request, 'cars/add_car.html', {'car_form': car_form})



