from django.contrib import admin
from .models import Texts

# Register your models here.
class TextsAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Texts, TextsAdmin)