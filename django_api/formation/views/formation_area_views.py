from formation.serializers.formation_area_serializer import FormationAreaSerializerList
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FormationAreaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Support Serializer 
    serializer_class = FormationAreaSerializerList
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    
    # Complement for administration of model ViewSet
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status = "active")
