from .serializers import AddressSerializer
from accounts.authentication import JWTAuthentication
from rest_framework import viewsets
from .models import Address
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def addAddress(request):
    data = request.data
    print(data)
    try:
        print('its add address')
        print(request.user)
        address = Address.objects.create(
            Full_name = request.data['Full_name'],
            address_1 = request.data['address_1'],
            address_2 = request.data['address_2'],
            zip_code = request.data['zip_code'],
            district = request.data['district'],
            city = request.data['city'],
            country = request.data['country'],
            latitude = request.data['latitude'],
            longitude = request.data['longitude'],
            user=request.user
        )

        serializer = AddressSerializer(address,many=False)
        
        message = {'detail':'Address posted Successfuly'}
        return Response(serializer.data)
    except :
        message = {'detail':'something weong!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def address_view_by_user(request):
    try:
        user = request.user
        address = Address.objects.filter(user=user)
        serializer = AddressSerializer(address,many=True)
        return Response(serializer.data)
    except:
        message = {'detail':'somthing is wrong'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST) 