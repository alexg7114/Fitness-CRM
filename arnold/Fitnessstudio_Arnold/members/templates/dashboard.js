
async function fetchDashboard() {
    const token = localStorage.getItem("access");

    const response = await fetch("http://127.0.0.1:8000/api/dashboard/", {
        method: "GET",
        headers: { "Authorization": `Bearer ${token}` }
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById("message").innerText = `Willkommen, ${data.user}`;
    } else {
        alert("Nicht autorisiert! Bitte logge dich erneut ein.");
        window.location.href = "login.html";
    }
}

function logout() {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "login.html";
}

fetchDashboard();
