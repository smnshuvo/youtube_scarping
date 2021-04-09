// using the js instead to collect data
let videos = document.querySelectorAll(".style-scope ytd-video-renderer");
let finalData = ""
videos.forEach(function (video){
    let videoTitle = video.querySelector('yt-formatted-string').innerText;
    videoTitle = videoTitle.replace(",","|");
    finalData+= `"${videoTitle}",`;

})
console.log(finalData);