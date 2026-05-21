html = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Slider Validation</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;background:#f5f5f5;min-height:100vh;display:flex;align-items:center;justify-content:center}
.app-header{position:fixed;top:0;left:0;right:0;height:56px;background:#fff;display:flex;align-items:center;padding:0 16px;border-bottom:1px solid #eee;z-index:99}
.app-header h1{font-size:18px;font-weight:700;color:#1a1a1a}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center;z-index:200;padding:20px}
.modal{background:#fff;border-radius:16px;width:100%;max-width:380px;padding:24px;position:relative;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
.close-btn{position:absolute;top:16px;right:16px;width:28px;height:28px;border:none;background:#f0f0f0;border-radius:50%;cursor:pointer;font-size:16px;color:#666}
.title{font-size:18px;font-weight:700;text-align:center;margin-bottom:20px}
.badge{width:40px;height:40px;background:#00897B;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 12px}
.badge span{color:#fff;font-size:13px;font-weight:700}
.pname{font-size:15px;font-weight:700;text-align:center;margin-bottom:4px}
.loc{font-size:13px;color:#666;text-align:center;margin-bottom:16px}
.code{background:#00897B;color:#fff;font-size:13px;font-weight:700;padding:8px 16px;border-radius:20px;width:fit-content;margin:0 auto 16px;letter-spacing:.5px}
.info{font-size:12px;color:#666;text-align:center;line-height:1.5;margin-bottom:20px}
.track{position:relative;width:100%;height:56px;background:#e8f5f3;border-radius:28px;border:2px solid #00897B;overflow:hidden}
.fill{position:absolute;left:0;top:0;height:100%;background:rgba(0,137,123,0.15);border-radius:28px;pointer-events:none}
.label{position:absolute;width:100%;height:100%;display:flex;align-items:center;justify-content:center;color:#00897B;font-size:14px;font-weight:600;pointer-events:none;user-select:none}
.thumb{position:absolute;left:4px;top:4px;width:48px;height:48px;background:#00897B;border-radius:50%;cursor:grab;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,137,123,0.4);z-index:10}
.thumb:active{cursor:grabbing}
.thumb svg{width:20px;height:20px;fill:#fff}
@keyframes hint{0%,100%{left:4px}50%{left:20px}}
.thumb.hint{animation:hint 1.5s ease-in-out infinite}
.valid-view{display:none;text-align:center;padding:20px 0}
.valid-view.show{display:block}
.check{width:64px;height:64px;background:#00897B;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px}
.check svg{width:32px;height:32px;fill:#fff}
.vtxt{font-size:18px;font-weight:700;color:#00897B;margin-bottom:8px}
.vsub{font-size:13px;color:#666;line-height:1.5}
.init{transition:opacity .4s}
.init.hide{opacity:0;pointer-events:none;height:0;overflow:hidden}
</style>
</head>
<body>
<div class="app-header"><h1>Manu Driver Nlg</h1></div>
<div class="overlay"><div class="modal">
<button class="close-btn" onclick="reset()">&#x2715;</button>
<div class="title">Commande &#224; r&#233;cup&#233;rer</div>
<div class="init" id="init">
<div class="badge"><span>1x</span></div>
<div class="pname">Panier Mixte Produits Frais (20&#8364;)</div>
<div class="loc">Super U - Noisy le Grand - Les Richardets</div>
<div class="code">SBSFEX6H9S9W0</div>
<div class="info">Validez ci dessous et montrez l&#39;&#233;cran au commer&#231;ant. Assurez-vous de ne confirmer qu&#39;une fois que vous &#234;tes chez le commer&#231;ant pour r&#233;cup&#233;rer votre panier.</div>
<div class="track" id="track">
<div class="fill" id="fill"></div>
<div class="label" id="lbl">Valider pour r&#233;cup&#233;rer</div>
<div class="thumb hint" id="thumb"><svg viewBox="0 0 24 24"><path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6z"/></svg></div>
</div></div>
<div class="valid-view" id="vview">
<div class="badge"><span>1x</span></div>
<div class="pname">Panier Mixte Produits Frais (20&#8364;)</div>
<div class="loc">Super U - Noisy le Grand - Les Richardets</div>
<div class="code">SBSFEX6H9S9W0</div>
<div class="check"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></div>
<div class="vtxt">Collecte confirm&#233;e</div>
<div class="vsub">Montrez l&#39;&#233;cran au commer&#231;ant pour r&#233;cup&#233;rer votre panier !</div>
</div></div></div>
<script>
var t=document.getElementById("thumb"),tr=document.getElementById("track"),f=document.getElementById("fill"),l=document.getElementById("lbl"),iv=document.getElementById("init"),vv=document.getElementById("vview");
var drag=false,sx=0,cx=0;
function mx(){return tr.offsetWidth-t.offsetWidth-8}
function start(e){drag=true;t.classList.remove("hint");sx=(e.touches?e.touches[0].clientX:e.clientX)-cx;t.style.transition="none";f.style.transition="none"}
function move(e){if(!drag)return;e.preventDefault();var x=(e.touches?e.touches[0].clientX:e.clientX)-sx;var m=mx();cx=Math.max(0,Math.min(x,m));t.style.left=(cx+4)+"px";f.style.width=(cx/m*100)+"%";l.style.opacity=1-cx/m}
function end(){if(!drag)return;drag=false;var m=mx();t.style.transition="left .4s";f.style.transition="width .4s";if(cx>m*0.75){t.style.left=(m+4)+"px";f.style.width="100%";l.style.opacity="0";setTimeout(function(){iv.classList.add("hide");vv.classList.add("show")},400)}else{cx=0;t.style.left="4px";f.style.width="0%";l.style.opacity="1";setTimeout(function(){t.classList.add("hint")},600)}}
function reset(){cx=0;t.style.transition="left .4s";f.style.transition="width .4s";t.style.left="4px";f.style.width="0%";l.style.opacity="1";iv.classList.remove("hide");vv.classList.remove("show");setTimeout(function(){t.classList.add("hint")},400)}
t.addEventListener("mousedown",start);t.addEventListener("touchstart",start,{passive:true});
document.addEventListener("mousemove",move);document.addEventListener("touchmove",move,{passive:false});
document.addEventListener("mouseup",end);document.addEventListener("touchend",end);
</script>
</body>
</html>'''
with open('slider_validated.html','w',encoding='utf-8') as f:
    f.write(html)
print('OK')