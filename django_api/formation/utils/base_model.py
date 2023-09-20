from django.db import models

def upload_image(instance, filename):
    return f"{instance}/{filename}"

# Base class 
class AbstractModel(models.Model):
    # Clases to select option
    class Status(models.TextChoices):
        ACTIVE = "active", "Activo"
        INACTIVE = "inactive", "Inactivo"
    
    # Fields or columns to database
    description = models.TextField(verbose_name = "descripción", max_length = 250)
    status = models.CharField(verbose_name = "estado de disponibilidad", max_length = 10, choices = Status.choices, default = Status.ACTIVE)
    image = models.ImageField(verbose_name = "imagen", upload_to = upload_image, default = "default.png")
    
    # Field to search in the url
    slug = models.SlugField(db_index = True, max_length = 150, unique = True, editable = False)
    
    # Fields to register actions in the fields
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # Custom class for table current
    class Meta:
        abstract = True