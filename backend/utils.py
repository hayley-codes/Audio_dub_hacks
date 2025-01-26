import os
import html
import re
import time
import subprocess
from google.cloud import speech
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate

# Helper function for Task 1: MP4 to WAV
def extract_audio(video_file, output_ext="wav"):
    """
    Extracts audio from a video file and converts it to the specified audio format.

    Args:
        video_file (str): Path to the input video file
        output_ext (str, optional): Desired output audio format extension. Defaults to "wav"

    Returns:
        str: Path to the output audio file if successful
        dict: Error message if file not found
        str: Error message if conversion fails
    """
    
    if not os.path.exists(video_file):
        return {"error": f"File {video_file} not found"}
    
    print(f"Extracting! audio from: {video_file}") #Debugging
   
    filename, ext = os.path.splitext(os.path.basename(video_file))
    
    print(f"Filename: {filename}, Extension: {ext}") #Debugging
    
    output_audio = os.path.join(os.path.dirname(video_file), f"{filename}.{output_ext}")
    
    
    #output_audio = f"{filename}.{output_ext}"
    
    print(f"Output WAV file: {output_audio}") #Debugging

    try:
        subprocess.run(["ffmpeg", "-y", "-i", video_file, output_audio],
                      stdout=subprocess.DEVNULL,
                      stderr=subprocess.STDOUT)
        if not os.path.exists(output_audio):
            print("FFmpeg did not generate the expected WAV file!")
            return {"error": "WAV file was not created"}
        return output_audio
    except Exception as e:
        return str(e)
     

    
# Helper function for Task 2: WAV to transcript
def transcribe_audio(audio_path):
    """
    Transcribes an audio file to text using Google Cloud Speech-to-Text API.

    Args:
        audio_path (str): Path to the input audio file (should be WAV format)

    Returns:
        str: Transcribed text from the audio file

    Note:
        The function assumes the audio is in English (en-US) and has 2 channels.
        The audio file should be accessible and in a supported format.
    """
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        language_code="en-US",
        audio_channel_count=2,
    )

    response = client.recognize(config=config, audio=audio)
    transcript_string = ""

    for result in response.results:
        transcript_string += result.alternatives[0].transcript

    return transcript_string

# Helper function for Task 3: Text translation
def translate_text(text, target_language):
    """
    Translates text to the specified target language using Google Cloud Translate API.

    Args:
        text (str): The text to translate
        target_language (str): The target language code (e.g., 'es' for Spanish, 'fr' for French)

    Returns:
        str: Translated text if successful
        str: Error message if translation fails
    """
    client = translate.Client()
    try:
        result = client.translate(text, target_language=target_language)
        translated_text = result['translatedText']
        translated_text = html.unescape(translated_text)
        translated_text = translated_text.encode('utf-8').decode('utf-8')
        translated_text = re.sub(r'[^\w\s,.!?\'"-]', '', translated_text)
        print(f"Final Translated Text: {translated_text}")
        return translated_text
    
    except Exception as e:
        return str(e)

# Helper function for Task 4: Text to MP3
def text_to_mp3(text, output_file="output.mp3", language_code="en-US", voice_name="en-US-Wavenet-D"):
    """
    Converts text to speech and saves it as an MP3 file using Google Cloud Text-to-Speech API.

    Args:
        text (str): The text to convert to speech
        output_file (str, optional): Path where the output MP3 will be saved. Defaults to "output.mp3"
        language_code (str, optional): Language code for the voice. Defaults to "en-US"
        voice_name (str, optional): Specific voice to use. Defaults to "en-US-Wavenet-D"

    Returns:
        str: Path to the generated MP3 file if successful
        None: If the file already exists (skips generation)

    Note:
        If the output file already exists, the function will skip generation and return the existing file path.
        The function uses a neutral gender voice for synthesis.
    """
    if os.path.exists(output_file):
        print(f"Deleting existing MP3 file: {output_file}")
        os.remove(output_file)
    else:
        print(f"Error: MP3 file was not created at {output_file}")

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to file: {output_file}")
    
    return output_file 

# Helper function for Task 5: Combine video and audio

