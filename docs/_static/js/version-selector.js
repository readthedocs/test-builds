function renderVersions(config) {
  if (!config.versions.active.length) {
    return "";
  }
  const versionsHTML = `
      ${ config.versions.active.map(
        (version) => `
        <a class="dropdown-item list-group-item list-group-item-action py-1 ${ version.slug === config.versions.current.slug ? 'active' : '' }"
           href="${ version.verbose_name }"
           role="option"
           data-version-name="${ version.verbose_name }"
           data-version="${ version.slug }">
           <span>${ version.verbose_name }</span>
        </a>
    `).join("\n")}
    `;
  return versionsHTML;
}

document.addEventListener("readthedocs-addons-data-ready", function(event) {
    const config = event.detail.data();
    const versionSelector = `
    <div class="navbar-item">
      <div class="version-switcher__container dropdown">
        <button id="pst-version-switcher-button-2"
                type="button"
                class="version-switcher__button btn btn-sm dropdown-toggle"
                data-bs-toggle="dropdown"
                aria-haspopup="listbox"
                aria-controls="pst-version-switcher-list-2"
                aria-label="Version switcher list"
                data-active-version-name="${ config.current.verbose_name }"
                data-active-version="${ config.current.slug }" aria-expanded="true">
          0.15.4 (stable)
        </button>

        <div id="pst-version-switcher-list-2"
             class="version-switcher__menu dropdown-menu list-group-flush py-0 show"
             role="listbox"
             aria-labelledby="pst-version-switcher-button-2"
             data-bs-popper="static">
          ${ renderVersions(config) }
        </div>
      </div>
    </div>
    `;


  const header = document.querySelector("header");
  header.insertAdjacentHTML("afterbegin", versionSelector);
});
