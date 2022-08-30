from django.contrib import admin
from .models import CustomUser, Ticket
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fields = ('name', 'surname', 'username', 'email', 'address', 'card_number', 'language', 'gender', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = None
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register((Ticket,))
