#!/usr/bin/env python3
"""Basic voice cloning example"""
import sys
sys.path.insert(0, '..')

from clone_voice import VoiceCloner

def main():
    # Initialize the voice cloner
    cloner = VoiceCloner()

    # Clone a voice from audio file
    print("Cloning voice from sample audio...")
    result = cloner.clone_from_audio(
        audio_path="sample_voice.wav",
        output_dir="./my_voice_model"
    )

    print(f"Result: {result}")

    if result["status"] == "success":
        print(f"✅ Voice model created at: {result['model_path']}")
    else:
        print(f"⚠️  {result.get('message', 'Demo mode')}")


if __name__ == "__main__":
    main()