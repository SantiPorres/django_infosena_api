from rest_framework import serializers
from offices.models import OfficesModel, SubOfficeModel

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficesModel
        fields = [
            'id',
            'title',
            'description',
            'partner',
            'slug',
            'created_at',
            'updated_at'
        ]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        model = SubOfficeModel.objects.all()
        data['sub_offices'] = [
            {suboffice.title: 
                [
                    {
                        'description': suboffice.description,
                        'partner': suboffice.partner,
                        'slug': suboffice.slug,
                        'created_at': suboffice.created_at,
                        'updated_at': suboffice.updated_at
                    }
                ]
            } for suboffice in model if suboffice.office.pk == instance.pk 
        ]
        
        return data