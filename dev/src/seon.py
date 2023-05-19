import requests
import json
from dev.src import scraper

def get_seon_fraud_score(api_key, URL):
    
    user_name = scraper.get_user_name(URL)
    
    
    headers = {
      "X-API-KEY": api_key
    }
    
    payload = {
        "config": {
            "ip": {
              "include": "flags,history,id",
              "version": "v1.1"
            },
            "email": {
              "include": "flags,history,id",
              "version": "v2.2"
            },
            "phone": {
              "include": "flags,history,id",
              "version": "v1.4"
            },
            "ip_api": True,
            "email_api": True,
            "phone_api": True,
            "device_fingerprinting": True,
        },
        "ip": "",
        "action_type": "account_register",
        "affiliate_id": "",
        "affiliate_name": "",
        "email": "",
        "email_domain": "",
        "password_hash": "",
        "user_fullname": "",
        "user_name": user_name,
        "user_id": "",
        "transaction_id": "",
        "user_dob": "",
        "user_category": "",
        "user_account_status": "",
        "user_created": "",
        "user_country": "",
        "user_city": "",
        "user_region": "",
        "user_zip": "",
        "user_street": "",
        "user_street2": "",
        "session": "",
        "phone_number": "",
        "transaction_type": "",
        "bonus_campaign_id": "",
        "merchant_id": "",
        "details_url": "",
        "custom_fields": {
        }
    }
    
    response = requests.post('https://api.seon.io/SeonRestService/fraud-api/v2.0', headers=headers,
                             data=json.dumps(payload))
    full_response = response.json()
    
    try:
        return full_response.get('data').get('fraud_score')
    
    except:
        return None
