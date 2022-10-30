from rest_framework.decorators import api_view
import datetime
from django.contrib import messages,auth
from .authentication import create_access_token,create_refresh_token, JWTAuthentication,decode_refresh_token
from rest_framework import status,exceptions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import Account, UserToken
from .serializers import RegisterSerializer


# @api_view(['POST'])
# def registeruser(request):
#     data = request.data
#     print(data)
#     try:
#         print('rajaaaa')
#         user = Account.objects.create(
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             email=data['email'],
#             phone_number=data['phone_number'],
#             password=make_password(data['password'])
#         )
        
#         serializer = RegisterSerializer(user,many=False)
#         return Response(serializer.data)
#     except :
#         message = {'detail':'User with this email already exist'}
#         return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def registeruser(request):
# try:
    data=request.data
    first_name=data['first_name']
    last_name=data['last_name']
    email=data['email']
    phone_number=data['phone_number'],
    password=data['password']
    confirm_password=data['confirm_password']

    # validatations for blank
    if email=='' or last_name=='' or first_name ==''  or password=='' or confirm_password=='':
        message={'error':' fill the blanks'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    # validation for password matching
    elif password!=confirm_password:
        message={'error':'password miss match'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    # for password length check
    elif len(password)<6:
        message={'error':'password contain min 6 charector'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
    # checking the email is already exist or not
    elif Account.objects.filter(email=email).exists():
        message={'error':'This email is already exist'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
        
    # creating a object of Account model for signup 
    user=Account.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        password=make_password(password),                    
    )
    serializere=RegisterSerializer(user,many=False)
    return Response(serializere.data)
# except:
    message={'error':'there is a error occure'}
    return Response(message,status=status.HTTP_400_BAD_REQUEST)

# user login
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Account.objects.filter(email=email).first()

        if user is None:
            response = Response()
           
            response.data={
                'message':'Invalid email'
            }
            return response        

        if not user.check_password(password):
            response = Response()
           
            response.data={
                'message':'invalid password'
            }
            return response        

        user = auth.authenticate(email=email, password=password)
        if user:
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)

            UserToken.objects.create(
                user_id=user.id,
                token=refresh_token,
                expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
            )

            response = Response()
            response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
            response.data = {
                'token': access_token
            }
            return response
        else:
            response = Response()
            response.data={
                'message':'Not verifyde'
            }
            return response  

# jwt refresh token
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
            user_id=id,
            token=refresh_token,
            expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists():
            raise exceptions.AuthenticationFailed('unauthenticated')

        access_token = create_access_token(id)

        return Response({
            'token':access_token
        })

#user data view by user
class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        return Response(RegisterSerializer(request.user).data)
        
# user logout
class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token=request.COOKIES.get('refresh_token')
        UserToken.objects.filter(token=refresh_token).delete()
        
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data={
            'message':'logout'
        }
        return response 

