/*
==========================================
HawkEye
Main JavaScript
==========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    initializeNavbar();

    initializeSmoothScroll();

    initializeRevealAnimations();

});

/* ==========================================
   NAVBAR
========================================== */

function initializeNavbar() {

    const navbar = document.getElementById("navbar");

    if (!navbar) return;

    window.addEventListener("scroll", () => {

        if (window.scrollY > 40) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    });

}

/* ==========================================
   SMOOTH SCROLL
========================================== */

function initializeSmoothScroll() {

    document
        .querySelectorAll('a[href^="#"]')
        .forEach(anchor => {

            anchor.addEventListener("click", function (event) {

                const targetId = this.getAttribute("href");

                if (targetId === "#") return;

                const target = document.querySelector(targetId);

                if (!target) return;

                event.preventDefault();

                target.scrollIntoView({

                    behavior: "smooth",

                    block: "start"

                });

            });

        });

}

/* ==========================================
   REVEAL
========================================== */

function initializeRevealAnimations() {

    const elements = document.querySelectorAll(

        ".card, .section-header, .hero-left, .hero-right"

    );

    const observer = new IntersectionObserver(

        (entries) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("visible");

                }

            });

        },

        {

            threshold: .15

        }

    );

    elements.forEach(element => {

        element.classList.add("reveal");

        observer.observe(element);

    });

}

/* ==========================================
   MOBILE MENU
========================================== */

const menuButton = document.getElementById("menuToggle");

const navigation = document.getElementById("navMenu");

if (menuButton && navigation) {

    menuButton.addEventListener("click", () => {

        navigation.classList.toggle("mobile-open");

        menuButton.classList.toggle("active");

    });

}

/* ==========================================
   ACTIVE NAVIGATION
========================================== */

const sections = document.querySelectorAll("section");

const navLinks = document.querySelectorAll(".nav-menu a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 120;

        if (scrollY >= sectionTop) {

            current = section.getAttribute("id");

        }

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        const href = link.getAttribute("href");

        if (href === `#${current}`) {

            link.classList.add("active");

        }

    });

});