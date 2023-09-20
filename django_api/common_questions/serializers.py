from rest_framework import serializers
from .models import CommonQuestion


class CommonQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonQuestion
        fields = [
            'id',
            'question',
            'answer',
            'slug',
            'created_at',
            'updated_at',
        ]