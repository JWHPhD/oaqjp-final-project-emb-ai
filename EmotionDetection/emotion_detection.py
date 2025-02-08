import requests
import json

#  Create a function named emotion_detector that takes a string input (text_to_analyze).
def emotion_detector(text_to_analyze):  
    
    #  URL for accessing the Emotion Predict function.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #  Set headers for the API request.
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #  Create a dictionary with the text to be analysed.
    myobj = {"raw_document": {"text": text_to_analyze}}
    
    #  Send a POST request to the API with headers and text.
    response = requests.post(url, json = myobj, headers = header)  
    
    #  Return response text and convert to json format.
    formatted_response = json.loads(response.text)  

    
    emotions_dict = {}  #  Create dictionary to store extracted emotions.
    
    #  Extract the required set of emotions.
    if "emotionPredictions" in formatted_response:  # Direct dictionary access
        for prediction in formatted_response['emotionPredictions']:
            if "emotion" in prediction:  # Only select when the key is 'emotions'.
                emotions_dict = prediction["emotion"]  # Store the emotion in the dictionary.
 
    
    dominant_emotion = None  #  Set initial values.
    highest_score = 0
    #  Determining the emotion with the highest score.
    for key, score in emotions_dict.items():
        if score > highest_score:  #  Compare each value to see if it is the highest score.
            highest_score = score  #  Assign the value of the highest score.
            dominant_emotion = key  #  Assign the key with the highest score.

    emotions_dict["dominant_emotion"] = dominant_emotion  #  Add dominant emotion to dictionary.              
    
    #  Return dictionary containing final output.
    return emotions_dict
    