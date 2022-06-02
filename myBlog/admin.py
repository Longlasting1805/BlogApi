from django.contrib import admin

# Register your models here.
import blogApi
from myBlog.models import Blog

admin.site.register(Blog)

