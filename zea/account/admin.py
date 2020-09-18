from django.contrib import admin
from .models import ProfileMer
from .models import ProfileStu

# Register your models here.
admin.site.register(ProfileStu)
admin.site.register(ProfileMer)