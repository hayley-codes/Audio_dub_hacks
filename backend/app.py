from flask import Flask, request, jsonify
import openai
from deep_translator import GoogleTranslator
from gtts import gTTS
import ffmpeg
import os

app = Flask(__name__)

openai.api_key = "your-api-key"  # Add your OpenAI API key

@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files['file']
    file.save("input.mp4")
    return jsonify({"message": "Video uploaded successfully!"})

@app.route('/extract-audio', methods=['POST'])
def extract_audio():
    input_video = "input.mp4"
    output_audio = "output.wav"

    try:
        ffmpeg.input(input_video).output(output_audio).run()
        return jsonify({"message": "Audio extracted!", "file": output_audio})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/separate-audio', methods=['POST'])
def separate_audio():
    input_audio = "output.wav"
    vocals_output = "output/vocals.wav"
    background_output = "output/background.wav"

    try:
        # Use FFmpeg's built-in vocal reduction and isolation
        os.system(f'ffmpeg -i {input_audio} -af "highpass=f=300, lowpass=f=3000" {vocals_output}')
        os.system(f'ffmpeg -i {input_audio} -af "pan=stereo|c0=c0+c1|c1=c0+c1, highpass=f=150, lowpass=f=4000" {background_output}')

        return jsonify({
            "message": "Audio separated!",
            "vocals": vocals_output,
            "background": background_output
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
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
