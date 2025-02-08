import requests

#  Create a function named emotion_detector that takes a string input (text_to_analyse).
def emotion_detector(text_to_analyse):  
    
    #  URL for accessing the Emotion Predict function.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #  Set headers for the API request.
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #  Create a dictionary with the text to be analysed.
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers = header)  #  Send a POST request to the API with headers and text.
    return response.text #  Return the response text from the API.

