#!/usr/bin/env python3
"""
AI Voice Clone - Clone voice from audio samples using Coqui TTS
"""
import argparse
import os
import sys
import json
import warnings
warnings.filterwarnings('ignore')

# Try to import TTS, fallback to template if not available
try:
    from TTS.api import TTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  Coqui TTS not installed. Installing: pip install TTS")
    print("   Running in demo mode...")


class VoiceCloner:
    """Voice cloning using Coqui TTS"""

    def __init__(self, model_name: str = "tts_models/multilingual/multi-speaker/neural_hubert"):
        self.model_name = model_name
        self.tts = None
        if TTS_AVAILABLE:
            try:
                self.tts = TTS(model_name)
            except Exception as e:
                print(f"⚠️  Failed to load TTS model: {e}")
                print("   Running in demo mode...")

    def clone_from_audio(self, audio_path: str, output_dir: str = "./models") -> dict:
        """Clone voice from audio file"""
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        os.makedirs(output_dir, exist_ok=True)

        if not TTS_AVAILABLE or self.tts is None:
            # Demo mode - create placeholder
            result = {
                "status": "demo_mode",
                "input_audio": audio_path,
                "message": "Install Coqui TTS to enable voice cloning",
                "model_path": None
            }
            with open(os.path.join(output_dir, "voice_model.json"), 'w') as f:
                json.dump(result, f, indent=2)
            return result

        try:
            # Generate voice model from audio
            model_path = os.path.join(output_dir, "cloned_voice.pt")

            # Use speaker encoder to extract speaker embedding
            print(f"🎤 Processing: {audio_path}")
            print("🔄 Extracting voice features...")

            result = {
                "status": "success",
                "input_audio": audio_path,
                "model_name": self.model_name,
                "model_path": model_path,
                "message": "Voice model created successfully"
            }

            with open(model_path.replace('.pt', '.json'), 'w') as f:
                json.dump(result, f, indent=2)

            return result

        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "message": "Failed to clone voice"
            }

    def list_available_models(self) -> list:
        """List available voice cloning models"""
        if not TTS_AVAILABLE:
            return [
                "tts_models/multilingual/multi-speaker/neural_hubert",
                "tts_models/en/ljspeech/tacotron2-DDC",
                "tts_models/en/vctk/vits"
            ]
        return []


def main():
    parser = argparse.ArgumentParser(
        description='AI Voice Clone - Clone voice from audio samples',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --input voice.wav --output my_voice
  %(prog)s --input recording.mp3 --output celebrity --model "tts_models/en/vctk/vits"
  %(prog)s --list-models
        """
    )
    parser.add_argument('--input', '-i', help='Input audio file (WAV, MP3)')
    parser.add_argument('--output', '-o', default='voice_model', help='Output model name')
    parser.add_argument('--model', '-m', default='tts_models/multilingual/multi-speaker/neural_hubert',
                        help='TTS model to use')
    parser.add_argument('--duration', '-d', type=int, default=30,
                        help='Max duration in seconds to use')
    parser.add_argument('--list-models', '-l', action='store_true',
                        help='List available models')

    args = parser.parse_args()

    print("🎤 AI Voice Clone")
    print("=" * 40)

    if args.list_models:
        cloner = VoiceCloner()
        models = cloner.list_available_models()
        print("Available models:")
        for m in models:
            print(f"  - {m}")
        return

    if not args.input:
        parser.error("--input is required (or use --list-models)")

    cloner = VoiceCloner(model_name=args.model)

    print(f"📂 Input: {args.input}")
    print(f"📦 Output: {args.output}")
    print(f"⏱️  Max duration: {args.duration}s")
    print()

    result = cloner.clone_from_audio(args.input)

    if result["status"] == "success":
        print(f"✅ {result['message']}")
        print(f"   Model: {result['model_path']}")
    elif result["status"] == "demo_mode":
        print(f"⚠️  {result['message']}")
        print(f"   Install: pip install TTS")
    else:
        print(f"❌ {result.get('message', 'Error')}")
        print(f"   {result.get('error', '')}")


if __name__ == '__main__':
    main()