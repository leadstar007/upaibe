async function sendPrompt() {
    const prompt = document.getElementById("prompt").value;
    const responseDisplay = document.getElementById("response");
    responseDisplay.textContent = "Thinking...";

    try {
        const res = await fetch("https://upaibe-web-services.onrender.com/gpt", {
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

const BASE_URL = "https://upaibe-web-services.onrender.com";

// Test /report
async function testReport() {
    const focus = document.getElementById("reportFocus").value || "monthly performance";
    const res = await fetch(`${BASE_URL}/report`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ focus })
    });
    const data = await res.json();
    document.getElementById("reportOutput").textContent = JSON.stringify(data, null, 2);
}

// Test /leads/live
async function testLeads() {
    const industry = document.getElementById("leadIndustry").value;
    const location = document.getElementById("leadLocation").value;
    const res = await fetch(`${BASE_URL}/leads/live`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ industry, location })
    });
    const data = await res.json();
    document.getElementById("leadsOutput").textContent = JSON.stringify(data, null, 2);
}

// Test /email/followup
async function testFollowupEmail() {
    const lead = document.getElementById("leadInfo").value;
    let parsed = {};
    try {
        parsed = JSON.parse(lead);
    } catch (e) {
        return alert("Invalid JSON in lead info");
    }

    const res = await fetch(`${BASE_URL}/email/followup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lead: parsed })
    });
    const data = await res.json();
    document.getElementById("emailOutput").textContent = JSON.stringify(data, null, 2);
}

// Test /onboarding/quiz
async function testOnboardingQuiz() {
    const industry = document.getElementById("quizIndustry").value || "general";
    const res = await fetch(`${BASE_URL}/onboarding/quiz`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ industry })
    });
    const data = await res.json();
    document.getElementById("quizOutput").textContent = JSON.stringify(data, null, 2);
}
