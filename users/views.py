from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        
        form = UserRegisterForm()
        
    return render(
        request,
        'users/registertration.html',
        {
            'title': 'Страница регистрации',
            'form': form,
        }
        )

@login_required
def profile(request):
    if request.method =="POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        
        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')
        
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
    
    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }
    
    return render(request, 'users/profile.html', data)