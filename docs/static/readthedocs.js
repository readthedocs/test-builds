// Show a message in the console immediatelly loading this script
console.log("This message comes from a file injected by CustomScript addon.");

function _handleReadTheDocsData (config) {
  console.log("_handleReadTheDocsData function called.");
  console.log("Project slug:", config.projects.current.slug);
}

// The event "readthedocs-addons-data-ready" has been already fired when this script is run.
// We need to check for `window.ReadTheDocsEventData` first, and if it's available
// use that data to call the handler.
if (window.ReadTheDocsEventData !== undefined) {
  _handleReadTheDocsData(window.ReadTheDocsEventData);
}

// After that, we subscribe to the Read the Docs Addons event to access data
// on future dispatchs (e.g. when a URL changes on a SPA)
document.addEventListener("readthedocs-addons-data-ready", function (event) {
  _handleReadTheDocsData(event.detail.data());
});
