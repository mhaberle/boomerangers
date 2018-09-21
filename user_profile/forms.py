from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.layout import Layout, Fieldset, MultiField, Div, ButtonHolder, Submit

from .models import UserProfile, PostDetail
from user_auth.models import User

class UserProfileForm(ModelForm):

	class Meta:
		model = UserProfile
		fields = ['first_name', 'last_name', 'birth_date', 'phone_number', 'city', 'state', 'zip_code',]


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		self.helper = FormHelper()
		self.helper.form_id = 'id-UserProfileForm'
		self.helper.form_class = 'form-inline'
		self.helper.form_show_labels = False

		super(UserProfileForm, self).__init__(*args, **kwargs)

		profile_instance = UserProfile.objects.get(user=self.user)


		var_first_name = profile_instance.first_name
		if var_first_name == '':
			var_first_name = 'First name'
			var_last_name = 'Last name'
			var_phone_number = 'Phone number'
			var_city = 'City'
			var_state = 'State'
			var_zip_code = 'Zip code'

		else:
			var_first_name
			var_last_name = profile_instance.last_name

			var_phone_number = ''
			if len(profile_instance.phone_number) == 10:
				index_count = 1
				for num in profile_instance.phone_number:
					var_phone_number += num
					if index_count == 3 or index_count == 6:
						var_phone_number += '-'
					index_count += 1

			var_city = profile_instance.city
			var_state = profile_instance.state
			var_zip_code = profile_instance.zip_code

		self.helper.layout = Layout(
			Fieldset(
				'Name',
				Div(
					Field(	'first_name', placeholder=var_first_name),
					Field(	'last_name',  placeholder=var_last_name),
							css_class = "form-inline",
					)
				),
			Fieldset(
				'Birth Date',
				Div(
					Field( 'birth_date', placeholder='blank'),
							css_class = "form-inline",
					)
				),	
			Fieldset(
				'Phone Number',
				Div(
					Field(	'phone_number', placeholder=var_phone_number),
						css_class = "form-inline",
					)
				),
			Fieldset(
				'Address',
				Div(
					Field(	'city', placeholder=var_city),
							css_class = "form-inline",
					),
				Div(
					Field(	'state', placeholder=var_state),
					Field(	'zip_code', placeholder=var_zip_code),
							css_class = "form-inline",
					)
				),
		    ButtonHolder(
            	Submit('save', 'Submit', css_class='btn btn-primary btn-lg btn-block')
            ),
        )

class PostDetailForm(ModelForm):

# looks like i need to init the user that creates this instance to attach it to the model entry, i believe since i'm missing this data, it's not letting me submit the form entry
	class Meta:
		model = PostDetail
		fields = ['user', 'post_name', 'class_start_date', 'class_start_time','post_details', 'street', 'city', 'state', 'zip_code', 'remove_post',]

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		self.helper = FormHelper()
		self.helper.form_id = 'id-PostDetailForm'
		self.helper.form_class = 'form-inline'
		self.helper.form_show_labels = False

		super(PostDetailForm, self).__init__(*args, **kwargs)


		self.fields['user'].initial = self.user.user
		self.fields['remove_post'].initial = "No"

		self.helper.layout = Layout(
			Field( 'user', type='hidden'),
			Fieldset(
				'Event title',
				Div(
					Field( 'post_name', placeholder='Your event name'),
							css_class = "form-inline",
					)
				),
			Fieldset(
				'Event date',
				Div(
					Field(	'class_start_time', placeholder='Event start time', form_class="datetime-input"),
					Field(	'class_start_date', placeholder='Event start date', id="datetimepicker3"),
							css_class = "form-inline",
					)
				),
			Fieldset(
				'Event details',
				Div(
					Field( 'post_details', placeholder='Tell us about your event'),
						css_class = "form-inline",
					)
				),
			Fieldset(
				'Event location',
				Div(
					Field(	'street', css_class='post_details', placeholder='Street'),
					Field(	'city', css_class='post_details', placeholder='City'),					
							css_class = "form-inline",
					),
				Div(
					Field(	'state', placeholder='State'),
					Field(	'zip_code', placeholder='Zip code'),
							css_class = "form-inline",
					)
				),
			Fieldset(
				'Remove this post',
				Div(
					Field( 'remove_post', placeholder=''),
						css_class = "form-inline",
					)
				),
            	Submit('save', 'Submit', css_class='btn btn-primary btn-lg btn-block')
            )