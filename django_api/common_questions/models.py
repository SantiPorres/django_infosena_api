from django.db import models
from utils.models import BaseModel
from uuid import uuid4


class CommonQuestion(BaseModel):
    question = models.CharField(
        max_length=120,
        unique=True,
        blank=False,
        null=False,
        default=uuid4()
    )

    answer = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        default=uuid4()
    )

    class Meta:
        verbose_name = 'common_question'
        verbose_name_plural = 'common_questions'

    def __str__(self):
        return self.question
    