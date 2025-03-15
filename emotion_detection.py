""" Emotion detection module """
import requests

def emotion_detector(text_to_analyze):
    """ Detect emotion on text """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=body, timeout=20)
    
    return response.text
