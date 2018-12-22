from django.urls import path
from . import views


urlpatterns = [
  path('', views.cars, name='cars'),
  path('<int:id>', views.car, name='car'),
  path('search', views.search, name='search'),
  path('add', views.regcar, name='regcar')
]