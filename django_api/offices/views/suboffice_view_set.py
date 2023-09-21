from rest_framework import viewsets
from offices.serializers.suboffice_serializer import SubOfficeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SubOfficeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SubOfficeSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()