Our demo showcases a functional prototype of DubIT, a video dubbing tool designed to expand access to multilingual content. The web app accepts an .mp4 video input and automatically generates a version dubbed in a target language.

The backend, written in Python, uses Google Cloud Speech-to-Text and Translation APIs to transcribe and translate audio, while FFmpeg is used to separate and reconstruct the video and audio streams. The final output is a fully reassembled .mp4 video dubbed in the selected language.


TO RUN:

Ensure you have Next.js, Flask, React, and FFMpeg installed on your machine.

Clone this project.

CD into backend

In terminal, ensure you are in a virtual environment, then type ``` pip install -r requirements.txt ```

Navigate to frontend/my-app

In terminal, type ``` npm install ```

Type ``` npm run dev ```

This should bring you to the webapp.
