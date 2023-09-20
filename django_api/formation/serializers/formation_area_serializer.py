from formation.models import FormationArea, Program
from rest_framework import serializers
from formation.models import TypeProgram


class FormationAreaSerializerList(serializers.ModelSerializer):
    
    class Meta:
        model = FormationArea
        fields = [
            'id',
            'title',
            'description',
            'status',
            'image',

        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['link'] = f'areas/{instance.slug}/'
        # Get info of models 
        id = instance.id
        model_program = Program.objects.filter(area = id)
        model_type_program = TypeProgram.objects.all()
        
        # Get type_programs of model type_program
        types_programs = [('tipoPrograma', i.type_program) for i in model_type_program ]
        
        # Build the serializer 
        data['tipoPrograma'] = [
                # Load the information with model and compress list 
                {key: value, 
                # Get programs and validate with respect to area
                'programas': [
                    {
                        # Get atributres for program if belongs area and type_program
                        'id': program.id,
                        'programa': program.program,
                        'link': f'areas/{instance.slug}/{program.program}'
                    } for program in model_program if value.__eq__(program.type_program.type_program)
                ]} for key, value in types_programs
            ]
        
        # Return the data with serializer 
        return data