from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from user_auth.models import User
from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile

@login_required
def edit_user_profile(request):

	view_title = 'Set Profile'
	form_title = 'Submit'

	current_user = request.user
	current_user_instance = UserProfile.objects.get(user=current_user) 
	if request.method=="POST":
		form = UserProfileForm(request.POST, instance=current_user_instance, user=current_user)
		if form.is_valid():
			form.save()
			return redirect('../get_started')
	else:
		form = UserProfileForm(user=current_user)
	return render(request, 'user_profile/edit_user_profile.html', {	'form': form,
																	'view_title': view_title,
																	'current_user': current_user,
																	'form_title': form_title,
																	'user': current_user,})

@login_required
def user_profile(request):
	
	view_title = "Profile Information"

	current_user = request.user
	current_user_instance = UserProfile.objects.get(user=current_user)
	first_name = current_user_instance.first_name
	last_name = current_user_instance.last_name
	birth_date = current_user_instance.birth_date 
	phone_number = current_user_instance.phone_number
	city = current_user_instance.city
	state = current_user_instance.state
	zip_code = current_user_instance.zip_code

	return render(request, 'user_profile/user_profile.html', {	'view_title': view_title,
																'current_user': current_user,
																'first_name': first_name,
																'last_name': last_name,
																'birth_date': birth_date,
																'phone_number': phone_number,
																'city': city,
																'state': state,
																'zip_code': zip_code,})

def get_started(request):

	view_title = "Get started"

	return render(request, 'user_profile/get_started.html', {})



@login_required
def create_boomerang(request):
	
	view_title = "home"

	current_user = request.user
	current_user_instance = UserProfile.objects.get(user=current_user) 
	if request.method=="POST":
		form = PostDetailForm(request.POST, instance=current_user_instance, user=current_user)
		if form.is_valid():
			form.save()
			return redirect('../view')
	else:
		form = UserProfileForm(user=current_user)
	return render(request, 'user_profile/create_boomerang.html', {'form': form,
																		'view_title': view_title,
																		'user': current_user,})
