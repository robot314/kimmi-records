from django.contrib import admin
from .models import Studio

# Register your models here.
class StudioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Studio, StudioAdmin)