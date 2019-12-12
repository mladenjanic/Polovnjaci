from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import Brand, Car, Fleet, User


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ("email", "get_full_name", "admin")
    list_filter = ("admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "location",
                    "address",
                    "zipcode",
                    "phone",
                )
            },
        ),
        ("Permissions", {"fields": ("admin", "staff", "active")}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand")
    list_display_links = ("id", "name", "brand")
    list_filter = ("brand",)
    ordering = ("name",)
    search_fields = ("name", "brand__company_name")
    list_per_page = 25


class BrandAdmin(admin.ModelAdmin):
    ordering = ("company_name",)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Fleet)
admin.site.register(User, UserAdmin)
