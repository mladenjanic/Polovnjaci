from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class CustomUser(User):
  mesto = models.CharField(max_length=200)
  postanski_broj = models.PositiveIntegerField()
  adresa = models.CharField(max_length=200)
  telefon = models.PositiveIntegerField()

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
  brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
  car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
  obelezje = models.CharField(max_length=200)
  cena = models.PositiveIntegerField()
  opis = models.TextField(blank=True)
  photo1 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo2 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo3 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo4 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo5 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo6 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo7 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  photo8 = models.ImageField(upload_to='cars/%Y/%m/%d', blank=True)
  date = models.DateTimeField(default=datetime.now)
  # Osnovne Informacije
  godiste = models.PositiveIntegerField()
  karoserija = models.CharField(max_length=200)
  gorivo = models.CharField(max_length=200)
  kubikaza = models.PositiveIntegerField()
  # Karakteristike
  snaga_kw = models.PositiveIntegerField()
  kilometraza = models.PositiveIntegerField()
  broj_vrata = models.PositiveIntegerField()
  broj_sedista = models.PositiveIntegerField()
  menjac = models.CharField(max_length=100)
  boja = models.CharField(max_length=100)
  klima = models.CharField(max_length=100)
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

  def car_name(self):
    return self.car.name

  def brand(self):
    return self.car.brand.company_name

  def __str__(self):
    return self.car.brand.company_name + ' ' + self.car.name + ' ' + self.obelezje















