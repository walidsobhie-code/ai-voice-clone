#!/usr/bin/env python3
"""
AI Voice Clone - Gradio UI
Web interface for voice cloning and synthesis
"""
import gradio as gr
import subprocess
import os
import tempfile

def clone_voice(audio_file, model_name):
    """Clone voice from audio file"""
    if audio_file is None:
        return "Please upload an audio file", None
    try:
        # Save uploaded file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
            f.write(audio_file)
            input_path = f.name
        
        # Run clone script
        result = subprocess.run(
            ['python3', 'clone_voice.py', '--input', input_path, '--output', model_name],
            capture_output=True, text=True, timeout=60
        )
        
        os.unlink(input_path)
        
        if result.returncode == 0:
            return f"✅ Voice cloned successfully!\nModel: {model_name}", None
        else:
            return f"⚠️ Template mode - {result.stdout}", None
    except Exception as e:
        return f"❌ Error: {str(e)}", None

def synthesize_speech(model_name, text, voice_speed):
    """Generate speech with cloned voice"""
    if not model_name:
        return "Please enter a model name", None
    if not text:
        return "Please enter text to synthesize", None
    
    try:
        result = subprocess.run(
            ['python3', 'synthesize.py', '--model', model_name, '--text', text, '--output', 'output.wav'],
            capture_output=True, text=True, timeout=60
        )
        
        if result.returncode == 0:
            return f"✅ Generated: {text[:50]}...", 'output.wav'
        else:
            return f"⚠️ Template mode - {result.stdout}", None
    except Exception as e:
        return f"❌ Error: {str(e)}", None

# Gradio Interface
with gr.Blocks(title="AI Voice Clone", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎙️ AI Voice Clone")
    gr.Markdown("Clone any voice with AI. Upload audio → Get voice model → Generate speech!")
    
    with gr.Tab("Clone Voice"):
        with gr.Row():
            with gr.Column():
                audio_input = gr.Audio(label="Upload Audio (10-30 seconds)", type="filepath")
                model_name_clone = gr.Textbox(label="Model Name", placeholder="my_voice_model")
                clone_btn = gr.Button("🔄 Clone Voice", variant="primary")
            with gr.Column():
                clone_output = gr.Textbox(label="Status", lines=3)
        
        clone_btn.click(clone_voice, inputs=[audio_input, model_name_clone], outputs=clone_output)
    
    with gr.Tab("Generate Speech"):
        with gr.Row():
            with gr.Column():
                model_name = gr.Textbox(label="Model Name", placeholder="my_voice_model")
                text_input = gr.Textbox(label="Text to Synthesize", placeholder="Hello friends!", lines=3)
                voice_speed = gr.Slider(minimum=0.5, maximum=2.0, value=1.0, label="Voice Speed")
                generate_btn = gr.Button("🎤 Generate Speech", variant="primary")
            with gr.Column():
                speech_output = gr.Audio(label="Generated Audio")
                speech_status = gr.Textbox(label="Status", lines=2)
        
        generate_btn.click(synthesize_speech, inputs=[model_name, text_input, voice_speed], 
                         outputs=[speech_status, speech_output])
    
    gr.Markdown("---")
    gr.Markdown("💡 **Tip**: Use clear audio with minimal background noise for best results.")

demo.launch(server_name="0.0.0.0", server_port=7860)
