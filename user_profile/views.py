from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from user_auth.models import User
from user_profile.forms import UserProfileForm
from user_profile.models import UserProfile

@login_required
def edit_user_profile(request):
	#editing the dashboard
	form_title = 'Submit'

	current_user = request.user
	current_user_instance = UserProfile.objects.get(user=current_user) 
	if request.method=="POST":
		form = UserProfileForm(request.POST, instance=current_user_instance, user=current_user)
		if form.is_valid():
			form.save()
			return redirect('../view')
	else:
		form = UserProfileForm(user=current_user)
	return render(request, 'user_profile/edit_user_profile.html', {'form': form,
																		'form_title': form_title,
																		'user': current_user,})




#!!!!!!!!!!! for user_profile use the edit_user_profile form just remove the button and add a link to edit, which will redirect to the form

@login_required
def user_profile(request):
	
	view_title = "profile"

	user_info = []
	current_user = request.user
	current_user_instance = UserProfile.objects.get(user=current_user)
	user_info.append(current_user_instance.first_name)
	user_info.append(current_user_instance.last_name)
	user_info.append(current_user_instance.birth_date)
	user_info.append(current_user_instance.phone_number)
	user_info.append(current_user_instance.city)
	user_info.append(current_user_instance.state)
	user_info.append(current_user_instance.zip_code)

	return render(request, 'user_profile/user_profile.html', {	'view_title': view_title,
																'user_info': user_info,})