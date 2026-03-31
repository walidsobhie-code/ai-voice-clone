# 🎙️ AI Voice Clone

> **Clone any voice with AI** — Create personalized voice synthesis from just 10-30 seconds of audio. Powered by Coqui XTTS.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![Try on HF](https://img.shields.io/huggingface/spaces/walidsobhie/ai-voice-clone?color=blue&label=Try+Live+Demo)](https://huggingface.co/spaces/walidsobhie/ai-voice-clone)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/walidsobhie-code/ai-voice-clone)](https://github.com/walidsobhie-code/ai-voice-clone/stargazers)

## 🎯 What It Does

```
Step 1: Upload 10s of audio  →  "This is my voice"
Step 2: AI clones the voice
Step 3: Generate anything   →  "Hello, I am cloned!"
```

**Voice AI is exploding** — from content creation to accessibility, voice cloning is revolutionizing communication.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Voice Cloning** | Clone from 10-30 seconds of audio |
| 🌍 **Multi-language** | English, Arabic, Spanish, French, German |
| ⚡ **Fast** | Generate speech in seconds |
| 🔊 **High Quality** | 44.1kHz output |
| 🎛️ **Gradio UI** | Beautiful web interface |
| 🐳 **Docker** | One-command deployment |

## 🚀 Quick Start

### Install
```bash
git clone https://github.com/walidsobhie-code/ai-voice-clone.git
cd ai-voice-clone
pip install -r requirements.txt
```

### Clone a Voice
```bash
# Upload 10-30 seconds of clear audio
python clone_voice.py --input my_voice.wav --output my_cloned_voice

# Output:
# 🎤 Loading audio: my_voice.wav
# 🔄 Cloning voice...
# ✅ Voice cloned successfully!
```

### Generate Speech
```bash
python synthesize.py --model my_cloned_voice.wav \
    --text "Hello everyone, this is my cloned voice!" \
    --output hello.wav
```

### Use Web UI
```bash
python gradio_app.py
# Opens: http://localhost:7860
```

## 🎨 Web UI Demo

```
┌─────────────────────────────────────────────────────────┐
│  🎙️ AI Voice Clone                                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [🎤 Clone Voice]        [🎤 Generate Speech]        │
│                                                          │
│  ┌──────────────────┐     ┌──────────────────┐          │
│  │ Upload Audio:   │     │ Text Input:    │          │
│  │ [my_voice.wav]  │     │ Hello world!   │          │
│  │ Duration: 15s   │     │ Speed: [1.0x]  │          │
│  └──────────────────┘     └──────────────────┘          │
│                                                          │
│  [🔄 Clone Voice]          [🎤 Generate]              │
│                                                          │
│  Status:                                               │
│  ✅ Voice cloned successfully!                          │
│  📊 Model: my_cloned_voice                           │
└─────────────────────────────────────────────────────────┘
```

## 💻 Python API

```python
from clone_voice import clone_voice
from synthesize import synthesize

# Step 1: Clone voice
result = clone_voice(
    input_file="my_voice.wav",
    output_name="my_model"
)
print(result)
# {'status': 'success', 'output': 'my_model.wav'}

# Step 2: Generate speech
result = synthesize(
    model_path="my_model.wav",
    text="Hello, I sound exactly like the original!",
    output="output.wav"
)
print(result)
# {'status': 'success', 'output': 'output.wav'}
```

## 🎯 Use Cases

| Industry | Use Case |
|----------|----------|
| 🎬 **Content** | Create videos with any voice |
| 🎧 **Podcast** | Clone voices for narration |
| ♿ **Accessibility** | Read text in any voice |
| 🏢 **Brand** | Consistent brand voice across content |
| 📚 **Education** | Localize content in local voices |
| 🎮 **Gaming** | Character voices for games |

## 🔬 How It Works

```
Original Audio (10-30s)
         ↓
 XTTS Encoder (extracts voiceprint)
         ↓
 Latent Space Representation
         ↓
 XTTS Decoder (generates new audio)
         ↓
 Your Cloned Voice Saying Anything!
```

## 🐳 Docker

```bash
# Build
docker build -t voice-clone .

# Run
docker run -p 7860:7860 voice-clone
```

## 📁 Project Structure

```
ai-voice-clone/
├── clone_voice.py      # Voice cloning
├── synthesize.py       # Speech synthesis
├── gradio_app.py       # Web UI
├── requirements.txt
├── Dockerfile
└── examples/
    ├── basic_clone.py
    └── multi_language.py
```

## ⚠️ Ethical Use

This tool should only be used ethically:
- ✅ With consent of the voice owner
- ✅ For legitimate purposes (accessibility, entertainment)
- ❌ NOT for fraud, impersonation, or deception

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## ⭐ Support

If this helped you, please star the repo!

---

**Built with ❤️ by [walidsobhie-code](https://github.com/walidsobhie-code)**

## 🗺️ Roadmap

- [ ] [Planned] Web version / hosted demo
- [ ] [Planned] API endpoint for production use
- [ ] [Planned] Support for more languages
- [ ] [In Progress] Performance optimizations
- [ ] [Done] Gradio web interface
- [ ] [Done] Docker deployment

## 🏢 Used By

> Have a project using this? Send a PR to add your company!

- *(coming soon — be the first to list your project!)*

## 🤝 Contributors

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

[![GitHub Contributors](https://contrib.rocks/image?repo=my-ai-stack/ai-voice-clone)](https://github.com/my-ai-stack/ai-voice-clone/graphs/contributors)
