# 🎵 AI Music Generation (Task 3)

An AI-powered text-to-music generation web application that creates music based on user-provided text prompts. The application uses Meta's MusicGen model through Hugging Face Transformers.

## ✨ Features

- Generate music from text descriptions
- Mood and genre selection
- Adjustable music duration
- AI-generated audio playback
- Download generated music in WAV format
- Interactive web interface

## 🛠️ Tech Stack

- **Python** – Backend development
- **Flask** – Web framework
- **Meta MusicGen-small** – Music generation model
- **Hugging Face Transformers** – AI model integration
- **PyTorch** – Deep learning framework
- **SciPy** – WAV audio file processing
- **HTML5, CSS3, JavaScript** – Frontend

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/OmkarSolat-17/CodeAlpha_MusicGeneration.git
cd CodeAlpha_MusicGeneration
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

Visit:

```text
http://127.0.0.1:5000
```

## 🧠 How It Works

1. The user enters a music description.
2. Mood, genre, and duration settings are selected.
3. The text prompt is passed to the MusicGen model.
4. The model generates audio based on the prompt.
5. The generated music can be played or downloaded.

## ⚠️ Requirements

- Python environment with compatible PyTorch and Transformers versions
- Internet connection for downloading the pretrained model initially
- Sufficient RAM and processing power for audio generation

**Note:** Music generation can be computationally intensive, especially on CPU-based systems.

## 📂 Project Structure

```text
CodeAlpha_MusicGeneration/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## 🎯 Project Objective

To explore generative AI and deep learning by building a web application capable of creating music from natural language descriptions.

## 👨‍💻 Internship

This project was developed as part of the **Artificial Intelligence Internship at CodeAlpha**.

---

⭐ If you find this project interesting, consider giving it a star!
