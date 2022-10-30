
from asyncore import write
import email
from rest_framework import serializers
from .models import Account

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Account
        fields = '__all__'
        #['first_name','last_name','email','phone_number','password','id']
        extra_kwargs ={
            'password':{'write_only':True}
        }
        

    def save(self):
        reg=Account(
                email=self._validated_data['email']
        )
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'password':'password doses not match'})
        reg.set_password(password)
        reg.save()
        return reg