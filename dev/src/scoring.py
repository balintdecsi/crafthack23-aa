from dev.src import originality_ai
from dev.src import seon
import os


originality_api_key = os.environ.get('originality_api_key')
seon_api_key = os.environ.get('seon_api_key')

seon_score_treshold = 10
ai_score_treshold = 0.1

def make_review_score(originality_api_key, seon_api_key, URL):
    ai_score = originality_ai.get_originality_ai_score(api_key = originality_api_key, URL = URL)
    seon_score = seon.get_seon_fraud_score(api_key = seon_api_key,  URL = URL)
       
    if seon_score >= seon_score_treshold or ai_score >= ai_score_treshold:
        return 1
    else:
        return 0

