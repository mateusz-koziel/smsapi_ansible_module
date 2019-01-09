from ansible.module_utils.basic import *
from smsapi.client import SmsApiPlClient


def check_points(data):
    api_key = data['api_key']

    client = SmsApiPlClient(access_token=api_key)
    
    try:
        r = client.account.balance()
        return False, False, r.points
    except:
        r = 'Something went wrong'
        return True, False, r

def send_sms(data):
    api_key = data['api_key']
    to_number = data['to']
    from_sender = data['from']
    message_ctx = data['message']

    if to_number == '':
        return True, False, 'Please provide number in TO field.'
    
    client = SmsApiPlClient(access_token=api_key)

    if from_sender != '':
        client.sms.send(to=to_number, message=message_ctx, from_=from_sender)
    else:
        client.sms.send(to=to_number, message=message_ctx)
    return False, True, 'SMS has been sent.'

def main():

    fields = {
        'api_key': {'required': True, 'type': 'str'},
        'to': {'required': False, 'type': 'str'},
        'from': {'required': False, 'type': 'str', 'default': ''},
        'message': {'required': False, 'type': 'str'},
        'state': {
            'default': 'check',
            'choices': ['check', 'send'],
            'type': 'str'
        },
    }

    choice_map = {
        'check': check_points,
        'send': send_sms
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Exit code 1', meta=result)


if __name__ == '__main__':
    main()