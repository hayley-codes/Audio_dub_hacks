from flask import Flask, request, jsonify
import openai
from deep_translator import GoogleTranslator
from gtts import gTTS
import ffmpeg
import os
import sys
import subprocess
from google.cloud import speech
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate

app = Flask(__name__)

#TASK 1: MP4 TO WAV
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

#TASK 2: Turns WAV audio files to a string, returns a transcript String
def transcribe_audio(audio_path):
    # Initialize client
    client = speech.SpeechClient()

    # Read the audio file
    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    # Configure audio and recognition settings
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        #encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # Update this if using a different format
        #sample_rate_hertz=64000,  # Update based on your audio file's sample rate
        language_code="en-US",    # Replace with your desired language code
        audio_channel_count=2,
    )

    # Perform the transcription
    response = client.recognize(config=config, audio=audio)

    transcript_string=""

    # Process and print results
    for result in response.results:
        transcript_string+=(result.alternatives[0].transcript)

    return transcript_string
audio_path="test_video.wav"


# TASK 3 Takes the text & sends a JSON request for target language, uses target language to translate 
@app.route('/translate', methods=['POST'])
def translate_text_api():
    # Get the incoming JSON request from the frontend
    data = request.get_json()

    # Check if 'target_language' is in the request
    if 'target_language' not in data:
        return jsonify({"error": "Missing 'target_language' in the request"}), 400
    
    # Get the target language from the request
    target_language = data['target_language']

    # Call the transcribe_audio function (the text is obtained here)
    text = transcribe_audio("path/to/audio/file")  # Assuming the audio file is passed here

    # Now, call the translation function
    translated_text = translate_text(text, target_language)

    return jsonify({
        "originalText": text,
        "translatedText": translated_text
    })

#TASK 4 Takes text and target language as parameter, translates given text to target language. Text to mp3 takes the new translated text
# and outputs an mp3 file with the audio version 
def translate_text(text, target_language):
    client = translate.Client()
    try:
        # Translate the text using the Google Translate API
        result = client.translate(text, target_language=target_language)
        #return result['translatedText']
        
    except Exception as e:
        return str(e)
#def text_to_mp3(text, output_file="output.mp3", language_code="en-US", voice_name="en-US-Wavenet-D"):
    """
    Converts input text into an MP3 audio file using Google Cloud Text-to-Speech API.

    Args:
        text (str): The input text to be converted.
        output_file (str): The name of the output MP3 file.
        language_code (str): The language code for the Text-to-Speech API (default: "en-US").
        voice_name (str): The name of the TTS voice (default: "en-US-Wavenet-D").
    """
    if os.path.exists(output_file):
        print(f"File '{output_file}' already exists. Skipping generation.")
        return

    client = texttospeech.TextToSpeechClient()

    # Configure the text input
    input_text = texttospeech.SynthesisInput(text=text)

    # Select the voice
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Set the audio format
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Generate speech
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    # Save the audio content to an MP3 file
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to file: {output_file}")



text_to_mp3("hi i'm very sleepy")




if __name__ == '__main__':
    app.run(debug=True)