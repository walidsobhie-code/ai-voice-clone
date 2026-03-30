#!/usr/bin/env python3
"""
AI Voice Clone - Gradio Web Interface
Clone voices and synthesize speech with a beautiful UI
"""
import os
import gradio as gr
from synthesize import VoiceSynthesizer
from clone_voice import VoiceCloner

# Global instances
synthesizer = None
cloner = None


def synthesize_speech(text, language="en", speed=1.0):
    """Synthesize speech from text"""
    global synthesizer

    if not text:
        return None, "⚠️  Please enter text to synthesize"

    try:
        synthesizer = VoiceSynthesizer()
        result = synthesizer.synthesize(
            text=text,
            output_path="/tmp/output.wav",
            language=language,
            speed=speed
        )

        if result["status"] == "success":
            return result["output"], f"✅ Generated: {result['output']}"
        else:
            return None, f"⚠️  {result.get('message', 'Demo mode')}"

    except Exception as e:
        return None, f"❌ Error: {str(e)}"


def clone_voice_fn(audio_file):
    """Clone voice from audio"""
    global cloner

    if audio_file is None:
        return "⚠️  Please upload an audio file"

    try:
        cloner = VoiceCloner()
        result = cloner.clone_from_audio(audio_file)

        if result["status"] == "success":
            return f"✅ Voice cloned: {result.get('model_path', 'Model created')}"
        elif result["status"] == "demo_mode":
            return f"⚠️  {result['message']} - Install Coqui TTS for full functionality"
        else:
            return f"❌ {result.get('message', 'Error')}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Build Gradio Interface
with gr.Blocks(title="AI Voice Clone", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🎤 AI Voice Clone")
    gr.Markdown("Clone any voice with AI and synthesize speech in multiple languages")

    with gr.Tab("🎙️ Synthesize"):
        gr.Markdown("### Text to Speech")

        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    label="Text to Synthesize",
                    placeholder="Enter text here...",
                    lines=4
                )

                with gr.Row():
                    language = gr.Dropdown(
                        ["en", "ar", "es", "fr", "de", "it", "pt", "zh", "ja", "ko"],
                        value="en",
                        label="Language"
                    )
                    speed = gr.Slider(0.5, 2.0, value=1.0, step=0.1, label="Speed")

                synthesize_btn = gr.Button("🎵 Generate Speech", variant="primary")

            with gr.Column():
                audio_output = gr.Audio(label="Generated Audio")
                status_output = gr.Textbox(label="Status", lines=2)

        synthesize_btn.click(
            synthesize_speech,
            inputs=[text_input, language, speed],
            outputs=[audio_output, status_output]
        )

    with gr.Tab("🎭 Clone Voice"):
        gr.Markdown("### Voice Cloning")

        gr.Markdown("""
        **Instructions:**
        1. Upload an audio file (10-30 seconds recommended)
        2. Click "Clone Voice"
        3. Use the cloned voice in the Synthesize tab
        """)

        with gr.Row():
            with gr.Column():
                audio_input = gr.Audio(
                    label="Voice Sample (WAV/MP3)",
                    type="filepath"
                )
                clone_btn = gr.Button("🎤 Clone Voice", variant="primary")

            with gr.Column():
                clone_status = gr.Textbox(label="Status", lines=3)

        clone_btn.click(
            clone_voice_fn,
            inputs=[audio_input],
            outputs=[clone_status]
        )

    with gr.Tab("ℹ️ Info"):
        gr.Markdown("""
        ## AI Voice Clone

        A powerful voice cloning and synthesis tool:
        - 🎯 **Voice Cloning** - Clone from 10-30 seconds of audio
        - 🌍 **Multi-language** - 10+ languages supported
        - ⚡ **Fast Processing** - Generate speech in seconds
        - 🔊 **High Quality** - 44.1kHz output

        ### Supported Languages
        | Code | Language |
        |------|----------|
        | en | English |
        | ar | Arabic |
        | es | Spanish |
        | fr | French |
        | de | German |
        | it | Italian |
        | pt | Portuguese |
        | zh | Chinese |
        | ja | Japanese |
        | ko | Korean |

        ### Requirements
        - Python 3.10+
        - Coqui TTS
        - FFmpeg

        ⚠️ **Note:** Voice cloning requires significant resources. For best results, use GPU.
        """)

# Launch
if __name__ == "__main__":
    print("🚀 Starting AI Voice Clone Web UI...")
    print("   Open http://localhost:7862 in your browser")
    app.launch(server_name="0.0.0.0", server_port=7862)