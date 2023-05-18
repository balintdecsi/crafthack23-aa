import originality_ai
import seon


text = """
This beautiful Mercedes-Benz E-Class is an absolute gem on the road. Its striking silver color and meticulously crafted design are truly captivating. With the 2020 model, it offers a fresh and modern appearance.
The car has only covered 20,000 miles, ensuring many years of reliable performance. It runs on petrol, providing an economical and environmentally friendly choice.
Step inside, and you'll be greeted by luxury and comfort. The premium materials and modern features create a perfect blend that enhances your driving experience. The comfortable seats and spacious interior ensure maximum comfort during every journey.
Don't miss out on this incredible opportunity to own a fantastic car. Contact us now to arrange a test drive and make this Mercedes-Benz E-Class yours today!
"""

originality_api_key = 'i7h8mkczvloynfp364eq0a5ujrdxbt2g'
seon_api_key = "51e9a24b-53f5-42db-9935-cb24cd8f3a3f"
user_name = 'valami'


def make_review_score(originality_api_key, seon_api_key, text, **kwargs):
    ai_score = originality_ai.get_originality_ai_score(api_key = originality_api_key, text = text)
    seon_score = seon.get_seon_fraud_score(api_key = seon_api_key,  user_name = user_name)
       
    if seon_score >= 10 or ai_score >= 0.9:
        return 1
    else:
        return 0

    
