from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, UpdateAPIView ,DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


#Create your views here.

# 회원가입
class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [
        AllowAny
    ]


# 회원정보 수정
class UpdateInfoView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'



class DeleteView(DestroyAPIView):
    permission_classes = [
        AllowAny
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer



