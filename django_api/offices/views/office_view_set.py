from rest_framework import viewsets
from offices.serializers.office_serializer import OfficeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OfficeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = OfficeSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()