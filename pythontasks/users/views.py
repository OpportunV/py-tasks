from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('tasks-index')
    else:
        form = UserRegisterForm()
    content = {
        'title': 'Register',
        'form': form,
    }
    return render(request, 'users/register.html', content)