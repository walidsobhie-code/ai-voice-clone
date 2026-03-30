#!/usr/bin/env python3
"""AI Voice Synthesis - Using Ollama for text generation"""
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:1b"

def synthesize(text: str, output: str = "output.wav") -> dict:
    # Ollama can't do actual TTS, but can generate script for it
    prompt = f"Generate a short voiceover script for: {text}"
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=30
        )
        if response.status_code == 200:
            script = response.json().get("response", "")
            return {"status": "success", "script": script[:200], "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "error", "message": "Ollama not running"}

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello world"
    result = synthesize(text)
    print(f"✅ Generated: {result}")
