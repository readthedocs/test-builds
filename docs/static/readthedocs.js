// Show a message in the console immediatelly loading this script
console.log("This message comes from a file injected by Cloudflare Worker");

function _handleReadTheDocsData (event) {
  const config = event.data();
  console.log("Project slug:", config.projects.current.slug);
}

// Subscribe to the Read the Docs Addons event to access data if it hasn't been fired yet.
document.addEventListener("readthedocs-addons-data-ready", function (event) {
  _handleReadTheDocsData(event.detail);
});
