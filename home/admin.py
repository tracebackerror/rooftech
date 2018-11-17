from django.contrib import admin

# Register your models here.

from .models import Contact, Project

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','desc')
    
admin.site.register(Contact, ContactAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','model_pic')
    fields = ('title','description', 'model_pic')
    
    
admin.site.register(Project, ProjectAdmin)