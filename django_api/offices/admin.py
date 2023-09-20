from django.contrib import admin
from offices.models import OfficesModel, SubOfficeModel

class EspecificSubOffices(admin.ModelAdmin):
    list_display = ['id', 'title', 'office']

admin.site.register(OfficesModel)
admin.site.register(SubOfficeModel, EspecificSubOffices)