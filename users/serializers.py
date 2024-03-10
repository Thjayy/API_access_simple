from rest_framework import serializers
from .models import User, UZBEKISTAN, KAZAKHSTAN, RUSSIA, USA, SOUTH_KOREA
from .utils import check_phone_country
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