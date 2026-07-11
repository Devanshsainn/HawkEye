document.addEventListener("DOMContentLoaded", () => {

    // Initialize Lucide Icons
    if (window.lucide) {
        lucide.createIcons();
    }

    // Fade-up animation
    document.querySelectorAll(".fade-up").forEach((element, index) => {
        element.style.animationDelay = `${index * 120}ms`;
    });

    const form = document.querySelector("form");

    if (!form) return;

    const button = form.querySelector("button");
    const input = form.querySelector("input[name='domain']");

    form.addEventListener("submit", function (e) {

        if (!input.value.trim()) {
            e.preventDefault();
            input.focus();
            return;
        }

        const originalText = button.innerHTML;

        button.disabled = true;

        button.innerHTML = `
            <span style="display:flex;align-items:center;justify-content:center;gap:10px;">
                <span class="spinner"></span>
                Scanning...
            </span>
        `;

        // Loading Overlay
        const overlay = document.createElement("div");
        overlay.id = "scanOverlay";

        overlay.innerHTML = `
            <div class="scan-box">

                <h2>HawkEye</h2>

                <p id="scanStatus">
                    Initializing Scan...
                </p>

                <div class="progress">

                    <div class="progress-bar"></div>

                </div>

            </div>
        `;

        document.body.appendChild(overlay);

        const steps = [
            "Resolving domain...",
            "Checking SSL Certificate...",
            "Inspecting Security Headers...",
            "Checking robots.txt...",
            "Checking sitemap.xml...",
            "Calculating Security Score...",
            "Generating Report..."
        ];

        let current = 0;

        const status = document.getElementById("scanStatus");

        const interval = setInterval(() => {

            if (current < steps.length) {

                status.innerText = steps[current];

                current++;

            } else {

                clearInterval(interval);

            }

        }, 300);

    });

});