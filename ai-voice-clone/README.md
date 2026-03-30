# AI Voice Clone 🎤

Clone any voice with AI using advanced TTS models. Create realistic synthetic speech that sounds like anyone.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/walidsobhie-code/ai-voice-clone)](https://github.com/walidsobhie-code/ai-voice-clone/stargazers)

## Why Voice Cloning?

Voice cloning is revolutionizing:
- **Content Creation** - Localize videos in any language
- **Accessibility** - Help people with speech impairments
- **Entertainment** - Create voiceovers for podcasts
- **Education** - Generate personalized audio content

Inspired by [Coqui TTS](https://github.com/coqui-ai/TTS) (28k+ stars) and [VibeVoice](https://github.com/PhamPhuc98/VibeVoice).

## Features

- 🎯 **Voice Cloning** - Clone voice from 10-30 seconds of audio
- 🌍 **Multi-language** - English, Arabic, Spanish, French, German, Chinese
- ⚡ **Fast Processing** - Generate speech in seconds
- 🔊 **High Quality** - 44.1kHz audio output
- 🔒 **Privacy-first** - Local processing (no cloud calls)
- 🖥️ **CLI Interface** - Easy command-line usage

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Clone a voice from audio sample
python clone_voice.py --input my_voice.wav --output my_voice

# Synthesize speech with cloned voice
python synthesize.py --text "Hello world!" --output hello.wav

# Interactive mode
python synthesize.py --interactive
```

## Installation

### Requirements
- Python 3.10+
- FFmpeg (for audio processing)

```bash
# Install FFmpeg
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
choco install ffmpeg
```

### Python Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Clone Voice
```bash
python clone_voice.py --input voice_sample.wav --output my_model

# Specify model
python clone_voice.py --input voice.wav --model "tts_models/en/vctk/vits"

# List available models
python clone_voice.py --list-models
```

### Synthesize Speech
```bash
# Basic synthesis
python synthesize.py --text "Hello, this is my cloned voice!" --output speech.wav

# Multi-language
python synthesize.py --text "مرحبا بالعالم" --lang ar --output arabic.wav
python synthesize.py --text "Bonjour le monde" --lang fr --output french.wav

# Adjust speed
python synthesize.py --text "Hello" --speed 0.8 --output slow.wav
python synthesize.py --text "Hello" --speed 1.2 --output fast.wav

# Batch processing
python synthesize.py --input text_file.txt --output audio.wav
```

## Command Reference

### clone_voice.py
| Option | Alias | Description | Default |
|--------|-------|-------------|---------|
| `--input` | `-i` | Input audio file | Required |
| `--output` | `-o` | Output model name | `voice_model` |
| `--model` | `-m` | TTS model to use | Default model |
| `--duration` | `-d` | Max audio duration (sec) | 30 |
| `--list-models` | `-l` | List available models | - |

### synthesize.py
| Option | Alias | Description | Default |
|--------|-------|-------------|---------|
| `--text` | `-t` | Text to synthesize | - |
| `--input` | `-i` | Input text file | - |
| `--output` | `-o` | Output audio file | `output.wav` |
| `--lang` | `-l` | Language code | `en` |
| `--speed` | `-s` | Speech speed (0.5-2.0) | 1.0 |
| `--speaker` | - | Speaker ID | 0 |
| `--interactive` | - | Interactive mode | - |

## Supported Languages

| Code | Language |
|------|----------|
| `en` | English |
| `ar` | Arabic |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `it` | Italian |
| `pt` | Portuguese |
| `pl` | Polish |
| `ru` | Russian |
| `zh` | Chinese |
| `ja` | Japanese |
| `ko` | Korean |

## Examples

See [`examples/`](examples/) for more use cases:

- `examples/basic_clone.py` - Basic voice cloning
- `examples/multi_language.py` - Multi-language synthesis
- `examples/batch_processing.py` - Process multiple files
- `examples/custom_model.py` - Use custom TTS models

## Documentation

- [Getting Started](docs/getting-started.md)
- [API Reference](docs/api.md)
- [FAQ](docs/faq.md)
- [Contributing](CONTRIBUTING.md)

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Audio Input │───▶│ Voice Clone  │───▶│ Voice Model │
└─────────────┘    └──────────────┘    └─────────────┘
                                               │
                                               ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   Text      │───▶│  Synthesize  │───▶│ Audio Output│
└─────────────┘    └──────────────┘    └─────────────┘
```

## Troubleshooting

### "TTS not found"
```bash
pip install TTS
```

### "FFmpeg not found"
```bash
# macOS
brew install ffmpeg

# Ubuntu
sudo apt install ffmpeg
```

### CUDA out of memory
```bash
# Use CPU mode
export CUDA_VISIBLE_DEVICES=""
python synthesize.py --text "Hello"
```

## Performance

- Voice cloning: ~30 seconds for 30s audio
- Synthesis: ~2-5 seconds per sentence
- Memory: 2-4GB RAM, 4GB+ VRAM for GPU

## License

MIT License - see [LICENSE](LICENSE)

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md).

## Star if Helpful!

If this project helps you, please ⭐ star the repo!

---

<p align="center">
  Built with ❤️ using <a href="https://github.com/coqui-ai/TTS">Coqui TTS</a>
</p>