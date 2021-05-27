from .views import stock
from django.contrib import admin
from  .models import *

# Register your models here.

class stockAdmin(admin.ModelAdmin):
    readonly_fields = ("createdAt", "updatedAt")

admin.site.register(Stock, stockAdmin)
admin.site.register(Providers, stockAdmin) ## Ver video 32 