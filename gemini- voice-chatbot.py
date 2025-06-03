import os
import re
import gradio as gr
import google.generativeai as genai
from gtts import gTTS
import tempfile

# Set your Google API key here
os.environ["GOOGLE_API_KEY"] = "Your API Key"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def clean_text_for_tts(text):
    # Remove markdown-like characters: *, _, , ~
    text = re.sub(r'[\*_~]+', '', text)

    # Replace long dashes or multiple dashes with a space
    text = re.sub(r'-{2,}', ' ', text)

    # Replace sequences of = or _ with a space (used in markdown headers)
    text = re.sub(r'[=_]{2,}', ' ', text)

    # Remove angle brackets, brackets, or other markdown artifacts
    text = re.sub(r'[\[\]<>]', '', text)

    # Replace multiple whitespace with a single space
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def chatbot_response(user_message, gr_history):
    try:
        gr_history = gr_history or []
        flat_texts = [msg["content"] for msg in gr_history]

        chat = model.start_chat(history=flat_texts)
        response = chat.send_message(user_message)
        answer = response.text

        clean_answer = clean_text_for_tts(answer)

        tts = gTTS(text=clean_answer, lang="en")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        new_gr_history = gr_history + [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": answer}
        ]

        return "", new_gr_history, temp_file.name

    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return "", gr_history, None


css = """
audio {
    display: none !important;  /* Hide audio controls */
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
    gr.HTML(js)  # Inject JS for auto-playing audio

    gr.Markdown("## 🤖 Gemini-powered Chatbot with Auto Text-to-Speech")

    chatbot = gr.Chatbot(label="Chatbot", type="messages")
    message = gr.Textbox(label="Your message", placeholder="Type here...")

    audio_out = gr.Audio(type="filepath", interactive=False, autoplay=True)

    message.submit(
        fn=chatbot_response,
        inputs=[message, chatbot],
        outputs=[message, chatbot, audio_out],
    )

    gr.Examples(
        examples=[["What is AI?"], ["Who is the PM of India?"]],
        inputs=[message],
        fn=chatbot_response,
        outputs=[message, chatbot, audio_out],
    )
    if __name__ == "__main__":
        demo.launch()