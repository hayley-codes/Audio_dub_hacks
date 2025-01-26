import os
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
    
    filename, ext = os.path.splitext(video_file)
    output_audio = f"{filename}.{output_ext}"
    
    try:
        subprocess.run(["ffmpeg", "-y", "-i", video_file],
                      stdout=subprocess.DEVNULL,
                      stderr=subprocess.STDOUT)
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
        return result['translatedText']
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
        print(f"File '{output_file}' already exists. Skipping generation.")
        return output_file

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