from rest_framework import serializers
from .models import User, UserCodeVerification, UZBEKISTAN, KAZAKHSTAN, RUSSIA, USA, SOUTH_KOREA
from .utils import check_phone_country, send_sms
from rest_framework.exceptions import ValidationError

class SignUpSerializer(serializers.ModelSerializer):
    auth_country = serializers.CharField(required=False, read_only=True)
    auth_status = serializers.CharField(required=False, read_only=True)
    
    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['phone_number'] = serializers.CharField(required=False)


    class Meta:
        model = User
        fields = ('auth_country', 'auth_status')


    def validate_phone_number(self, phone_number):
        user = User.objects.filter(phone_number = phone_number)
        if user.exists():
            data = {
                'status': False,
                'message': "The user is already provided"
            }
            raise ValidationError(data)
        return phone_number


    def validate(self, data):
        user_input = data.get('phone_country')
        phone_country = check_phone_country(user_input)
        if phone_country == 'uzbekistan':
            data = {
                'auth_country':UZBEKISTAN,
                'phone_number':user_input
            }
        elif phone_country == 'kazakhstan':
            data = {
                'auth_country':KAZAKHSTAN,
                'phone_number':user_input
            }
        
        elif phone_country == 'russia':
            data = {
                'auth_country':RUSSIA,
                'phone_number':user_input
            }
        
        elif phone_country == 'usa':
            data = {
                'auth_country':USA,
                'phone_number':user_input
            }
        
        elif phone_country == 'south_korea':
            data = {
                'auth_country':SOUTH_KOREA,
                'phone_number':user_input
            }
        
        else:
            data = {
                'status': False,
                'message': "The data you provided is incorrect"
            }
            raise ValidationError(data)
        return data
    
    def create(self, validated_data):
        user = super(SignUpSerializer, self).create(validated_data)
        auth_country = validated_data.get('auth_type')

        if auth_country == UZBEKISTAN:
            code = user.create_confirmation_code(UZBEKISTAN)
            send_sms(code)
        
        elif auth_country == KAZAKHSTAN:
            code = user.create_confirmation_code(KAZAKHSTAN)
            send_sms(code)
        
        elif auth_country == RUSSIA:
            code = user.create_confirmation_code(RUSSIA)
            send_sms(code)
        
        elif auth_country == USA:
            code = user.create_confirmation_code(USA)
            send_sms(code)
        
        elif auth_country == SOUTH_KOREA:
            code = user.create_confirmation_code(SOUTH_KOREA)
            send_sms(code)

        else:
            data = {
                'status': False,
                'message': "The code you sended is incorrect"
            }
            raise ValidationError(data)
        return user
    

    def to_representation(self, instance):
        data = super(SignUpSerializer, self).to_representation(instance)
        
        data['access'] = instance.token()['access']
        data['refresh'] = instance.token()['refresh']

        return data