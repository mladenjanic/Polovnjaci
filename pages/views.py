from django.http import HttpResponse
from django.shortcuts import render

from cars.forms import SearchForm
from cars.models import User


# Create your views here.
def index(request):
    user = User.objects.get(pk=1)
    car_form = SearchForm()
    return render(request, "pages/index.html", {"car_form": car_form})


def about(request):
    return render(request, "pages/about.html", {})
