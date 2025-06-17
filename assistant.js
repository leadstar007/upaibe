async function sendPrompt() {
    const prompt = document.getElementById("prompt").value;
    const responseDisplay = document.getElementById("response");
    responseDisplay.textContent = "Thinking...";

    try {
        const res = await fetch("https://upaibe-app.onrender.com/gpt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const data = await res.json();
        responseDisplay.textContent = data.response || data.error || "No response";
    } catch (err) {
        responseDisplay.textContent = "Error: " + err.message;
    }
}