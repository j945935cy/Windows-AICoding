const navToggle = document.querySelector(".nav-toggle");
const siteNav = document.querySelector(".site-nav");

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const text = button.dataset.copy || "";

    try {
      await navigator.clipboard.writeText(text);
      button.textContent = "已複製";
      setTimeout(() => {
        button.textContent = "複製";
      }, 1600);
    } catch {
      button.textContent = "複製失敗";
      setTimeout(() => {
        button.textContent = "複製";
      }, 1600);
    }
  });
});

const backToTop = document.querySelector(".back-to-top");

if (backToTop) {
  window.addEventListener("scroll", () => {
    backToTop.classList.toggle("visible", window.scrollY > 520);
  });

  backToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

const filterButtons = document.querySelectorAll(".filter-button");
const chapterCards = document.querySelectorAll(".chapter-card");

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;

    filterButtons.forEach((item) => item.classList.remove("active"));
    button.classList.add("active");

    chapterCards.forEach((card) => {
      const shouldShow = filter === "all" || card.dataset.category === filter;
      card.classList.toggle("hidden", !shouldShow);
    });
  });
});

document.querySelectorAll(".faq-question").forEach((question) => {
  question.addEventListener("click", () => {
    const answer = question.nextElementSibling;
    if (answer) {
      answer.classList.toggle("open");
    }
  });
});

document.querySelectorAll("[data-progress]").forEach((checkbox) => {
  const key = `ai-coding-progress-${checkbox.dataset.progress}`;
  checkbox.checked = localStorage.getItem(key) === "done";

  checkbox.addEventListener("change", () => {
    if (checkbox.checked) {
      localStorage.setItem(key, "done");
    } else {
      localStorage.removeItem(key);
    }
  });
});
