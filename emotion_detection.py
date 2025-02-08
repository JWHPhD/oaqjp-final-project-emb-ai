import requests
import json

#  Create a function named emotion_detector that takes a string input (text_to_analyse).
def emotion_detector(text_to_analyse):  
    
    #  URL for accessing the Emotion Predict function.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #  Set headers for the API request.
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #  Create a dictionary with the text to be analysed.
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers = header)  #  Send a POST request to the API with headers and text.
    formatted_response = json.loads(response.text)  #  Return response text and convert to json format.

    #  Create dictionary to store extracted emotions.
    emotions_dict = {}
    
    #  Extract the required set of emotions.
    if "emotionPredictions" in formatted_response:  # Direct dictionary access
        for prediction in formatted_response['emotionPredictions']:
            if "emotion" in prediction:  # Only select when the key is 'emotions'.
                emotions_dict = prediction["emotion"]  # Store the emotion in the dictionary
 
    #  Set initial values.
    dominant_emotion = None
    highest_score = 0

    #  if emotions_dict:  #  
    for emotion, score in emotions_dict:
        if score > highest_score:
            highest_score = score
            dominant_emotion = emotion
                    
    # Add dominant emotion to the dictionary
    emotions_dict["dominant_emotion"] = dominant_emotion

    return emotions_dict
    