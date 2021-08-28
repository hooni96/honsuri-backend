from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from django.db import IntegrityError


@permission_classes([AllowAny])
class RegisterView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    '''
    회원가입 api
    ---
    파라미터: RequestBody로 email, password, name, nickname, phone_number 등 전달
    결과: 성공시 {"message": "Register_Success"} 반환
    '''
    def post(self, request, formet=None):
        try:
            serializer = UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Register_Success"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError: 
            return Response({"message": "Nickname_Exists"}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class Login(GenericAPIView):
    serializer_class = UserLoginSerializer
    '''
    로그인 api
    ---
    파라미터: email, password
    결과: 성공 시 id, token 반환
    '''
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request_Body_Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['id'] == "None":
            return Response({"message": "Not_Matching"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(
            {
                 "id": UserSerializer(
                     user,context=self.get_serializer_context()
                 ).data.get('id'), 
                 "token": user['token']
             }
        )


@permission_classes([AllowAny])
class EmailFindView(APIView): 
    '''
    아이디 찾기 api
    ---
    파라미터: Request Body로 name, phone_number 전달
    결과: 성공시 유저 이메일 리스트 반환, 실패시 {"message": "Not_Matching"} 반환
    '''
    @swagger_auto_schema(request_body=EmailFindSerializer)
    def post(self, request):
        name = request.data['name']
        phone_number = request.data['phone_number']
        if User.objects.filter(name = name, phone_number=phone_number):
            queryset = User.objects.filter(phone_number = phone_number, name = name)
            serializer = EmailFindSerializer(queryset, many=True) 
            email_list=[]
            for each in serializer.data:
                email_list.append(each['email']) 
            return Response(email_list, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Not_Matching"}, status=status.HTTP_401_UNAUTHORIZED)