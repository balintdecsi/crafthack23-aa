import requests
import json

headers = {
  "X-API-KEY": "51e9a24b-53f5-42db-9935-cb24cd8f3a3f"
}

def get_user_score(user_name: str) -> str:
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
    return response.json()['data']['fraud_score']