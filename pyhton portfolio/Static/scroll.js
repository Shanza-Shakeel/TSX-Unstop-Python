window.addEventListener("scroll", revealOnScroll);

function revealOnScroll() {
    const reveals = document.querySelectorAll(".reveal");
    for (const el of reveals) {
        const windowHeight = window.innerHeight;
        const elementTop = el.getBoundingClientRect().top;
        const revealPoint = 100;

        if (elementTop < windowHeight - revealPoint) {
            el.classList.add("active");
        }
    }
}
