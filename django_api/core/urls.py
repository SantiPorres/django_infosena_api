from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from utils.constants import TESTIMONIALS_URL, COMMON_QUESTIONS_URL


def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('', include('formation.urls'), name = "formation_area"),
    path('', include('offices.urls'), name = "offices-suboffices"),
    path(f'{TESTIMONIALS_URL}', include('testimonials.urls'), name = "testimonials"),
    path(f'{COMMON_QUESTIONS_URL}', include('common_questions.urls'), name = "common_questions"),
]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)