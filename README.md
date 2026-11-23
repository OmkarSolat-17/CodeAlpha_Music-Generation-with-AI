# 🎵 AI Music Generation

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Model-MusicGen-FF6F00?style=flat-square&logo=huggingface&logoColor=white" alt="MusicGen">
  <img src="https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</p>

<p align="center">
  <b>Generate music from text descriptions using Meta's MusicGen model.</b><br>
  <sub>AI-powered text-to-music web application with mood, genre, and duration controls.</sub>
</p>

---

## ✨ Features

- Generate music from natural language descriptions
- Mood and genre selection controls
- Adjustable music duration
- AI-generated audio playback in browser
- Download generated music in WAV format
- Interactive web interface

## 🛠️ Tech Stack

| Component | Technology |
|:----------|:-----------|
| **Backend** | Python, Flask |
| **AI Model** | Meta MusicGen-small |
| **ML Framework** | PyTorch, Hugging Face Transformers |
| **Audio** | SciPy (WAV processing) |
| **Frontend** | HTML5, CSS3, JavaScript |

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/OmkarSolat-17/CodeAlpha_Music-Generation-with-AI.git
cd CodeAlpha_Music-Generation-with-AI
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

Visit: `http://127.0.0.1:5000`

## 🧠 How It Works

```
Text Prompt → Mood/Genre/Duration Settings → MusicGen Model → Audio Output → WAV File
                                                    ↓
                                         Hugging Face Transformers
```

1. User enters a text description of the desired music
2. Mood, genre, and duration settings are configured
3. The prompt is passed to Meta's MusicGen-small model via Hugging Face Transformers
4. The model generates raw audio based on the text prompt
5. Audio is converted to WAV format using SciPy
6. Generated music can be played in-browser or downloaded

## ⚠️ Requirements

- **Python** 3.10+ with compatible PyTorch and Transformers versions
- **Internet connection** for initial model download (~2 GB)
- **RAM:** 8 GB+ recommended (model is memory-intensive)
- **GPU** optional but recommended for faster generation

> **Note:** Music generation is computationally intensive, especially on CPU. First run downloads the pretrained model.

## 📂 Project Structure

```
CodeAlpha_Music-Generation-with-AI/
├── app.py               # Flask application and MusicGen integration
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Web interface template
├── static/
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
└── README.md
```

## 🎯 Project Objective

Explore generative AI and deep learning by building a web application capable of creating music from natural language descriptions using Meta's MusicGen model.

## 👨‍💻 Internship

This project was developed as part of the **Artificial Intelligence Internship at CodeAlpha**.

---

<p align="center">
  <sub>Built by <a href="https://github.com/OmkarSolat-17">Omkar Solat</a> · B.Tech CSE (AI/ML)</sub>
</p>
