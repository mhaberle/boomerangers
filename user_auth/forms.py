from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm, HiddenInput

from user_auth.models import User

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label='Password',
		widget = forms.PasswordInput)

class UserCreationForm(forms.ModelForm):

	password1 = forms.CharField(label='Password',
		widget = forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password',
		widget = forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

	class Meta:
		model = User
		fields = ('email',)

	def clean_password(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user