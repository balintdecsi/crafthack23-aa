import requests

def make_originality_ai_request(text: str, api_key: str):

    # Specify the API endpoint URL
    url = 'https://api.originality.ai/api/v1/scan/ai'
    
    # Set up the request headers
    headers = {
        'X-OAI-API-KEY': api_key
                }
    
    # Set up the request json
    payload = {
            "title": "base title",
            "content": f'{text}'
        }
    # Send the request
    response = requests.post(url, headers = headers, json = payload)
    
    # Process the response
    if response.status_code == 200:
        # Request successful
        full_response = response.json()
        
    else:
        # Request failed
        #full_response = {"Request failed with status code: " + str(response.status_code)}
        full_response = {}
    return full_response



def get_originality_ai_score(text: str, api_key: str):
    full_response = make_originality_ai_request(text, api_key)
    try:
        score = full_response.get('score').get('ai')
        return score
    except:
        return 0

