# gemini-voice-chatbot
This project is a Gemini 1.5 Flash-powered chatbot with automatic text-to-speech (TTS) using gTTS and Gradio for the UI. It accepts text input, responds with intelligent replies from Google's Gemini API, and plays back the response using generated voice — auto-playing the audio for a seamless experience.

## Features
✅ Text-based chatbot using Gemini 1.5 Flash

🔊 Auto-generated speech for responses using Google Text-to-Speech (gTTS)

🎛️ Built with an interactive Gradio interface

🧼 Cleans Markdown-style formatting from chatbot responses

🎙️ Auto-plays voice responses using injected JavaScript

🧠 Maintains conversation history for contextual awareness

Requirements
Make sure you have Python 3.7+ and install dependencies:
pip install gradio google-generativeai gTTS

🔑 Setup
Get your Google Generative AI API key.

Set it as an environment variable or directly in the script:
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"

▶️ Usage
Simply run the script:
python gemini-voice-chatbot.py

 Example Inputs
Try these examples in the chatbot:

"What is AI?"

"Who is the Prime Minister of India?"

 File Structure

├── app.py              # Main chatbot script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

 Acknowledgements
Google Generative AI (Gemini) ,
Gradio ,
gTTS

