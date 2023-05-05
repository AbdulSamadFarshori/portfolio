from django.contrib import admin
from .models import ContactDetail, MetaData

# Register your models here.

@admin.register(ContactDetail)
class ContactDetailAdminView(admin.ModelAdmin):

    list_display = [field.name for field in ContactDetail._meta.get_fields()]

@admin.register(MetaData)
class MetaDataAdminView(admin.ModelAdmin):

    list_display = [field.name for field in MetaData._meta.get_fields()]

