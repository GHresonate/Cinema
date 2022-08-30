from django.contrib.auth import authenticate, login
from django_registration.backends.one_step.views import RegistrationView
from .models import CustomUser
from .forms import CustomUserChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


class CustomRegistration(RegistrationView):
    success_url = '/'


def profile(request, username):
    old_user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        user = CustomUserChangeForm(request.POST, instance=old_user)
        if user.is_valid():
            user.save()
        else:
            print(user.errors)
            raise ValueError
        return HttpResponseRedirect('/')
    else:
        print(old_user)
        form = CustomUserChangeForm(instance=old_user)
        print(form)
        return render(request, 'user_app/profile.html',
                      {'form': form})
