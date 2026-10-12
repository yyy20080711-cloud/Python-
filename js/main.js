(function () {
  var buttons = document.querySelectorAll(".filter-btn");
  var cards = document.querySelectorAll("[data-category]");

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      buttons.forEach(function (item) {
        item.classList.remove("active");
      });
      btn.classList.add("active");
      var value = btn.getAttribute("data-filter");
      cards.forEach(function (card) {
        var match = value === "all" || card.getAttribute("data-category") === value;
        card.classList.toggle("hidden", !match);
      });
    });
  });
})();
