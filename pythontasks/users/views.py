from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import User


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
def profile(request, id_):
    target_user = get_object_or_404(User, id=id_)
    if request.user.id == id_ or 'Admin' in [group.name for group in request.user.groups.all()]:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=target_user)
            p_form = ProfileUpdateForm(request.POST, instance=target_user.profile)
            
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Account has been updated')
                return redirect(target_user.profile.get_absolute_url())
        else:
            u_form = UserUpdateForm(instance=target_user)
            p_form = ProfileUpdateForm(instance=target_user.profile)
        context = {
            'title': target_user.username,
            'target_user': target_user,
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'users/profile.html', context)
    messages.warning(request, 'You are not allowed to go there')
    return redirect('tasks-index')


def users(request):
    if 'Admin' not in [group.name for group in request.user.groups.all()]:
        messages.warning(request, 'You are not allowed to go there')
        return redirect('tasks-index')
    users_list = User.objects.all()
    context = {
        'title': 'Users',
        'users': users_list,
    }
    return render(request, 'users/users.html', context)
