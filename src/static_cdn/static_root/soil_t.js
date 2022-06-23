var progress = 25;

// function setProgress() {
//   document.getElementById("stps").style.background =
//     "conic-gradient( #072400 " +
//     progress +
//     "%, #98ff79 " +
//     progress +
//     "%)";

//   document.getElementById("stmc").innerHTML =
//     progress.toString() + "%";
// }

// window.onload = function () {
//   setProgress();
// };

document.getElementById("stps").style.background =
"conic-gradient( #072400 " +
progress +
"%, #98ff79 " +
progress +
"%)";

document.getElementById("stmc").innerHTML =
progress.toString() + "°C";