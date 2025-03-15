""" Deployment of Emotion Detection Application with Flask """

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Application")

@app.route("/emotionDetector")
def detect_emotion():
    """ Detect emotion from text """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    anger_score_result = f"'anger': {result['anger']}"
    disgust_score_result = f"'disgust': {result['disgust']}"
    fear_score_result = f"'fear': {result['fear']}"
    joy_score_result = f"'joy': {result['joy']}"
    sadness_score_result = f"'sadness': {result['sadness']}"
    emotion_score_result = f"{anger_score_result}, {disgust_score_result}, {fear_score_result}, {joy_score_result} and {sadness_score_result}"

    return f"For the given statement, the system response is {emotion_score_result}. The dominant emotion is <b>{result['dominant_emotion']}</b>."

@app.route("/")
def home():
    """ Render emotion detection interface """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
