from offices.models import SubOfficeModel
from rest_framework import serializers

class SubOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubOfficeModel
        fields = [
            'id',
            'title',
            'description',
            'partner',
            'slug',
            'office',
            'created_at',
            'updated_at'
        ]