from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    content = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'users/register.html', content)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
