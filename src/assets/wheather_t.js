var progress = 50;

// function setProgress() {
//   document.getElementById("wtps").style.background =
//     "conic-gradient( #072400 " +
//     progress +
//     "%, #98ff79 " +
//     progress +
//     "%)";

//   document.getElementById("wtmc").innerHTML =
//     progress.toString() + "%";
// }

// window.onload = function () {
//   setProgress();
// };

document.getElementById("wtps").style.background =
"conic-gradient( #072400 " +
progress +
"%, #98ff79 " +
progress +
"%)";

document.getElementById("wtmc").innerHTML =
progress.toString() + "°C";