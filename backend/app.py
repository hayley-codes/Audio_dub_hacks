from flask import Flask, request, jsonify
import os
from utils import extract_audio, transcribe_audio, translate_text, text_to_mp3

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process-video', methods=['POST'])
def process_video():
    try:
        # Step 1: Handle file upload
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files.get('file')
        target_language = request.form.get('target_language', 'es')  # Default to Spanish if not specified
        
        # Save uploaded file
        input_video = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_video)
        
        # Step 2: Convert MP4 to WAV
        wav_path = extract_audio(input_video)
        if isinstance(wav_path, dict) and "error" in wav_path:
            return jsonify(wav_path), 400
        
        # Step 3: Convert WAV to transcript
        transcript = transcribe_audio(wav_path)
        
        # Step 4: Translate transcript
        translated_text = translate_text(transcript, target_language)
        
        # Step 5: Convert translated text to MP3
        output_filename = f"translated_audio_{target_language}.mp3"
        output_path = os.path.join(UPLOAD_FOLDER, output_filename)
        final_audio_path = text_to_mp3(
            translated_text, 
            output_file=output_path,
            language_code=target_language
        )
        
        return jsonify({
            "success": True,
            "original_text": transcript,
            "translated_text": translated_text,
            "audio_file_path": final_audio_path
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)