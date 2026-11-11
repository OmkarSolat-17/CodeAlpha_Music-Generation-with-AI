
import os
import uuid
import torch
import numpy as np

from flask import Flask, render_template, request, jsonify, send_from_directory
from transformers import MusicgenForConditionalGeneration, AutoProcessor
from scipy.io.wavfile import write as write_wav


# --------------------------------------------------
# Flask Application Setup
# --------------------------------------------------

app = Flask(__name__)

GENERATED_DIR = "generated"
os.makedirs(GENERATED_DIR, exist_ok=True)


# --------------------------------------------------
# AI MusicGen Model Setup
# --------------------------------------------------

MODEL_NAME = "facebook/musicgen-small"

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"\nLoading MusicGen model on {device}...")
print("This may take some time during the first run.\n")

processor = AutoProcessor.from_pretrained(MODEL_NAME)

model = MusicgenForConditionalGeneration.from_pretrained(
    MODEL_NAME
).to(device)

model.eval()

print("\nMusicGen model loaded successfully!")
print(f"Running on: {device}\n")


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# Generate AI Music
# --------------------------------------------------

@app.route("/generate", methods=["POST"])
def generate_music():

    try:

        # Get user input
        data = request.get_json()

        prompt = data.get("prompt", "").strip()
        mood = data.get("mood", "Calm")
        genre = data.get("genre", "Classical")
        duration = int(data.get("duration", 8))

        # Validate prompt
        if not prompt:

            return jsonify({
                "success": False,
                "message": "Please enter a music description."
            }), 400

        # Limit duration
        duration = max(5, min(duration, 15))

        # Build final prompt
        full_prompt = (
            f"{genre} music, {mood} mood. "
            f"{prompt}. Instrumental music."
        )

        print("\nGenerating music...")
        print(f"Prompt: {full_prompt}")
        print(f"Duration: {duration} seconds")

        # --------------------------------------------------
        # Prepare Input
        # --------------------------------------------------

        inputs = processor(
            text=[full_prompt],
            padding=True,
            return_tensors="pt"
        ).to(device)

        # Approximately 50 audio tokens per second
        max_new_tokens = duration * 50

        # --------------------------------------------------
        # AI Music Generation
        # --------------------------------------------------

        with torch.no_grad():

            audio_values = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                guidance_scale=3
            )

        # --------------------------------------------------
        # Audio Processing
        # --------------------------------------------------

        audio = audio_values[0].detach().cpu().numpy()

        # Convert audio to mono
        if audio.ndim == 2:

            # Expected MusicGen format: (channels, samples)
            if audio.shape[0] <= 2:

                audio = np.mean(audio, axis=0)

            # Alternative format: (samples, channels)
            elif audio.shape[1] <= 2:

                audio = np.mean(audio, axis=1)

            else:

                raise ValueError(
                    f"Unexpected audio shape: {audio.shape}"
                )

        elif audio.ndim != 1:

            raise ValueError(
                f"Unexpected audio dimensions: {audio.shape}"
            )

        # Replace invalid values
        audio = np.nan_to_num(
            audio,
            nan=0.0,
            posinf=1.0,
            neginf=-1.0
        )

        # Normalize audio range
        audio = np.clip(audio, -1.0, 1.0)

        # Convert to 16-bit PCM format
        audio = (audio * 32767).astype(np.int16)

        # --------------------------------------------------
        # Save WAV File
        # --------------------------------------------------

        sample_rate = int(
            model.config.audio_encoder.sampling_rate
        )

        filename = f"music_{uuid.uuid4().hex[:10]}.wav"

        filepath = os.path.join(
            GENERATED_DIR,
            filename
        )

        # Save mono WAV audio
        write_wav(
            filepath,
            sample_rate,
            audio
        )

        print("\nMusic generated successfully!")
        print(f"Saved file: {filepath}")

        # --------------------------------------------------
        # Return Result
        # --------------------------------------------------

        return jsonify({

            "success": True,

            "message": "Your music has been generated!",

            "audio_url": f"/audio/{filename}",

            "filename": filename,

            "prompt": full_prompt

        })

    except Exception as e:

        print("\nMusic generation error:")
        print(str(e))

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


# --------------------------------------------------
# Serve Generated Audio
# --------------------------------------------------

@app.route("/audio/<filename>")
def serve_audio(filename):

    return send_from_directory(
        GENERATED_DIR,
        filename,
        as_attachment=False
    )


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )
