from rest_framework import viewsets
from offices.serializers.suboffice_serializer import SubOfficeSerializer

class SubOfficeViewSet(viewsets.ModelViewSet):
    serializer_class = SubOfficeSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()