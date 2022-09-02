from django.urls import path, include
from . import views
from django_registration.backends.one_step.views import RegistrationView
from .forms import CustomUserCreationForm

urlpatterns = [
    path('register/', views.CustomRegistration.as_view(form_class=CustomUserCreationForm),
         name='django_registration_register' ),
    path('profile', views.profile, name="profile"),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]
