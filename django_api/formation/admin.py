from django.contrib import admin
from .models import FormationArea,TypeProgram, Program
# Register your models here.

class EditShowModelProgram(admin.ModelAdmin):
    list_display = ('id', 'program', 'area', 'type_program')


admin.site.register(Program, EditShowModelProgram)
admin.site.register(FormationArea)
admin.site.register(TypeProgram)