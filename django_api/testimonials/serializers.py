from rest_framework import serializers
from .models import Testimony


class TestimonySerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimony
        fields = [
            'id',
            'testimony',
            'witness_name',
            'created_at',
            'updated_at',
            'get_image_url',
        ]