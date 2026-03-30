#!/usr/bin/env python3
"""
AI Voice Synthesize - Generate speech using cloned voice
"""
import argparse
import os
import sys
import json
import warnings
warnings.filterwarnings('ignore')

# Try to import TTS
try:
    from TTS.api import TTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False


class VoiceSynthesizer:
    """Speech synthesis using cloned voice"""

    def __init__(self, model_path: str = None):
        self.model_path = model_path
        self.tts = None
        if TTS_AVAILABLE:
            try:
                self.tts = TTS("tts_models/multilingual/multi-speaker/neural_hubert")
            except Exception as e:
                print(f"⚠️  Failed to load TTS: {e}")

    def synthesize(self, text: str, output_path: str = "output.wav",
                   language: str = "en", speed: float = 1.0) -> dict:
        """Synthesize speech from text"""
        if not text:
            raise ValueError("Text cannot be empty")

        if not TTS_AVAILABLE or self.tts is None:
            # Demo mode
            result = {
                "status": "demo_mode",
                "text": text,
                "output": output_path,
                "message": "Install Coqui TTS for real synthesis"
            }
            # Create dummy file
            with open(output_path, 'w') as f:
                f.write(f"DEMO: {text}")
            return result

        try:
            print(f"🔄 Synthesizing: {text[:50]}...")

            # Multi-speaker synthesis
            self.tts.tts_to_file(
                text=text,
                file_path=output_path,
                language=language,
                speed=speed
            )

            file_size = os.path.getsize(output_path) if os.path.exists(output_path) else 0

            result = {
                "status": "success",
                "text": text,
                "output": output_path,
                "language": language,
                "speed": speed,
                "file_size_bytes": file_size
            }

            return result

        except Exception as e:
            return {
                "status": "error",
                "text": text,
                "error": str(e)
            }

    def synthesize_multi_voice(self, text: str, speaker_id: int = 0,
                               output_path: str = "output.wav") -> dict:
        """Synthesize with multiple speakers"""
        if not TTS_AVAILABLE or self.tts is None:
            return {
                "status": "demo_mode",
                "message": "Multi-voice requires Coqui TTS"
            }

        try:
            self.tts.tts_to_file(
                text=text,
                file_path=output_path,
                speaker_id=speaker_id
            )
            return {"status": "success", "output": output_path}
        except Exception as e:
            return {"status": "error", "error": str(e)}


def main():
    parser = argparse.ArgumentParser(
        description='AI Voice Synthesize - Generate speech from text',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --text "Hello world" --output hello.wav
  %(prog)s --text "مرحبا بالعالم" --lang ar --output arabic.wav
  %(prog)s --interactive
        """
    )
    parser.add_argument('--text', '-t', help='Text to synthesize')
    parser.add_argument('--input', '-i', help='Input file with text (one per line)')
    parser.add_argument('--output', '-o', default='output.wav', help='Output audio file')
    parser.add_argument('--lang', '-l', default='en', help='Language code (en, ar, es, fr, de)')
    parser.add_argument('--speed', '-s', type=float, default=1.0, help='Speech speed (0.5-2.0)')
    parser.add_argument('--speaker', type=int, default=0, help='Speaker ID for multi-speaker models')
    parser.add_argument('--interactive', action='store_true', help='Interactive mode')

    args = parser.parse_args()

    print("🎙️ AI Voice Synthesize")
    print("=" * 40)

    synth = VoiceSynthesizer()

    if args.interactive:
        print("Interactive mode. Type 'quit' to exit.")
        print()

        while True:
            text = input("Enter text: ")
            if text.lower() in ('quit', 'exit', 'q'):
                break

            result = synth.synthesize(
                text=text,
                output_path=args.output,
                language=args.lang,
                speed=args.speed
            )

            if result["status"] == "success":
                print(f"✅ Saved to: {result['output']}")
                print(f"   Size: {result['file_size_bytes']} bytes")
            elif result["status"] == "demo_mode":
                print(f"⚠️  {result['message']}")
            else:
                print(f"❌ Error: {result.get('error')}")
            print()

    elif args.input:
        # Process input file
        if not os.path.exists(args.input):
            print(f"❌ File not found: {args.input}")
            sys.exit(1)

        with open(args.input, 'r') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]

        print(f"📄 Processing {len(lines)} lines...")

        for i, line in enumerate(lines):
            output = args.output.replace('.wav', f'_{i}.wav')
            result = synth.synthesize(line, output, args.lang, args.speed)
            print(f"  [{i+1}/{len(lines)}] {line[:30]}... -> {output}")

        print("✅ Done!")

    elif args.text:
        result = synth.synthesize(
            text=args.text,
            output_path=args.output,
            language=args.lang,
            speed=args.speed
        )

        if result["status"] == "success":
            print(f"✅ Speech saved to: {result['output']}")
            print(f"   Size: {result['file_size_bytes']} bytes")
        elif result["status"] == "demo_mode":
            print(f"⚠️  {result['message']}")
            print(f"   Install: pip install TTS")
        else:
            print(f"❌ Error: {result.get('error')}")
    else:
        parser.error("--text, --input, or --interactive required")


if __name__ == '__main__':
    main()