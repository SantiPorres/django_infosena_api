from django.db import models
from .utils.base_model import AbstractModel  # inheit class for aditional functionalities
from slugify import slugify

class TypeProgram(models.Model):
    
    class Type(models.TextChoices):
        TECHNICAL = 'técnico', 'Técnico'
        TECHNOLOGIST = 'tecnólogo', 'Tecnólogo'
        OPERATOR = 'operario', 'Operario'
        SPECIALIZATION = 'especialización', 'Especialización'
        ASSISTANT = 'auxiliar', 'Auxiliar'
        
    type_program = models.CharField(verbose_name = "tipo de programa", max_length = 15, choices = Type.choices, unique = True)
    
    class Meta:
        verbose_name = "tipo de programa"
        verbose_name_plural = "tipos de programas"
        ordering = ['type_program']
    
    def __str__(self) -> str:
        return str(self.type_program)

class FormationArea(AbstractModel):
    
    # Filds or columns to database
    title: str = models.CharField(verbose_name = "nombre área", max_length = 100, unique = True, null = False, blank = False)
    # custom class to add funcionalities
    class Meta:
        verbose_name = "área formación"
        verbose_name_plural = "áreas de formación"
        ordering = ["title"]
    
    # Funtions to edition
    def save(self, *args, **kwargs):
        title = slugify(self.title)
        self.slug = title
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.title)

class Program(AbstractModel):
    program = models.CharField(verbose_name = "nombre del programa", max_length = 100, unique = True, null= False, blank= False)
    area = models.ForeignKey(FormationArea, verbose_name = "área de formación", max_length = 150, on_delete = models.CASCADE)
    type_program = models.ForeignKey(TypeProgram, verbose_name= "tipo de programa", max_length = 100, on_delete = models.CASCADE, related_name = "type_programs")
    class Meta: 
        verbose_name = "programa"
        verbose_name_plural = "programas"
        ordering = ["program"]
    
    def save(self, *args, **kwargs):
        program = slugify(self.program)
        self.slug = program
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.program)