import os
import re
import gradio as gr
import google.generativeai as genai
from gtts import gTTS
import tempfile

# Google API Key setup
os.environ["GOOGLE_API_KEY"] = "Your API KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def clean_text_for_tts(text):
    text = re.sub(r'[\*_~]+', '', text)
    text = re.sub(r'-{2,}', ' ', text)
    text = re.sub(r'[=_]{2,}', ' ', text)
    text = re.sub(r'[\[\]<>]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chatbot_response(user_message, chat_state, gr_history):
    if user_message.strip() == "":
        return "", chat_state, gr_history, None

    try:
        if chat_state is None:
            chat_state = model.start_chat(history=[])
            gr_history = []

        response = chat_state.send_message(user_message)
        answer = response.text

        clean_answer = clean_text_for_tts(answer)

        tts = gTTS(text=clean_answer, lang="en")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        # Make sure gr_history is initialized
        gr_history = gr_history or []
        gr_history.append([user_message, answer])

        return "", chat_state, gr_history, temp_file.name

    except Exception as e:
        error_msg = f"⚠️ Error: {str(e)}"
        print(error_msg)
        gr_history.append([user_message, error_msg])
        return "", chat_state, gr_history, None


css = """
audio {
    display: none !important;
}
"""

js = """
<script>
window.onload = function() {
    const observer = new MutationObserver(() => {
        const audios = document.querySelectorAll('audio');
        audios.forEach(audio => {
            if (audio.paused) {
                audio.play().catch(() => {
                    console.log("Audio autoplay blocked.");
                });
            }
        });
    });
    observer.observe(document.body, {childList: true, subtree: true});
};
</script>
"""

with gr.Blocks(css=css) as demo:
    gr.HTML(js)
    gr.Markdown("## 🤖 Gemini-powered Chatbot with TTS and Persistent Chat")

    chatbot = gr.Chatbot(label="Chatbot")
    message = gr.Textbox(label="Your message", placeholder="Type here...", lines=10)
    audio_out = gr.Audio(type="filepath", interactive=False, autoplay=True)

    chat_state = gr.State()
    
    message.submit(
        fn=chatbot_response,
        inputs=[message, chat_state, chatbot],
        outputs=[message, chat_state, chatbot, audio_out],
    )

    gr.Examples(
        examples=[["What is AI?"], ["Who is the PM of India?"]],
        inputs=[message],
        fn=chatbot_response,
        outputs=[message, chat_state, chatbot, audio_out],
    )

if __name__ == "__main__":
    demo.launch()
