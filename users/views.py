'''A module of users views'''
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request, *args, **kwargs):
	if request.method == 'POST':
		register_form = UserRegisterForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			username = register_form.cleaned_data.get('username')
			messages.success(request, f'Account successfully created for {username}.')
			return redirect('login')

	else:
		register_form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': register_form})

@login_required
def user_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid and p_form.is_valid:
			u_form.save()
			p_form.save()
			messages.success(request, f'Account successfully updated.')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {'u_form': u_form, 'p_form': p_form}

	return render(request, 'users/profile.html', context)
