import os
html = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Slider Validation</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#1a1a2e; font-family:Arial,sans-serif; display:flex; justify-content:center; align-items:center; min-height:100vh; flex-direction:column; }
h1 { color:#fff; margin-bottom:20px; }
.slider-container { position:relative; width:600px; max-width:90vw; overflow:hidden; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.5); cursor:ew-resize; user-select:none; }
.slider-container img { display:block; width:100%%; height:auto; }
.img-after { position:absolute; top:0; left:0; width:100%%; height:100%%; overflow:hidden; }
.img-after img { position:absolute; top:0; left:0; width:100%%; height:100%%; object-fit:cover; }
.slider-line { position:absolute; top:0; left:50%%; width:3px; height:100%%; background:#fff; transform:translateX(-50%%); pointer-events:none; }
.slider-handle { position:absolute; top:50%%; left:50%%; width:40px; height:40px; background:#fff; border-radius:50%%; transform:translate(-50%%,-50%%); display:flex; align-items:center; justify-content:center; font-weight:bold; color:#1a1a2e; box-shadow:0 2px 10px rgba(0,0,0,0.3); pointer-events:none; }
.status { color:#fff; margin-top:20px; font-size:18px; padding:10px 20px; border-radius:8px; transition:all 0.3s; }
.status.validated { background:#4CAF50; font-weight:bold; }
</style>
</head>
<body>
<h1>Glissez pour valider</h1>
<div class="slider-container" id="slider">
<img src="WhatsApp Image 2026-05-19 at 13.30.24 (1).jpeg" alt="Photo 1">
<div class="img-after" id="imgAfter">
<img src="WhatsApp Image 2026-05-19 at 13.30.24.jpeg" alt="Photo 2">
</div>
<div class="slider-line" id="sliderLine"></div>
<div class="slider-handle" id="sliderHandle">&#8596;</div>
</div>
<div class="status" id="status">Glissez vers la droite pour valider</div>
<script>
var slider=document.getElementById("slider");
var imgAfter=document.getElementById("imgAfter");
var sliderLine=document.getElementById("sliderLine");
var sliderHandle=document.getElementById("sliderHandle");
var status=document.getElementById("status");
var isDown=false;
function updateSlider(x){
var rect=slider.getBoundingClientRect();
var pos=(x-rect.left)/rect.width;
pos=Math.max(0,Math.min(1,pos));
var percent=pos*100;
imgAfter.style.clipPath="inset(0 0 0 "+percent+"%)";
sliderLine.style.left=percent+"%";
sliderHandle.style.left=percent+"%";
if(percent>=90){status.textContent="Valide !";status.classList.add("validated");}
else{status.textContent="Glissez vers la droite pour valider";status.classList.remove("validated");}
}
imgAfter.style.clipPath="inset(0 0 0 0%)";
sliderLine.style.left="0%";
sliderHandle.style.left="0%";
slider.addEventListener("mousedown",function(e){isDown=true;updateSlider(e.clientX);});
document.addEventListener("mousemove",function(e){if(!isDown)return;updateSlider(e.clientX);});
document.addEventListener("mouseup",function(){isDown=false;});
slider.addEventListener("touchstart",function(e){isDown=true;updateSlider(e.touches[0].clientX);});
document.addEventListener("touchmove",function(e){if(!isDown)return;updateSlider(e.touches[0].clientX);});
document.addEventListener("touchend",function(){isDown=false;});
</script>
</body>
</html>'''
with open('slider.html','w',encoding='utf-8') as f:
    f.write(html)
print('OK')
