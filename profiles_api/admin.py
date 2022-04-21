from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile) # registering UserProfile model to the admin site to access it
admin.site.register(models.ProfileFeedItem)

