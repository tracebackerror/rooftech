from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    desc = models.TextField(default="NA")
    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="NA")
    model_pic = models.ImageField(upload_to = 'images/', default = '')
    
    def image_tag(self):
        field_data = format_html("{}",    mark_safe('<img src="' + self.model_pic + '" />'),)