from django.contrib import admin
from profiles.models import CustomUser, Profile, FollowRelation

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(FollowRelation)
