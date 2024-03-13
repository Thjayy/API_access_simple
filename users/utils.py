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
    

class SmsThread(threading.Thread):
    def __init__(self, sms):
        self.sms = sms
        super(SmsThread, self).__init__()

    def run(self):
        send_message(self.sms)
        
def send_message(message_text):
    url = f'https://api.telegram.org/bot6523801257:AAEzDTJ4RlWL_m-IpJLBCSfhcgZkh-Tk9_M/sendMessage'
    params = {
        'chat_id':"765001726",
        'text':message_text,
    }
    response = requests.post(url, data=params)
    return response.json()

def send_sms(sms_text):
    sms_thread = SmsThread(sms_text)
    sms_thread.start()
    sms_thread.join()