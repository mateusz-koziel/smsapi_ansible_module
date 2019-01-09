## SMSAPI - Ansible module

Module for Ansible to use with [SMSAPI](https://smsapi.pl).

### Req
Module to works require python lib; you can got it using: `pip install smsapi-python`.

### How to use
1. Check you account
``` yaml
- name: Check user account
  smsapi:
    api_key: <here-provide-your-api-token>
    state: check
```

2. Send SMS
``` yaml
- name: Send SMS
  smsapi:
    api_key: <here-provide-your-api-token>
    state: send
    to: <provide-consumer-number>
    from: <provide-sender-name-that-same-like-in-smsapi>
    message: <provide-message-content>
```