from django.contrib import admin
from blog.models import post
from blog.models import Category

# Register your models here.
admin.site.register(post)
admin.site.register(Category)