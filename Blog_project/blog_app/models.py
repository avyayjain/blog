from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_heading = models.CharField(max_length=50)
    blog_image = models.ImageField(upload_to='pics')
    blog_des = models.TextField(max_length= 1000)
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_publisher = models.CharField(max_length=20)

    
