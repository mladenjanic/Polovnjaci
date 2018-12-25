from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.models import User
from .forms import RegCarForm
from .models import Brand, Car, Fleet



def fleets(request):
  fleets = Fleet.objects.all()
  return render(request, 'cars/car_lists.html', {'fleets': fleets})

def fleet(request, id):
  return render(request, 'cars/car_detail.html', {id:id})

def search(request):
  return render(request, 'cars/car_search.html', {})

def regcar(request):
  user = User.objects.get(id=request.user.id)
  if request.method == 'POST':
    car_form = RegCarForm(user, request.POST)

    if car_form.is_valid():

      cdata = car_form.cleaned_data.get
      brand_selected = Brand.objects.filter(company_name=cdata('brand_select'))
      car_selected = Car.objects.filter(name=cdata('car_select'))

      reg1 = Fleet(brand_name_id=brand_selected[0].id ,car_id=car_selected[0].id, obelezje=cdata('obelezje'), cena=cdata('cena'), date=cdata('date'), godiste=cdata('godiste'), karoserija=cdata('karoserija'), gorivo=cdata('gorivo'), kubikaza=cdata('kubikaza'), snaga_kw=cdata('snaga_kw'), kilometraza=cdata('kilometraza'),
      broj_vrata=cdata('broj_vrata'), broj_sedista=cdata('broj_sedista'), menjac=cdata('menjac'), boja=cdata('boja'), klima=cdata('klima'), registrovan_do=cdata('registrovan_do'), abs=cdata('abs'), esp=cdata('esp'), airbag_vozac=cdata('airbag_vozac'), airbag_suvozac=cdata('airbag_suvozac'), alarm=cdata('alarm'), centralno_zakljucavanje=cdata('centralno_zakljucavanje'), tempomat=cdata('tempomat'), putni_racunar=cdata('putni_racunar'), metalik_boja=cdata('metalik_boja'), navigacija=cdata('navigacija'), svetla_za_maglu=cdata('svetla_za_maglu'), siber=cdata('siber'), alu_felne=cdata('alu_felne'), dpf=cdata('dpf'), kuka=cdata('kuka'), kamera=cdata('kamera'), photo1=cdata('photo1'), photo2=cdata('photo2'), photo3=cdata('photo3'), photo4=cdata('photo4'), photo5=cdata('photo5'), photo6=cdata('photo6'), photo7=cdata('photo7'), photo8=cdata('photo8'), opis=cdata('opis'))
      reg1.save()
      return redirect('cars')
    else:
      print ('Invalid')
  else:
    car_form = RegCarForm(user = User.objects.get(id=request.user.id))
  return render(request, 'cars/add_car.html', {'car_form': car_form})






