from formation.serializers.program_serializer import ProgramSerializerList
from rest_framework import viewsets

class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializerList
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all().filter(status = "active")