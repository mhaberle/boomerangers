from django.contrib import admin

from .models import UserProfile, PostDetail, PostResponse

admin.site.register(UserProfile)
admin.site.register(PostDetail)
admin.site.register(PostResponse)
