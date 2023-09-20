from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Testimony
from .serializers import TestimonySerializer


class TestimoniesList(APIView):
    def get(self, request, format=None):
        testimonies = Testimony.active.all()
        serializer = TestimonySerializer(testimonies, many=True)
        return Response(serializer.data)
