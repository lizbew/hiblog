from django.contrib import admin
from .models import BlogConfig, BlogPost

# Register your models here.


admin.site.register(BlogConfig)
admin.site.register(BlogPost)