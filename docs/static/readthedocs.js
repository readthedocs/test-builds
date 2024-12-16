function _handleReadTheDocsData (eventData) {
  const config = eventData.data();

  if (config.versions.current.hidden) {
    console.log("This version is HIDDED");
  } else {
    console.log("This version IS NOT HIDDEN");
  }
}

console.log("This message comes from a file injected by Cloudflare Worker");

if (window.ReadTheDocsEventData) {
  // Access Read the Docs Addons data if it's already available when this script is loaded.
  _handleReadTheDocsData(window.ReadTheDocsEventData);
} else {
  // Subscribe to the Read the Docs Addons event to access data if it hasn't been fired yet.
  document.addEventListener("readthedocs-addons-data-ready", function (event) {
    _handleReadTheDocsData(event.detail);
  });

}
