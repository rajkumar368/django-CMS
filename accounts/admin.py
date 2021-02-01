from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User,Profile

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Profile)
