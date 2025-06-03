# gemini-voice-chatbot
This project is a Gemini 1.5 Flash-powered chatbot with automatic text-to-speech (TTS) using gTTS and Gradio for the UI. It accepts text input, responds with intelligent replies from Google's Gemini API, and plays back the response using generated voice — auto-playing the audio for a seamless experience.

## Features
1.  Text-based chatbot using Gemini 1.5 Flash
   
2.  Auto-generated speech for responses using Google Text-to-Speech (gTTS)
   
3.  Built with an interactive Gradio interface
  
4.  Cleans Markdown-style formatting from chatbot responses

5.   Auto-plays voice responses using injected JavaScript

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

Example Inputs :-
Try these examples in the chatbot:

"What is AI?"

"Who is the Prime Minister of India?"

 File Structure

.
├── app.py              # Main chatbot script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation


 Acknowledgements : -
Google Generative AI (Gemini) ,
Gradio ,
gTTS  

Gradio

gTTS (Google Text-to-Speech)

