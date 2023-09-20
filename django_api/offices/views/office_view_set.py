from rest_framework import viewsets
from offices.serializers.office_serializer import OfficeSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    serializer_class = OfficeSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()