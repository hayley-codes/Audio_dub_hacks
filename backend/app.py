from flask import Flask, request, jsonify
import openai
from deep_translator import GoogleTranslator
from gtts import gTTS
import ffmpeg
import os
import sys
import subprocess

app = Flask(__name__)

#TASK ONE: MP4 TO WAV
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#Extracts the audio from mp4 as wav file 
def extract_audio(video_file, output_ext="wav"):
    if not os.path.exists(video_file):
        return {"error": f"File {video_file} not found"}
    
    filename, ext = os.path.splitext(video_file)
    output_audio = f"{filename}.{output_ext}"
    
    try:
        subprocess.run(["ffmpeg", "-y", "-i", video_file],
                        stdout = subprocess.DEVNULL,
                        stderr = subprocess.STDOUT)
        return output_audio
    except Exception as e:
        return str(e)

#Flask route to recieve MP4 file from frontend
@app.route('/extract-audio', methods=['POST'])
def extract_audio_api():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files.get('file')
    
    input_video = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_video)
    
    output_audio = extract_audio(input_video)
    
    return jsonify({"message": "Audio extracted!", "file": output_audio})

if __name__ == '__main__':
    app.run(debug=True)
