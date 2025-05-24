async function submitForm() {
    const form = document.getElementById("dizzinessForm");
    const data = new FormData(form);
    const entries = Object.fromEntries(data.entries());

    document.getElementById("responseBox").textContent = "Processing...";

    const response = await fetch("/diagnose", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(entries)
    });

    const result = await response.json();

    if (result.error) {
        document.getElementById("responseBox").textContent = "Error: " + result.error;
    } else {
        document.getElementById("responseBox").textContent = result.result;
    }
}