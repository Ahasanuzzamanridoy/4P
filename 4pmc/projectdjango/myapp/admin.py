from django.contrib import admin
from .models import Receivebook

# Register your models here.
admin.site.register(Receivebook)
class ReceivebookAdmin(admin.ModelAdmin):
    list_display = ('Bookid', 'Ficode', 'Date')