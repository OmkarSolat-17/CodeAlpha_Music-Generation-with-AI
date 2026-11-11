
const generateBtn = document.getElementById("generateBtn");

const promptInput = document.getElementById("prompt");
const moodSelect = document.getElementById("mood");
const genreSelect = document.getElementById("genre");
const durationSelect = document.getElementById("duration");

const loading = document.getElementById("loading");
const result = document.getElementById("result");
const errorBox = document.getElementById("error");

const audioPlayer = document.getElementById("audioPlayer");
const downloadBtn = document.getElementById("downloadBtn");
const resultPrompt = document.getElementById("resultPrompt");


generateBtn.addEventListener("click", async () => {

    const prompt = promptInput.value.trim();

    if (!prompt) {
        showError("Please describe the music you want to generate.");
        promptInput.focus();
        return;
    }

    result.classList.add("hidden");
    errorBox.classList.add("hidden");
    loading.classList.remove("hidden");

    generateBtn.disabled = true;
    generateBtn.innerHTML = "♫ Generating your music...";

    try {

        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                prompt: prompt,
                mood: moodSelect.value,
                genre: genreSelect.value,
                duration: durationSelect.value
            })
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            throw new Error(data.message || "Music generation failed.");
        }

        audioPlayer.src = data.audio_url;
        audioPlayer.load();

        downloadBtn.href = data.audio_url;
        downloadBtn.download = data.filename;

        resultPrompt.textContent = data.prompt;

        result.classList.remove("hidden");

        result.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });

    } catch (error) {

        showError(error.message);

    } finally {

        loading.classList.add("hidden");

        generateBtn.disabled = false;

        generateBtn.innerHTML =
            '<span class="button-icon">♫</span>' +
            'Generate Music' +
            '<span class="button-arrow">→</span>';
    }
});


function showError(message) {
    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
}
