// using the js instead to collect data
let videos = document.querySelectorAll(".style-scope ytd-video-renderer");
videos.forEach(function (video){
    let videoTitle = video.querySelector('yt-formatted-string').innerText;
    videoTitle.replace(",","|");
    console.log(`"${videoTitle}",`);
})