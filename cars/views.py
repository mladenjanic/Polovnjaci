from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegCarForm, UserForm, LoginForm
from .models import Brand, Car, Fleet, User



def fleets(request):
  fleets = Fleet.objects.order_by('-oglas_postavljen')

  paginator = Paginator(fleets, 15)
  page = request.GET.get('page')
  paged_fleets = paginator.get_page(page)

  return render(request, 'cars/car_lists.html', {'fleets': paged_fleets})

def fleet(request, fleet_id):
  fleet = Fleet.objects.get(id=fleet_id)
  return render(request, 'cars/car_detail.html', {'fleet':fleet})

def search(request):
  return render(request, 'cars/car_search.html', {})

def regcar(request):
  user = User.objects.get(pk=request.user.id)
  if request.method == 'POST':
    car_form = RegCarForm(user, request.POST, request.FILES)
    
    if car_form.is_valid():
      
      cdata = car_form.cleaned_data.get
      brand_selected = Brand.objects.filter(company_name=cdata('brand_select'))
      car_selected = Car.objects.filter(name=cdata('car_select'))
      #user = User.objects.get(pk=request.user.id)
      
     

      reg1 = Fleet(brand_name_id=brand_selected[0].id ,car_id=car_selected[0].id, user_id=user.id, obelezje=cdata('obelezje'), cena=cdata('cena'), oglas_postavljen=cdata('oglas_postavljen'), godiste=cdata('godiste'), karoserija=cdata('karoserija'), gorivo=cdata('gorivo'), kubikaza=cdata('kubikaza'), snaga_kw=cdata('snaga_kw'), kilometraza=cdata('kilometraza'),
      broj_vrata=cdata('broj_vrata'), broj_sedista=cdata('broj_sedista'), menjac=cdata('menjac'), boja=cdata('boja'), klima=cdata('klima'), registrovan_do=cdata('registrovan_do'), abs=cdata('abs'), esp=cdata('esp'), airbag_vozac=cdata('airbag_vozac'), airbag_suvozac=cdata('airbag_suvozac'), alarm=cdata('alarm'), centralno_zakljucavanje=cdata('centralno_zakljucavanje'), tempomat=cdata('tempomat'), putni_racunar=cdata('putni_racunar'), metalik_boja=cdata('metalik_boja'), navigacija=cdata('navigacija'), svetla_za_maglu=cdata('svetla_za_maglu'), siber=cdata('siber'), alu_felne=cdata('alu_felne'), dpf=cdata('dpf'), kuka=cdata('kuka'), kamera=cdata('kamera'), photo1=cdata('photo1'), photo2=cdata('photo2'), photo3=cdata('photo3'), photo4=cdata('photo4'), photo5=cdata('photo5'), photo6=cdata('photo6'), photo7=cdata('photo7'), photo8=cdata('photo8'),  opis=cdata('opis'))
      reg1.save()
      return redirect('cars')
    else:
      print ('Invalid')
  else:
    car_form = RegCarForm(user = User.objects.get(id=request.user.id))
  return render(request, 'cars/add_car.html', {'car_form': car_form})


def profile(request):
  return render(request, 'account/profile.html')




def register_user(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    
    if user_form.is_valid():
      user_form.save()
      return redirect('login')
    else:
      messages.error(request, ('Please correct the error below.'))
  else:
    user_form = UserForm()
  return render(request, 'registration/register_user.html', {'user_form': user_form })


def login_user(request):
  form = LoginForm(request.POST or None)
  context = {"form": form}

  next_ = request.GET.get('next')
  next_post = request.POST.get('next')
  redirect_path = next_ or next_post or None
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/cars')
    else:
      print("Error")
  return render(request, 'registration/login.html', context)





  






