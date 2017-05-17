import json
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

language_translator = LanguageTranslator(
    username='',
    password= ''
 )

tone_analyzer = ToneAnalyzerV3(
   username='',
   password='',
   version='')

def getJson(tweet):
    translation = language_translator.translate(
        text=tweet,
        source='pt',
        target='en'
    )
    phrase = (json.dumps(translation, indent=2, ensure_ascii=False))
    resp = json.dumps(tone_analyzer.tone(text=phrase), indent=2)
    data  = json.loads(resp)
    response = []

    for row in data['document_tone']['tone_categories']:
        if(row['category_id'] == "emotion_tone"):
            response = row['tones']

    return response
