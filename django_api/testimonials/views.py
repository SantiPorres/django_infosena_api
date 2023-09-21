from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Testimony
from .serializers import TestimonySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TestimoniesList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        testimonies = Testimony.active.all()
        serializer = TestimonySerializer(testimonies, many=True)
        return Response(serializer.data)
