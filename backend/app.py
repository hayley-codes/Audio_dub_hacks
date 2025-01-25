from flask import Flask, request, jsonify
import openai
from deep_translator import GoogleTranslator
from gtts import gTTS
import ffmpeg
from spleeter.separator import Separator

app = Flask(__name__)

openai.api_key = "your-api-key"  # Add your OpenAI API key

@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files['file']
    file.save("input.mp4")
    return jsonify({"message": "Video uploaded successfully!"})

@app.route('/extract-audio', methods=['POST'])
def extract_audio():
    ffmpeg.input("input.mp4").output("output.wav").run()
    return jsonify({"message": "Audio extracted!", "file": "output.wav"})

@app.route('/separate-audio', methods=['POST'])
def separate_audio():
    separator = Separator("spleeter:2stems")
    separator.separate_to_file("output.wav", "output")
    return jsonify({"message": "Audio separated!", "vocals": "output/vocals.wav", "background": "output/background.wav"})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    with open("output/vocals.wav", "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    return jsonify({"text": response["text"]})

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json["text"]
    target_lang = request.json["language"]
    translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
    return jsonify({"translated_text": translated_text})

@app.route('/tts', methods=['POST'])
def text_to_speech():
    text = request.json["text"]
    lang = request.json["language"]
    tts = gTTS(text=text, lang=lang)
    tts.save("dubbed_speech.mp3")
    return jsonify({"message": "TTS generated!", "file": "dubbed_speech.mp3"})

if __name__ == '__main__':
    app.run(debug=True)
