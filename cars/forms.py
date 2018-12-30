import json
from django import forms
from django.contrib.auth.models import User
from .models import *

class RegCarForm(forms.ModelForm):
  dcars = {}
  list_cars = []
  for car in Car.objects.all():
    if car.brand.company_name in dcars:
      dcars[car.brand.company_name].append(car.name)
    else:
      dcars[car.brand.company_name] = [car.name]
    list_cars.append((car.name,car.name))

  brands = [str(brand) for brand in Brand.objects.all()]
  

  brand_select = forms.ChoiceField(choices=([(brand, brand) for brand in brands]), label='')
  car_select = forms.ChoiceField(choices=(list_cars), label='')

  brands = json.dumps(brands)
  cars = json.dumps(dcars)

  class Meta:
    model = Fleet
    fields = ['brand_select', 'car_select','brand_name', 'car', 'obelezje', 'cena', 'oglas_postavljen', 'godiste', 'karoserija', 'gorivo', 'kubikaza', 'snaga_kw', 'kilometraza', 'broj_vrata', 'broj_sedista', 'menjac', 'boja', 'klima', 'registrovan_do', 'abs', 'esp', 'airbag_vozac', 'airbag_suvozac', 'alarm', 'centralno_zakljucavanje', 'tempomat', 'putni_racunar', 'metalik_boja', 'navigacija', 'svetla_za_maglu', 'siber', 'alu_felne', 'dpf', 'kuka', 'kamera', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8', 'opis']
    
    

  def __init__(self, user, *args, **kwargs):
    #user = User.objects.get(id=request.user.id)
    super(RegCarForm, self).__init__(*args, **kwargs)
    self.fields['brand_select'].queryset = Brand.objects.filter(user=user)
    self.fields['brand_name'].widget = forms.HiddenInput()
    self.fields['car'].widget = forms.HiddenInput()
    