def combine_video_audio(video_file, audio_file, output_file):
    """
    Combines the video file and audio file into a new video file with the dubbed audio.

    Args:
        video_file (str): Path to the input video file
        audio_file (str): Path to the input audio file
        output_file (str): Path where the output video file will be saved

    Returns:
        str: Path to the output file if successful
        dict: Error message if file not found
        str: Error message if combination fails
    """
    #Delete previous MP4
    if os.path.exists(output_file):
        try:
            os.remove(output_file)
            print(f"Deleted old video file: {output_file}")
            # Ensure file is fully deleted
            time.sleep(1)  # Add small delay for OS to release file lock
        except Exception as e:
            print(f"ERROR: Failed to delete old video: {str(e)}")
            return {"error": "Failed to delete old video file"}

    # Ensure all paths are absolute
    video_file = os.path.abspath(video_file)
    audio_file = os.path.abspath(audio_file)
    output_file = os.path.abspath(output_file)

    # Check if input files exist
    if not os.path.exists(video_file):
        print(f"ERROR: Video file not found: {video_file}")
        return {"error": "Video input file not found"}
    if not os.path.exists(audio_file):
        print(f"ERROR: Audio file not found: {audio_file}")
        return {"error": "Audio input file not found"}

    print(f"Combining video {video_file} with audio {audio_file} into {output_file}")

    # Get durations of video and audio
    def get_duration(file):
        cmd = [
            "ffprobe", "-i", file, "-show_entries", "format=duration",
            "-v", "quiet", "-of", "csv=p=0"
        ]
        try:
            return float(subprocess.check_output(cmd).decode("utf-8").strip())
        except Exception as e:
            return {"error": f"Failed to retrieve duration for {file}: {str(e)}"}

    video_duration = get_duration(video_file)
    audio_duration = get_duration(audio_file)

    if isinstance(video_duration, dict) or isinstance(audio_duration, dict):
        return {"error": "Failed to retrieve file durations"}

    print(f"Video Duration: {video_duration}s, Audio Duration: {audio_duration}s")

    # Adjust audio to match video duration
    adjusted_audio_file = os.path.join(os.path.dirname(audio_file), "adjusted_audio.mp3")

    if audio_duration > video_duration:
        print(f"Trimming audio from {audio_duration}s to {video_duration}s")
        trim_cmd = [
            "ffmpeg", "-y", "-i", audio_file, "-t", str(video_duration),
            "-c:a", "libmp3lame", "-b:a", "192k", adjusted_audio_file
        ]
    else:
        print(f"Padding audio to match video duration")
        trim_cmd = [
            "ffmpeg", "-y", "-i", audio_file, "-af",
            f"apad=whole_dur={video_duration}",
            "-c:a", "libmp3lame", "-b:a", "192k", adjusted_audio_file
        ]

    try:
        result = subprocess.run(trim_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        print(f"Audio Trim/Pad Output: {result.stdout}")
        print(f"Audio Trim/Pad Error: {result.stderr}")
        
        if not os.path.exists(adjusted_audio_file):
                print(f"ERROR: Adjusted audio file {adjusted_audio_file} was not created.")
                return {"error": "Failed to create adjusted audio file"}

    except Exception as e:
        return {"error": f"Failed to adjust audio duration: {str(e)}"}

    # Ensure adjusted audio file exists
    if not os.path.exists(adjusted_audio_file):
        return {"error": "Failed to create adjusted audio file"}

    print(f"Final Adjusted Audio: {adjusted_audio_file}")

    # Combine adjusted audio with video
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", video_file, "-i", adjusted_audio_file,
        "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", "-shortest", 
        "-async", "1",  "-movflags", "faststart",output_file
    ]

    try:
        result = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        print(f"FFmpeg Output: {result.stdout}")
        print(f"FFmpeg Error: {result.stderr}")
    
    except Exception as e:
        return {"error": f"FFmpeg failed to combine video and audio: {str(e)}"}

    # Check if output file was created successfully
    if not os.path.exists(output_file):
        return {"error": "Combined video file was not created"}

    print(f"Successfully created {output_file}")
    return output_file
