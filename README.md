gemini-voice-chatbot
Gemini Voice Chatbot is a conversational AI powered by Google’s Gemini 1.5 Flash model with automatic text-to-speech (TTS) functionality. It uses gTTS to convert the chatbot’s text replies into speech and Gradio for an interactive web interface. Your messages get smart replies that are also read out loud — audio plays automatically for a smooth experience.

Features
Smart Chatbot: Powered by Gemini 1.5 Flash to provide intelligent answers

Voice Responses: Converts chatbot replies to natural speech using Google Text-to-Speech (gTTS)

Interactive UI: Clean, easy-to-use interface built with Gradio

Markdown Cleaner: Removes markdown formatting for clear speech output

Auto-Playing Audio: JavaScript injected to play voice responses automatically

Requirements
Python 3.7 or higher

Install dependencies with:

bash
Copy
Edit
pip install gradio google-generativeai gTTS
Setup
Obtain your Google Generative AI API key from Google Makersuite.

Set your API key as an environment variable or directly in your Python script:

python
Copy
Edit
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
Usage
Run the chatbot application with:

bash
Copy
Edit
python app.py
This will open the Gradio chat interface in your default browser.

Example Questions to Try
What is AI?

Who is the Prime Minister of India?

Tell me a fun fact about space.

File Structure
bash
Copy
Edit
.
├── app.py              # Main chatbot script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
Acknowledgements
Google Generative AI (Gemini)

Gradio

gTTS (Google Text-to-Speech)

