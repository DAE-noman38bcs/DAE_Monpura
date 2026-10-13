/*
  Developer: Mahmud Abdullah Al Naman (মাহমুদ আব্দুল্লাহ আল নোমান)
  Email: noman38bcs@gmail.com
  Phone: 01623015273
  File: monpuragrok.widget.js
*/
async function pingMonpuraGrok() {
  document.getElementById("status").textContent = "online";
  document.getElementById("log").textContent = "[MonpuraGrok] engine ready @ " + new Date().toISOString();
}
window.addEventListener("DOMContentLoaded", pingMonpuraGrok);
