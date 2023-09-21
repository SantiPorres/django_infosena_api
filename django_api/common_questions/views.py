from django.shortcuts import render
from rest_framework.views import APIView
from .models import CommonQuestion
from .serializers import CommonQuestionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommonQuestionsList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        common_questions = CommonQuestion.active.all()
        serializer = CommonQuestionSerializer(common_questions, many=True)

        return Response(serializer.data)
    