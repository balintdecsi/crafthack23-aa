from dev.src import originality_ai
from dev.src import seon


originality_api_key = 'i7h8mkczvloynfp364eq0a5ujrdxbt2g'
seon_api_key = "51e9a24b-53f5-42db-9935-cb24cd8f3a3f"


def make_review_score(originality_api_key, seon_api_key, URL):
    ai_score = originality_ai.get_originality_ai_score(api_key = originality_api_key, URL = URL)
    seon_score = seon.get_seon_fraud_score(api_key = seon_api_key,  URL = URL)
       
    if seon_score >= 10 or ai_score >= 0.1:
        return 1
    else:
        return 0

