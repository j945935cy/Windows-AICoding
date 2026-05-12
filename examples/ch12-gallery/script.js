const filterButtons = document.querySelectorAll(".filter-button");
const galleryCards = document.querySelectorAll(".gallery-card");
const modal = document.querySelector("#modal");
const closeModal = document.querySelector("#closeModal");
const modalCategory = document.querySelector("#modalCategory");
const modalTitle = document.querySelector("#modalTitle");
const modalDescription = document.querySelector("#modalDescription");

function setFilter(filter) {
  galleryCards.forEach((card) => {
    const shouldShow = filter === "all" || card.dataset.category === filter;
    card.classList.toggle("hidden", !shouldShow);
  });
}

function openModal(card) {
  modalCategory.textContent = card.dataset.category;
  modalTitle.textContent = card.dataset.title;
  modalDescription.textContent = card.dataset.description;
  modal.classList.add("open");
  modal.setAttribute("aria-hidden", "false");
  closeModal.focus();
}

function hideModal() {
  modal.classList.remove("open");
  modal.setAttribute("aria-hidden", "true");
}

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    filterButtons.forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    setFilter(button.dataset.filter);
  });
});

galleryCards.forEach((card) => {
  card.addEventListener("click", () => {
    openModal(card);
  });
});

closeModal.addEventListener("click", hideModal);

modal.addEventListener("click", (event) => {
  if (event.target === modal) {
    hideModal();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && modal.classList.contains("open")) {
    hideModal();
  }
});
