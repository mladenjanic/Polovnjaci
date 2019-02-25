from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegCarForm, UserForm, LoginForm, SearchForm
from .models import Brand, Car, Fleet, User




def fleets(request):
  fleets = Fleet.objects.order_by('-oglas_postavljen')

  paginator = Paginator(fleets, 15)
  page = request.GET.get('page')
  paged_fleets = paginator.get_page(page)

  return render(request, 'cars/car_lists.html', {'fleets': paged_fleets})

def fleet(request, id):
  fleet = Fleet.objects.get(id=id)
  fl_user = User.objects.get(id=fleet.user_id)
  return render(request, 'cars/car_detail.html', {'fleet':fleet, 'fl_user': fl_user})

@login_required
def regcar(request):
  user = User.objects.get(pk=request.user.id)
  if request.method == 'POST':
    car_form = RegCarForm(user, request.POST, request.FILES)
    
    if car_form.is_valid():
      
      cdata = car_form.cleaned_data.get
      brand_selected = Brand.objects.filter(company_name=cdata('brand_select'))
      car_selected = Car.objects.filter(name=cdata('car_select'))
     

      reg1 = Fleet(brand_name_id=brand_selected[0].id ,car_id=car_selected[0].id, user_id=user.id, obelezje=cdata('obelezje'), cena=cdata('cena'), oglas_postavljen=cdata('oglas_postavljen'), godiste=cdata('godiste'), karoserija=cdata('karoserija'), gorivo=cdata('gorivo'), kubikaza=cdata('kubikaza'), snaga_kw=cdata('snaga_kw'), kilometraza=cdata('kilometraza'),
      broj_vrata=cdata('broj_vrata'), broj_sedista=cdata('broj_sedista'), menjac=cdata('menjac'), boja=cdata('boja'), klima=cdata('klima'), registrovan_do=cdata('registrovan_do'), abs=cdata('abs'), esp=cdata('esp'), airbag_vozac=cdata('airbag_vozac'), airbag_suvozac=cdata('airbag_suvozac'), alarm=cdata('alarm'), centralno_zakljucavanje=cdata('centralno_zakljucavanje'), tempomat=cdata('tempomat'), putni_racunar=cdata('putni_racunar'), metalik_boja=cdata('metalik_boja'), navigacija=cdata('navigacija'), svetla_za_maglu=cdata('svetla_za_maglu'), siber=cdata('siber'), alu_felne=cdata('alu_felne'), dpf=cdata('dpf'), kuka=cdata('kuka'), kamera=cdata('kamera'), photo1=cdata('photo1'), photo2=cdata('photo2'), photo3=cdata('photo3'), photo4=cdata('photo4'), photo5=cdata('photo5'), photo6=cdata('photo6'), photo7=cdata('photo7'), photo8=cdata('photo8'),  opis=cdata('opis'))
      reg1.save()
      messages.success(request, ('Uspesno ste postavili oglas!'))
      return redirect('cars')
    else:
      messages.error(request, ('Ups, doslo je do greske prilikom postavljanja oglasa!'))
  else:
    car_form = RegCarForm(user = User.objects.get(id=request.user.id))
  return render(request, 'cars/add_car.html', {'car_form': car_form})


class FleetUpdate(UpdateView):
  model = Fleet
  fields = '__all__'
  template_name = 'cars/car_edit.html'
  
class FleetDeleteView(DeleteView)  :
  model = Fleet
  template_name = 'cars/fleet_confirm_delete.html'
  success_url = reverse_lazy('cars')


def search(request):
  queryset_list = Fleet.objects.order_by('-oglas_postavljen')
  user = User.objects.get(pk=1)
  car_form = SearchForm()
  

  if 'karoserija' in request.GET:
    karoserija = request.GET['karoserija']
    if karoserija:
      queryset_list = queryset_list.filter(karoserija__exact=karoserija)
  
  if 'brand_select' in request.GET:
    brand = request.GET['brand_select']
    if brand:
      queryset_list = queryset_list.filter(brand_name__company_name=brand)

  if 'cena_do' in request.GET:
    cena_do = request.GET['cena_do']
    if cena_do:
      queryset_list = queryset_list.filter(cena__lte=cena_do)

  if 'cena_od' in request.GET:
    cena_od = request.GET['cena_od']
    if cena_od:
      queryset_list = queryset_list.filter(cena__gte=cena_od)

  if 'gorivo' in request.GET:
    gorivo = request.GET['gorivo']
    if gorivo:
      queryset_list = queryset_list.filter(gorivo__exact=gorivo)
   
  return render(request, 'cars/car_search.html', {'car_form': car_form, 'fleets': queryset_list})



@login_required
def profile(request, id):
  fleets = Fleet.objects.filter(user_id=request.user.id)
  return render(request, 'account/profile.html', {'fleets': fleets})


def register_user(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST)
    
    if user_form.is_valid():
      user_form.save()
      messages.success(request, ('Uspesno ste kreirali nalog!'))
      return redirect('login')
    else:
      messages.error(request, ('Please correct the error below.'))
  else:
    user_form = UserForm()
  return render(request, 'registration/register_user.html', {'user_form': user_form })



def edit_user(request, id):
  user = User.objects.get(id=request.user.id)

  form = UserForm(request.POST or None, instance=user)
  if form.is_valid():
    form.save()
    messages.success(request, ('Uspesno ste izmenili podatke!'))
    return redirect('profile')
  
  return render(request, 'registration/edit_user.html', {'form': form })

class UserDeleteView(DeleteView):
  model = User
  template_name = 'registration/user_delete_confirm.html'
  success_url = reverse_lazy('cars')


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
    messages.success(request, ('Uspesno ste se ulogovali!'))
    if user is not None:
      login(request, user)
      return redirect('/cars')
    else:
      messages.error(request, ('Ups! Proverite da li su uneti podaci ispravni'))
  return render(request, 'registration/login.html', context)





  






