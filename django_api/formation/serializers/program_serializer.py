from formation.models import Program
from rest_framework import serializers

class ProgramSerializerList(serializers.ModelSerializer):
    
    class Meta:
        model = Program
        fields = [
            'id',
            'program',
            'description',
            'status',
            'image',
            'area',
            'type_program',
            'created_at',
            'updated_at',
        ]