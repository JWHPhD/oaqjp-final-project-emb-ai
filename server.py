#  Import the necessary libraries and functions.
from flask import Flask, render_template, request
#  Import the function emotion detector.
from EmotionDetection.emotion_detection import emotion_detector

#  Initiate and name the application.
app = Flask("Emotion Detector")


@app.route("/emotionDetector")

def sent_detector():
    #  Retrieve the text to be analyzed from the request arguments.
    text_to_analyze = request.args.get('textToAnalyze')

    #  Pass the text to the emotion_detector function and store the response.
    response = emotion_detector(text_to_analyze)

    dom_emotion = response[-1]
    response.delete[-1]
    
    return "For the given statement, the system response is "{response}. The dominant emotion is {dom_emotion}

