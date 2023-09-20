from django.urls import path, include
from offices.views.office_view_set import OfficeViewSet
from offices.views.suboffice_view_set import SubOfficeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'oficinas', OfficeViewSet, basename = "office")
router.register(r'sub-oficinas', SubOfficeViewSet, basename= "sub-office")


urlpatterns = [
    path('', include(router.urls))
]
