from django.db import models
from .utils.base_model import AbstractModel # Get the all columns 

class OfficesModel(AbstractModel):
    
    class Meta:
        verbose_name = "ofinas"
        verbose_name_plural = "oficinas"
        ordering = ["title"]

class SubOfficeModel(AbstractModel):
    office = models.ForeignKey(OfficesModel, verbose_name = "oficinas", db_index=True, max_length=150, null= False, blank=False, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "sub oficina"
        verbose_name_plural = "sub oficinas"
        ordering = ["title", "partner"]

