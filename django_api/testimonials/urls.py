from django.urls import path
from .views import TestimoniesList


urlpatterns = [
    path('', TestimoniesList.as_view())
]