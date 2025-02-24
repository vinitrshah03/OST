document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded");

    // Sidebar Toggle
    const showAsideBtn = document.querySelector('.show-side-btn');
    const sidebar = document.querySelector('.sidebar');
    const wrapper = document.getElementById('wrapper');

    showAsideBtn.addEventListener('click', function () {
        sidebar.classList.toggle('show-sidebar');
        wrapper.classList.toggle('fullwidth');
    });

    // Sidebar Dropdown Menu
    document.querySelectorAll('.has-dropdown > a').forEach(item => {
        item.addEventListener('click', function (event) {
            event.preventDefault();
            const parent = this.parentElement;
            parent.classList.toggle('opened');

            // Close other dropdowns
            document.querySelectorAll('.has-dropdown').forEach(sibling => {
                if (sibling !== parent) sibling.classList.remove('opened');
            });
        });
    });

    // Close Sidebar
    document.querySelector('.close-aside').addEventListener('click', function () {
        sidebar.classList.remove('show-sidebar');
        wrapper.classList.remove('fullwidth');
    });

    // Dark Mode Toggle
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const body = document.body;
    const lightLabel = document.getElementById("light-label");
    const darkLabel = document.getElementById("dark-label");

    // Load dark mode preference
    if (localStorage.getItem("dark-mode") === "enabled") {
        body.classList.add("dark-mode");
        darkModeToggle.checked = true;
        lightLabel.style.opacity = "0.3";
        darkLabel.style.opacity = "1";
    } else {
        lightLabel.style.opacity = "1";
        darkLabel.style.opacity = "0.3";
    }

    darkModeToggle.addEventListener("change", function () {
        if (this.checked) {
            body.classList.add("dark-mode");
            localStorage.setItem("dark-mode", "enabled");
            lightLabel.style.opacity = "0.3";
            darkLabel.style.opacity = "1";
        } else {
            body.classList.remove("dark-mode");
            localStorage.setItem("dark-mode", "disabled");
            lightLabel.style.opacity = "1";
            darkLabel.style.opacity = "0.3";
        }
    });

    // Lazy load images
    document.querySelectorAll("img").forEach(img => {
        img.loading = "lazy";
    });
});