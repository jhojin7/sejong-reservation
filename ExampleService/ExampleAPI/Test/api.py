from django.shortcuts import render
from rest_framework import generics

from .models import TestModel
from .serializers import TestModelSerializer
# Create your views here.



class TestModelList(generics.ListCreateAPIView):
    """
    TestModel을 생성 또눈 모든 TestModel을 조회 위한 뷰
    """
    queryset = TestModel.objects.all()  # 어떤 모델을 사용할지 지정
    serializer_class = TestModelSerializer  # 시리얼라이저 함수 지정


class TestModelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    특정 TestModel 조회, 수정, 삭제 위한 뷰
    """
    queryset = TestModel.objects.all()  # 어떤 모델을 사용할지 지정
    serializer_class = TestModelSerializer  # 시리얼라이저 함수 지정





