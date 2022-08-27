from django.contrib import admin
from .models import Note


# class TodoAdmin(admin.ModelAdmin):
#     list_display = ("title", "description", "completed")
    
# # Register model

admin.site.register(Note)