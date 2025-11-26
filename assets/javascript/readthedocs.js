document.addEventListener("DOMContentLoaded", function(event) {
    // Trigger Read the Docs' search addon instead of Zensical default
    document.querySelector(".md-search__button").addEventListener("click", (e) => {
        const event = new CustomEvent("readthedocs-search-show");
        document.dispatchEvent(event);
    });
});
