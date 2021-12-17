from django.contrib import admin
from .models import Blog

# Register your models here.

@admin.register(Blog)
class Blog_Admin(admin.ModelAdmin):
    list_display = ['blog_heading','blog_image','blog_des','blog_date','blog_publisher']
