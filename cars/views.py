from django.shortcuts import render


def cars(request):
  return render(request, 'cars/car_lists.html', {})

def car(request, id):
  return render(request, 'cars/car_detail.html', {id:id})
