var progress = 11;

if (progress <= 2) {
    document.getElementById("uvmc").style.color = "#2bff00";
}
if (progress > 2 && progress <= 5) {
    document.getElementById("uvmc").style.color = "#fffb00";
}
if (progress > 5 && progress <= 7) {
    document.getElementById("uvmc").style.color = "#ff6600";
}
if (progress > 7 && progress <= 10) {
    document.getElementById("uvmc").style.color = "#ff0000";
}
if (progress > 10) {
    document.getElementById("uvmc").style.color = "#79005e";
}

document.getElementById("uvmc").innerHTML =
progress.toString() + "";
