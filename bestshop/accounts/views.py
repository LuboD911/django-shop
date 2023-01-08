from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from bestshop.accounts.forms import RegisterForm, ProfileForm
from bestshop.accounts.models import Profile
from bestshop.products.models import Product


class SignUpView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login user')

class SignInView(LoginView):
    template_name = 'accounts/login.html'

def logout_user(request):
    logout(request)
    return redirect('home')

def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

        user_products = Product.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'products': user_products,
        'profile': profile,
    }

    return render(request, 'accounts/profile_details.html', context)