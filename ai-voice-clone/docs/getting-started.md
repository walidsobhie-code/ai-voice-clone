# Getting Started with AI Voice Clone

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/walidsobhie-code/ai-voice-clone.git
cd ai-voice-clone
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Install FFmpeg** (required for audio processing)

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg
```

**Windows:**
```bash
choco install ffmpeg
```

## Quick Start

### 1. Clone a Voice

```bash
python clone_voice.py --input my_voice.wav --output my_voice_model
```

This will create a voice model from your audio sample (10-30 seconds recommended).

### 2. Synthesize Speech

```bash
python synthesize.py --text "Hello world!" --output hello.wav
```

### 3. Interactive Mode

```bash
python synthesize.py --interactive
```

Type any text and hear it in your cloned voice!

## Supported Languages

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

## Troubleshooting

### Out of Memory
If you run out of GPU memory, use CPU mode:
```bash
export CUDA_VISIBLE_DEVICES=""
python synthesize.py --text "Hello"
```

### Audio Quality Issues
- Use high-quality audio (44.1kHz, WAV format)
- Avoid background noise
- Keep audio duration between 10-30 seconds