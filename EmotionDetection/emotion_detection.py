""" Emotion detection module """
import json
import requests

def emotion_detector(text_to_analyze):
    """ Detect emotion on text """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=body, timeout=20)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    emotions_scores = list(emotions.values())
    emotions_names = list(emotions.keys())

    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    dominant_emotion_name = emotions_names[emotions_scores.index(max(emotions_scores))]

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_name
    }
