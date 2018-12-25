from django.contrib import admin
from django.contrib.auth.models import User
from .models import Brand, Car, Fleet


class CarAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'brand')
  list_display_links = ('id', 'name', 'brand')
  list_filter = ('brand',)
  ordering = ('name',)
  search_fields = ('name', 'brand__company_name')
  list_per_page = 25



admin.site.register(Brand)
admin.site.register(Car, CarAdmin)
admin.site.register(Fleet)

