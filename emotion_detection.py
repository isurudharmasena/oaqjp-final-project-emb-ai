import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detection(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
# Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotions from response
    anger = formatted_response['emotion']['anger']
    disgust = formatted_response['emotion']['disgust']
    fear = formatted_response['emotion']['fear']
    joy = formatted_response['emotion']['joy']
    sadness = formatted_response['emotion']['sadness']

    #get dominant emotion
    dominant_emotion = max(formatted_response['emotion'],key = data.get)

    return  {'anger': anger, 'disgust':disgust, 'fear':fear,'joy':joy,'sadness':sadness,'dominant_emotion':dominant_emotion} 