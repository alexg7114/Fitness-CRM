
document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();
    
    if (response.ok) {
        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);
        window.location.href = "dashboard/";  // Weiterleitung zum Dashboard
        //window.location.href = "http://127.0.0.1:5500/dashboard.html";

    } else {
        alert("Login fehlgeschlagen");
    }
});

