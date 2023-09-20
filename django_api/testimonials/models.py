from django.db import models
from utils.models import BaseModel
from uuid import uuid4
from utils.constants import BASE_URL, TESTIMONIALS_URL


class Testimony(BaseModel):
    testimony = models.TextField(
        max_length=500,
        blank=False,
        null=False,
        default=uuid4()
    )

    witness_name = models.CharField(
        max_length=120,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to=f'{TESTIMONIALS_URL}',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'testimony'
        verbose_name_plural = 'testimonies'

    def __str__(self):
        return self.witness_name
    
    def save(self, *args, **kwargs):
        if self.witness_name == '' or self.witness_name == None:
            self.witness_name = 'anonymous'
        return super().save(*args, **kwargs)
    
    def get_image_url(self):
        if self.image:
            return f'{BASE_URL}' + self.image.url
        return ''
    