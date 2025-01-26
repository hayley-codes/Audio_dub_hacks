from flask import Flask, request, jsonify
import os
from utils import extract_audio, transcribe_audio, translate_text, text_to_mp3, combine_video_audio
import os
import subprocess
from google.cloud import speech
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate

app = Flask(__name__)

@app.route('/process-video', methods=['POST'])
def process_video():
    print("Hello world")
    try:
        # Step 1: Handle file upload
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files.get('file')
        target_language = request.form.get('target_language', 'es')  # Default to Spanish if not specified
        
        #Debugging
        print(f"Received file: {file.filename}")

        # Save uploaded file
        UPLOAD_FOLDER = "uploads"
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        input_video = os.path.join(UPLOAD_FOLDER, file.filename).replace("\\","/")
        
        #Debugging
        print(f"Saving file to {input_video}")
        if not os.path.exists(input_video):
            return jsonify({"error": "File upload failed"}), 400

        file.save(input_video)
        print("File saved")
        
        # Step 2: Convert MP4 to WAV
        wav_path = extract_audio(input_video)
        if isinstance(wav_path, dict) and "error" in wav_path:
            return jsonify(wav_path), 400
        
        # Step 3: Convert WAV to transcript
        transcript = transcribe_audio(wav_path)
        
        # Step 4: Translate transcript
        translated_text = translate_text(transcript, target_language)
        print(translated_text)
        
        # Step 5: Convert translated text to MP3
        output_filename = f"translated_audio_{target_language}.mp3"
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)
        final_audio_path = text_to_mp3(
            translated_text, 
            output_file=output_path,
            language_code=target_language
        )
        # Step 6: Combine video and audio
        
        #Debugging
        print(f"Generated translated audio file: {final_audio_path}")
        print(f"Checking if audio file exists: {os.path.exists(final_audio_path)}")
        print(f"Original video path: {input_video}")
        print(f"Checking if video file exists: {os.path.exists(input_video)}")

        combined_output_filename = f"combined_video_{target_language}.mp4"
        combined_output_path = os.path.abspath(os.path.join(UPLOAD_FOLDER, combined_output_filename))
        
        print(f"Expected combined output file path: {combined_output_path}") #Debugging
        
        #Run FFmpeg combination function
        combined_video_path = combine_video_audio(input_video, final_audio_path, combined_output_path)
        
        print(f"Expected combined video file exists: {os.path.exists(combined_video_path)}") #Debugging
        
        if not combined_video_path or not isinstance(combined_video_path, str):
            return jsonify({"error": "Failed to generate combined video"}), 500

        if not os.path.exists(combined_video_path):
            return jsonify({"error": "Combined video file was not created"}), 500

        print(f"Type of combined_video_path: {type(combined_video_path)}")

        return jsonify({
            "success": True,
            "original_text": transcript,
            "translated_text": translated_text,
            "audio_file_path": final_audio_path,
            "combined_video_path": combined_video_path
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)