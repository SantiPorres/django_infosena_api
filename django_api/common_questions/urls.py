from django.urls import path
from .views import CommonQuestionsList


urlpatterns = [
    path('', CommonQuestionsList.as_view())
]