from django.urls import path
from . import views


urlpatterns = [
  path('', views.fleets, name='cars'),
  path('<int:id>/', views.fleet, name='car'),
  path('search', views.search, name='search'),
  path('add', views.regcar, name='regcar'),
  path('<int:pk>/update', views.FleetUpdate.as_view(), name='edit-car'),
  path('<int:pk>/delete', views.FleetDeleteView.as_view(), name='delete'),
  
]