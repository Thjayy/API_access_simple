import re
from rest_framework.validators import ValidationError


uzbekistan_regex = r'^\+998\d{9}$'
kazakhstan_regex = r'^\+7\d{10}$'
russia_regex = r'^\+7\d{10}$'
usa_regex = r'^\+1\d{10}$'
south_korea_regex = r'^\+82\d{9,10}$'

def check_phone_country(user_input):
    if re.match(uzbekistan_regex, user_input) is not None:
        return 'access with Uzbekistan phone number'
    
    elif re.match(kazakhstan_regex, user_input) is not None:
        return 'access with Kazakhstan phone number'
    
    elif re.match(russia_regex, user_input) is not None:
        return 'access with Russian phone number'
    
    elif re.match(usa_regex, user_input) is not None:
        return 'access with American phone number'
    
    elif re.match(south_korea_regex, user_input) is not None:
        return 'access with Korean phone number'
    
    else:
        data = {
            'status': False,
            'message': "Enter correct phone number"
        }
        raise ValidationError(data)