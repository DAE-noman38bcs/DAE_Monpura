// MonpuraPy widget — minimal status poller
async function pingMonpuraPy() {
  document.getElementById("status").textContent = "online";
  document.getElementById("log").textContent = "[MonpuraPy] engine ready @ " + new Date().toISOString();
}
window.addEventListener("DOMContentLoaded", pingMonpuraPy);
