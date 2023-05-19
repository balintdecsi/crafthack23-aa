from dev.src import originality_ai
from dev.src import seon
import os


originality_api_key = os.environ.get('originality_api_key')
seon_api_key = os.environ.get('seon_api_key')

seon_score_trashold = 10
ai_score_trashold = 0.1

def make_review_score(originality_api_key, seon_api_key, URL):
    ai_score = originality_ai.get_originality_ai_score(api_key = originality_api_key, URL = URL)
    seon_score = seon.get_seon_fraud_score(api_key = seon_api_key,  URL = URL)
       
    if seon_score >= 10 or ai_score >= 0.1:
        return 1
    else:
        return 0

