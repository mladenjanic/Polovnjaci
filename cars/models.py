from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


# class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   location = models.CharField(max_length=100, blank=True)
#   address = models.CharField(max_length=100, blank=True)
#   zipcode = models.PositiveIntegerField(blank=True)
#   phone = models.CharField(max_length=15, blank=True)
#   is_staff = models.BooleanField(default=False)

#   def __str__(self):
#     return self.user.username


class UserManager(BaseUserManager):
  def create_user(self, email, password=None, is_active=True, is_staff=False,       is_admin=False):
    if not email:
      raise ValueError("Mora biti uneta email adresa")
    if not password:
      raise ValueError("Mora biti uneta sifra")
    user_obj = self.model(
      email = self.normalize_email(email)
    )
    user_obj.set_password(password)
    user_obj.staff = is_staff
    user_obj.admin = is_admin
    user_obj.active = is_active
    user_obj.save(using=self._db)
    return user_obj

  def create_staffuser(self, email, password=None):
    user = self.create_user(
      email,
      password=password,
      is_staff=True
    )
    return user

  def create_superuser(self, email, password=None):
    user = self.create_user(
      email,
      password=password,
      is_staff=True,
      is_admin=True
    )
    return user



class User(AbstractBaseUser):
  email = models.EmailField(max_length=100, unique=True)
  location = models.CharField(max_length=100, blank=True, null=True)
  first_name = models.CharField(max_length=100, blank=True, null=True)
  last_name = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=100, blank=True, null=True)
  zipcode = models.PositiveIntegerField(blank=True, null=True)
  phone = models.CharField(max_length=15, blank=True, null=True)
  active = models.BooleanField(default=True)
  staff = models.BooleanField(default=False)
  admin = models.BooleanField(default=False)

  objects = UserManager()


  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email

  if first_name and last_name:
    def get_full_name(self):
      return '{0} {1}'.format(self.first_name, self.last_name)
  

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  @property
  def is_staff(self):
    return self.staff

  @property
  def is_active(self):
    return self.active

  @property
  def is_admin(self):
    return self.admin

  





  



class Brand(models.Model):
  company_name = models.CharField(max_length=200, blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.company_name

class Car(models.Model):
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, blank=True, null=True)

  def brand_name(self):
    return self.brand.company_name

  def __str__(self):
    return self.name

class Fleet(models.Model):

  KAROSERIJA = (
    ('Limuzina', 'Limuzina'),
    ('Hečbek', 'Hečbek'),
    ('Karavan', 'Karavan'),
    ('Kupe', 'Kupe'),
    ('Monovolumen', 'Monovolumen'),
    ('Kabriolet', 'Kabriolet'),
  )

  GORIVO = (
    ('Dizel', 'Dizel'),
    ('Benzin', 'Benzin'),
    ('Benzin + TNG', 'Benzin + TNG'),
    ('Metan CNG', 'Metan CNG'),
    ('Hibrid', 'Hibrid'),
  )

  BROJ_VRATA = (
    ('2/3', '2/3'),
    ('4/5', '4/5'),
  )

  BROJ_SEDISTA = (
    ('2 sedista', '2 sedista'),
    ('3 sedista', '3 sedista'),
    ('4 sedista', '4 sedista'),
    ('5 sedista', '5 sedista'),
    ('6 sedista', '6 sedista'),
    ('7 sedista', '7 sedista'),
    ('8 sedista', '8 sedista'),
  )

  MENJAC = (
    ('Manuelni 4 brzine', 'Manuelni 4 brzine'),
    ('Manuelni 5 brzina', 'Manuelni 5 brzina'),
    ('Manuelni 6 brzina', 'Manuelni 6 brzina'),
    ('Poluautomatski', 'Poluautomatski'),
    ('Automatski', 'Automatski'),
  )

  KLIMA = (
    ('Nema klimu', 'Nema klimu'),
    ('Manuelna klima', 'Manuelna klima'),
    ('Automatska klima', 'Automatska klima'),
  )

  brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
  car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  obelezje = models.CharField(max_length=200)
  cena = models.PositiveIntegerField()
  opis = models.TextField(blank=True)
  photo1 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo2 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo3 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo4 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo5 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo6 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo7 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  photo8 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True, default='no_photo.png')
  oglas_postavljen = models.DateTimeField(default=datetime.now)
  # Osnovne Informacije
  godiste = models.PositiveIntegerField()
  karoserija = models.CharField(max_length=200, choices=KAROSERIJA)
  gorivo = models.CharField(max_length=200, choices=GORIVO)
  kubikaza = models.PositiveIntegerField()
  # Karakteristike
  snaga_kw = models.PositiveIntegerField()
  kilometraza = models.PositiveIntegerField()
  broj_vrata = models.CharField(max_length=200, choices=BROJ_VRATA)
  broj_sedista = models.CharField(max_length=200, choices=BROJ_SEDISTA)
  menjac = models.CharField(max_length=200, choices=MENJAC)
  boja = models.CharField(max_length=100)
  klima = models.CharField(max_length=100, choices=KLIMA)
  registrovan_do = models.DateField()
  # Sigurnost
  abs = models.BooleanField(default=False)
  esp = models.BooleanField(default=False)
  airbag_vozac = models.BooleanField(default=False)
  airbag_suvozac = models.BooleanField(default=False)
  alarm = models.BooleanField(default=False)
  centralno_zakljucavanje = models.BooleanField(default=False)
  # Opema
  tempomat = models.BooleanField(default=False)
  putni_racunar = models.BooleanField(default=False)
  metalik_boja = models.BooleanField(default=False)
  navigacija = models.BooleanField(default=False)
  svetla_za_maglu = models.BooleanField(default=False)
  siber = models.BooleanField(default=False)
  alu_felne = models.BooleanField(default=False)
  dpf = models.BooleanField(default=False)
  kuka = models.BooleanField(default=False)
  kamera = models.BooleanField(default=False)

  def get_absolute_url(self):
    return "/cars/%i/" % self.id

  def car_name(self):
    return self.car.name

  def brand(self):
    return self.car.brand.company_name


  def snaga_ks(self):
    return self.snaga_kw * 1.36

  def __str__(self):
    return self.car.brand.company_name + ' ' + self.car.name + ' ' + self.obelezje















