import json
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
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
  registrovan_do = forms.CharField(widget=forms.DateInput(attrs={'placeholder': 'gggg-mm-dd'}))
  
  
  
  

  brands = json.dumps(brands)
  cars = json.dumps(dcars)

  class Meta:
    model = Fleet
    fields = ['brand_select', 'car_select','brand_name', 'car', 'obelezje', 'cena', 'oglas_postavljen', 'godiste', 'karoserija', 'gorivo', 'kubikaza', 'snaga_kw', 'kilometraza', 'broj_vrata', 'broj_sedista', 'menjac', 'boja', 'klima', 'registrovan_do', 'abs', 'esp', 'airbag_vozac', 'airbag_suvozac', 'alarm', 'centralno_zakljucavanje', 'tempomat', 'putni_racunar', 'metalik_boja', 'navigacija', 'svetla_za_maglu', 'siber', 'alu_felne', 'dpf', 'kuka', 'kamera', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8','user', 'opis']
    
    

  def __init__(self, user, *args, **kwargs):
    super(RegCarForm, self).__init__(*args, **kwargs)
    if user.is_staff:
      self.fields['brand_select'].queryset = Brand.objects.filter(user=user)
    self.fields['car'].widget = forms.HiddenInput()
    self.fields['brand_name'].widget = forms.HiddenInput()
    self.initial['user'] = User.objects.get(pk=user.id)
    

class UserForm(forms.ModelForm):
  password1 = forms.CharField(label='Lozinka', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Potvrdi lozinku', widget=forms.PasswordInput)

  class Meta:
      model = User
      fields = ('email', 'first_name', 'last_name',  'location', 'address', 'zipcode', 'phone', 'password1', 'password2')

  def clean_password2(self):
    # Check that the two password entries match
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError("Passwords don't match")
    return password2

  def save(self, commit=True):
    # Save the provided password in hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit:
      user.save()
    return user


class LoginForm(forms.Form):
  username = forms.EmailField(label='Email')
  password = forms.CharField(widget=forms.PasswordInput)


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
    
      









