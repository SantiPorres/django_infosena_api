from rest_framework import routers
from django.urls import path, include

from formation.views.formation_area_views import FormationAreaViewSet
from formation.views.program_views import ProgramViewSet

router = routers.DefaultRouter()
router.register(r'areas', FormationAreaViewSet, basename = "formation-area")
router.register(r'programas', ProgramViewSet, basename='program')



urlpatterns = [
    path('', include(router.urls), name = 'areas')
]

