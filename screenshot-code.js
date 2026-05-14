// use this on browser's console of https://learn.cylabacademy.org/library page
// TODO: find the thing we need to screenshot hehe
let s = document.createElement('script');
s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html-to-image/1.11.11/html-to-image.min.js';
document.head.appendChild(s);
s.onload = () => htmlToImage.toPng(document.querySelector('.CHANGEME'), { backgroundColor: '#ffffff' }).then(d => {
    let a = document.createElement('a');
    a.download = 'screenshot.png';
    a.href = d;
    a.click();
});