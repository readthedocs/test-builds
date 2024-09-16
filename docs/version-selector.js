document.addEventListener("readthedocs-addons-data-ready", function(event) {
    const config = event.detail.data();
    const versionSelector = ```
    <div class="navbar-item">
      <div class="version-switcher__container dropdown">
        <button id="pst-version-switcher-button-2" type="button" class="version-switcher__button btn btn-sm dropdown-toggle show" data-bs-toggle="dropdown" aria-haspopup="listbox" aria-controls="pst-version-switcher-list-2" aria-label="Version switcher list" data-active-version-name="0.15.4 (stable)" data-active-version="v0.15.4" aria-expanded="true">0.15.4 (stable)</button>
        <div id="pst-version-switcher-list-2" class="version-switcher__menu dropdown-menu list-group-flush py-0 show" role="listbox" aria-labelledby="pst-version-switcher-button-2" data-bs-popper="static">
          <a class="dropdown-item list-group-item list-group-item-action py-1" href="https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/version-dropdown.html" role="option" data-version-name="dev" data-version="dev"><span>dev</span></a>
          <a class="dropdown-item list-group-item list-group-item-action py-1 active" href="https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html" role="option" data-version-name="0.15.4 (stable)" data-version="v0.15.4"><span>0.15.4 (stable)</span></a>
          <a class="dropdown-item list-group-item list-group-item-action py-1" href="https://pydata-sphinx-theme.readthedocs.io/en/v0.14.4/user_guide/version-dropdown.html" role="option" data-version-name="0.14.4" data-version="v0.14.4"><span>0.14.4</span></a>
          <a class="dropdown-item list-group-item list-group-item-action py-1" href="https://pydata-sphinx-theme.readthedocs.io/en/v0.13.3/user_guide/version-dropdown.html" role="option" data-version-name="0.13.3" data-version="v0.13.3"><span>0.13.3</span></a>
          <a class="dropdown-item list-group-item list-group-item-action py-1" href="https://pydata-sphinx-theme.readthedocs.io/en/v0.12.0/user_guide/version-dropdown.html" role="option" data-version-name="0.12.0" data-version="v0.12.0"><span>0.12.0</span></a>
          <a class="dropdown-item list-group-item list-group-item-action py-1" href="https://pydata-sphinx-theme.readthedocs.io/en/v0.11.0/user_guide/version-dropdown.html" role="option" data-version-name="0.11.0" data-version="v0.11.0"><span>0.11.0</span></a>
        </div>
      </div>
    </div>
    ```;


  const header = document.querySelector("header");
  header.insertAdjacentHTML("afterbegin", versionSelector);
});
