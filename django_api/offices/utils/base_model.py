from django.db import models
from slugify import slugify

class AbstractModel(models.Model):
    
    # Columns to database 
    title = models.CharField(verbose_name = "título del área", max_length = 100, unique = True, blank = True, null = True)
    description = models.TextField(verbose_name = "descripción", max_length = 100, null = True)
    partner = models.CharField(verbose_name = "nombre de la persona", max_length = 400, null = True)
    slug = models.SlugField(blank = True, null = True, max_length = 150, unique = True, editable=False)
    
    # aditional configuration to register actions over it 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta: 
        abstract = True
    
    def save(self, *args, **kwargs):
        name = slugify(self.title)
        self.slug = name
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.title)