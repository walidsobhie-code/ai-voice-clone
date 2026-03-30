#!/usr/bin/env python3
"""
AI Voice Clone - Gradio Web UI
Run: python web_ui.py
"""
import gradio as gr
import os
import warnings
warnings.filterwarnings('ignore')

try:
    from TTS.api import TTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False


class VoiceCloneUI:
    def __init__(self):
        self.tts = None
        if TTS_AVAILABLE:
            try:
                self.tts = TTS("tts_models/multilingual/multi-speaker/neural_hubert")
            except Exception as e:
                print(f"⚠️  TTS load error: {e}")

    def synthesize(self, text, language, speed):
        """Synthesize speech"""
        if not text:
            return None, "Please enter text to synthesize"

        if not TTS_AVAILABLE or self.tts is None:
            return None, "⚠️ TTS not installed. Run: pip install TTS"

        try:
            output_path = "/tmp/gradio_output.wav"
            self.tts.tts_to_file(
                text=text,
                file_path=output_path,
                language=language,
                speed=speed
            )
            return output_path, "✅ Synthesis complete!"
        except Exception as e:
            return None, f"❌ Error: {str(e)}"


# Create UI
ui = VoiceCloneUI()

demo = gr.Interface(
    fn=ui.synthesize,
    inputs=[
        gr.Textbox(label="Text to synthesize", placeholder="Enter text here..."),
        gr.Dropdown(["en", "ar", "es", "fr", "de", "it", "pt", "zh", "ja", "ko"],
                   label="Language", value="en"),
        gr.Slider(minimum=0.5, maximum=2.0, value=1.0, step=0.1, label="Speed")
    ],
    outputs=[
        gr.Audio(label="Generated Speech"),
        gr.Textbox(label="Status")
    ],
    title="🎤 AI Voice Clone",
    description="Generate speech in multiple languages using AI",
    examples=[
        ["Hello world!", "en", 1.0],
        ["مرحبا بالعالم", "ar", 1.0],
        ["Bonjour le monde", "fr", 1.0]
    ]
)

if __name__ == "__main__":
    print("🚀 Starting AI Voice Clone Web UI...")
    print("   Open http://localhost:7860 in your browser")
    demo.launch(server_name="0.0.0.0")