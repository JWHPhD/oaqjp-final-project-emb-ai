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

    #  Create a variable to hold the dominant emotion result.
    dom_emotion = response.get("dominant_emotion", "Unknown")
    response.pop("dominant_emotion",  None)  #  Delete the dominant emotion entry.
    
    #  Return the output per the customer's request..
    return f"For the given statement, the system response is {response}. The dominant emotion is {dom_emotion}."

@app.route("/")
def render_index_page():
    #  Render the HTML template.
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)