"""
This is the emotion_detector() function using Watson NLP library.
"""

import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    
    # Step 1: Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Step 2: Extract required set of emotions and their scores
    if response.status_code == 200:        
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    # Step 3: Find the dominant emotion
        emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        dominant_emotion_index = emotion_list.index(max(emotion_list))
        emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        dominant_emotion_key = emotion_keys[dominant_emotion_index]

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_key = None

    # Step 4: Modify the function to return the required output format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_key
    }
    
    return result
