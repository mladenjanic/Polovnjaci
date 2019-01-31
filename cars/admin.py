from django.contrib import admin
from .models import Brand, Car, Fleet, User
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'get_full_name', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',  'location', 'address', 'zipcode', 'phone')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CarAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'brand')
  list_display_links = ('id', 'name', 'brand')
  list_filter = ('brand',)
  ordering = ('name',)
  search_fields = ('name', 'brand__company_name')
  list_per_page = 25

class BrandAdmin(admin.ModelAdmin):
  ordering = ('company_name',)



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Fleet)
admin.site.register(User, UserAdmin)




