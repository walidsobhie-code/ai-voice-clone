#!/usr/bin/env python3
"""
AI Voice Synthesis - Generate speech with cloned voice
"""
import os
import argparse

try:
    from TTS.api import TTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

def synthesize(model_path: str, text: str, output: str = "output.wav", speed: float = 1.0) -> dict:
    """Generate speech with cloned voice"""
    if not TTS_AVAILABLE:
        return {
            "status": "template",
            "message": "Install TTS: pip install TTS",
            "model": model_path,
            "text": text
        }
    
    try:
        tts = TTS(model_name="xtts", progress_bar=True)
        
        print(f"🎤 Synthesizing: {text[:50]}...")
        tts.tts_to_file(
            text=text,
            speaker_wav=model_path if os.path.exists(model_path) else None,
            file_path=output,
            speed=speed
        )
        
        return {"status": "success", "output": output}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description="AI Voice Synthesis")
    parser.add_argument("--model", "-m", default="cloned_voice.wav", help="Voice model file")
    parser.add_argument("--text", "-t", required=True, help="Text to synthesize")
    parser.add_argument("--output", "-o", default="output.wav", help="Output file")
    parser.add_argument("--speed", "-s", type=float, default=1.0, help="Speech speed (0.5-2.0)")
    args = parser.parse_args()
    
    result = synthesize(args.model, args.text, args.output, args.speed)
    
    if result["status"] == "success":
        print(f"✅ Generated: {result['output']}")
    else:
        print(f"⚠️ {result.get('message', 'Error')}")

if __name__ == "__main__":
    main()
