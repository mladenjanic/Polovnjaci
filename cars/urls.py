from django.urls import path
from . import views


urlpatterns = [
  path('', views.fleets, name='cars'),
  path('<int:fleet_id>', views.fleet, name='car'),
  path('search', views.search, name='search'),
  path('add', views.regcar, name='regcar'),
  
]