from django.db import models

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from user_auth.models import User
from boomerangers.settings import AUTH_USER_MODEL

from datetime import datetime

class UserProfile(models.Model):
	#user identification data
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name = models.CharField("first name", max_length=50)
	last_name = models.CharField("last name", max_length=50)

	#contact info
	phone_number = models.CharField("phone number", max_length=11)
	
	#user address
	city = models.CharField("city", max_length=100)

	STATE_CHOICES = (
		('AL','AL'),('AK','AK'),('AZ','AZ'),('AR','AR'),('CA','CA'),('CO','CO'),('CT','CT'),('DE','DE'),('FL','FL'),('GA','GA'),('HI','HI'),('ID','ID'),('IL','IL'),('IN','IN'),('IA','IA'),
		('KS','KS'),('KY','KY'),('LA','LA'),('ME','ME'),('MD','MD'),('MA','MA'),('MI','MI'),('MN','MN'),('MS','MS'),('MO','MO'),('MT','MT'),('NE','NE'),('NV','NV'),('NH','NH'),('NJ','NJ'),
		('NM','NM'),('NY','NY'),('NC','NC'),('ND','ND'),('OH','OH'),('OK','OK'),('OR','OR'),('PA','PA'),('RI','RI'),('SC','SC'),('SD','SD'),('TN','TN'),('TX','TX'),('UT','UT'),('VT','VT'),
		('VA','VA'),('WA','WA'),('WV','WV'),('WI','WI'),('WY','WY'),
		)
	state = models.CharField("state", max_length=50, choices=STATE_CHOICES, default='AL')
	zip_code = models.CharField("zip code", max_length=5)
	
	#other user attributes
	birth_date = models.DateField(verbose_name="birth date", default=datetime.now)

	def __str__(self):
		return self.user.email

class PostDetail(models.Model):

	poster = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post_name = models.CharField("post name", max_length=50)
	post_start_date = models.DateField(verbose_name="start date", default=datetime.now)
	post_end_date = models.DateField(verbose_name="end date", default=datetime.now)	
	post_details = models.TextField("post details")
	date_posted = models.DateField(auto_now_add=False)
	#event location
	street = models.CharField("street address", max_length=100)
	city = models.CharField("city", max_length=100)

	STATE_CHOICES = (
		('AL','AL'),('AK','AK'),('AZ','AZ'),('AR','AR'),('CA','CA'),('CO','CO'),('CT','CT'),('DE','DE'),('FL','FL'),('GA','GA'),('HI','HI'),('ID','ID'),('IL','IL'),('IN','IN'),('IA','IA'),
		('KS','KS'),('KY','KY'),('LA','LA'),('ME','ME'),('MD','MD'),('MA','MA'),('MI','MI'),('MN','MN'),('MS','MS'),('MO','MO'),('MT','MT'),('NE','NE'),('NV','NV'),('NH','NH'),('NJ','NJ'),
		('NM','NM'),('NY','NY'),('NC','NC'),('ND','ND'),('OH','OH'),('OK','OK'),('OR','OR'),('PA','PA'),('RI','RI'),('SC','SC'),('SD','SD'),('TN','TN'),('TX','TX'),('UT','UT'),('VT','VT'),
		('VA','VA'),('WA','WA'),('WV','WV'),('WI','WI'),('WY','WY'),
		)
	state = models.CharField("state", max_length=50, choices=STATE_CHOICES, default='AL')
	zip_code = models.CharField("zip code", max_length=5)

	CONTINUE_POSTING = (
		('True', 'True'), ('False', 'False'), 
		)
	deactivate_post = models.CharField('remove listing', max_length=50, choices=CONTINUE_POSTING, default='False')

	def __str__(self):
		return self.post_name

class PostResponse(models.Model):
	post = models.OneToOneField(PostDetail, on_delete=models.CASCADE)

	ATTENDING_OPTIONS = (
		('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe'), ('', ''),
		)
	attending_status = models.CharField('will you be attending?', max_length=10, choices=ATTENDING_OPTIONS, default='')

	def __str__(self):
		return str(self.post) + str(' - ') + str(self.attending_status)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
		instance.userprofile.save()
