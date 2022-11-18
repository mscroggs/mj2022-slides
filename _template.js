var slides = {slides}
var cSlide = 0

document.addEventListener('keydown', function(event){
    const currentCode = event.which || event.code;
    var currentKey = event.key;
    if (!currentKey) {
        currentKey = String.fromCharCode(currentCode);
    }
    const keyName = "" + currentKey
    process_key(keyName)
});

function process_key(keyName){
    if((keyName == "ArrowRight" || keyName == "PageDown") && cSlide + 1 < slides.length){
        cSlide++
        document.body.innerHTML = slides[cSlide][0]
        document.body.className = slides[cSlide][1]["style"]
    }
    if((keyName == "ArrowLeft" || keyName == "PageUp") && cSlide > 0){
        cSlide--
        document.body.innerHTML = slides[cSlide][0]
        document.body.className = slides[cSlide][1]["style"]
    }
}
