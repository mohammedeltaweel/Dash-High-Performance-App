function newFunc() {
    const options = {
      root: null,
      // threshold: 0.9,
      rootMargin: "-150px"
    };
    const sections = document.querySelectorAll("section");
    const observer = new IntersectionObserver(function (entries, observer) {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          entry.target.classList.remove("abc");
          return;
        }
        entry.target.classList.add("abc");
        const liElements = document.querySelectorAll(".section.abc ul li");
        const filterDotElements = document.querySelectorAll(".section.abc .filter-dot");
        const filterTextElements = document.querySelectorAll(".section.abc .filter-text");
      // Get the labels
        liElements.forEach(function (liElement) {
            liElement.addEventListener("click", function () {
              const filterDot = liElement.querySelector(".section.abc .filter-dot");
              const filterText = liElement.querySelector(".section.abc .filter-text");
              const isActiveDot = filterDot.classList.contains("active");
              const isActiveText = filterText.classList.contains("active");
              const activeDotCount = Array.from(filterDotElements).filter((dot) =>
                dot.classList.contains("active")
              ).length;
              const activeTextCount = Array.from(filterTextElements).filter((text) =>
                text.classList.contains("active")
              ).length;
              if (isActiveDot && isActiveText) {
                if (activeDotCount > 1 || activeTextCount > 1) {
                  filterDot.classList.remove("active");
                  filterText.classList.remove("active");
                }
              } else {
                filterDot.classList.add("active");
                filterText.classList.add("active");
              }
            });
          });
  
  
      });
    }, options);
  
    sections.forEach((section) => {
      observer.observe(section);
    });
  }
  