""" Deployment of Emotion Detection Application with Flask """

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Application")

@app.route("/emotionDetector")
def detect_emotion():
    """ Detect emotion from text """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    anger= f"'anger': {result['anger']}"
    disgust = f"'disgust': {result['disgust']}"
    fear = f"'fear': {result['fear']}"
    joy = f"'joy': {result['joy']}"
    sadness = f"'sadness': {result['sadness']}"
    emotion_result = f"{anger}, {disgust}, {fear}, {joy} and {sadness}"
    result_prefix = "For the given statement, the system response is"
    result_suffix = f"The dominant emotion is <b>{result['dominant_emotion']}</b>"
    return f"{result_prefix} {emotion_result}. {result_suffix}."

@app.route("/")
def home():
    """ Render emotion detection interface """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
