const menuButton = document.querySelector(".menu-button");
const siteNav = document.querySelector(".site-nav");
const projectCards = document.querySelectorAll(".project-card");
const projectDetail = document.querySelector("#projectDetail");

menuButton.addEventListener("click", () => {
  const isOpen = siteNav.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(isOpen));
});

siteNav.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    siteNav.classList.remove("open");
    menuButton.setAttribute("aria-expanded", "false");
  });
});

projectCards.forEach((card) => {
  card.addEventListener("click", () => {
    projectCards.forEach((item) => item.classList.remove("active"));
    card.classList.add("active");
    projectDetail.textContent = card.dataset.detail;
  });
});
