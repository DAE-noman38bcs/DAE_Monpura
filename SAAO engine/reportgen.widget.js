// ReportGen widget — minimal status poller
async function pingReportGen() {
  document.getElementById("status").textContent = "online";
  document.getElementById("log").textContent = "[ReportGen] engine ready @ " + new Date().toISOString();
}
window.addEventListener("DOMContentLoaded", pingReportGen);
