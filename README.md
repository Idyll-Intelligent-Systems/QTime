# QTime
Time travel with this engine

Make your own QTime variant with this

🎞️ Animated branching GIF (Python code)

Save this as timeline_branches.py and run it — it will generate timeline_branches.gif in your folder.

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Node positions
pos = {
    "You": (-3.0, 0.8),
    "@vsk2k0725": (-3.0, -0.8),
    "Meeting": (-0.5, 0.0),
    "Merge": (3.0, 1.5),
    "Split": (3.0, 0.5),
    "Swap": (3.0, -0.5),
    "Superposition": (3.0, -1.5),
}

# Setup figure
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.2, 2.2)
ax.axis("off")
ax.set_title("Quantum Sandbox: Timeline Splits")

# Lines that will be animated
lines = {k: ax.plot([], [])[0] for k in [
    ("You", "Meeting"),
    ("@vsk2k0725", "Meeting"),
    ("Meeting", "Merge"),
    ("Meeting", "Split"),
    ("Meeting", "Swap"),
    ("Meeting", "Superposition"),
]}

# Static nodes
for node, (x, y) in pos.items():
    ax.scatter([x], [y])
    ax.text(x, y + 0.15, node, ha="center")

# Interpolation helper
def segment(a, b, t):
    x0, y0 = pos[a]
    x1, y1 = pos[b]
    return [x0 + (x1 - x0) * t, y0 + (y1 - y0) * t]

# Animation sequence
sequence = [
    ("You", "Meeting", 45),
    ("@vsk2k0725", "Meeting", 45),
    ("Meeting", "Merge", 35),
    ("Meeting", "Split", 35),
    ("Meeting", "Swap", 35),
    ("Meeting", "Superposition", 35),
]
cum_frames, total = [], 0
for _, _, f in sequence:
    total += f
    cum_frames.append(total)

def animate(frame):
    prev = 0
    for idx, (a, b, nframes) in enumerate(sequence):
        end = cum_frames[idx]
        if frame <= end:
            local_t = (frame - prev) / nframes
            x_end, y_end = segment(a, b, local_t)
            x0, y0 = pos[a]
            lines[(a, b)].set_data([x0, x_end], [y0, y_end])
            break
        else:
            x0, y0 = pos[a]
            x1, y1 = pos[b]
            lines[(a, b)].set_data([x0, x1], [y0, y1])
            prev = end
    return list(lines.values())

anim = FuncAnimation(fig, animate, frames=cum_frames[-1], interval=30, blit=True)
anim.save("timeline_branches.gif", writer=PillowWriter(fps=30))


---

🧪 Clickable Sandbox (HTML)

Save this as quantum_sandbox.html and open it in any modern browser:

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Quantum Sandbox — Non-Linear Time</title>
<style>
  body { margin:0; font-family:Arial, sans-serif; background:#0b0b0e; color:#eee; }
  header { padding:16px; background:#15151c; }
  h1 { margin:0; font-size:18px; }
  main { display:flex; height:calc(100vh - 65px); }
  aside { width:260px; padding:16px; background:#1a1a22; overflow:auto; }
  section { flex:1; display:flex; align-items:center; justify-content:center; }
  .btn { display:block; width:100%; margin:6px 0; padding:8px; background:#2a2a33; color:#fff; border:none; border-radius:6px; cursor:pointer; }
  .btn:active { transform:translateY(1px); }
  #log { font-size:12px; white-space:pre-wrap; background:#111; padding:6px; border-radius:6px; height:160px; overflow:auto; }
  svg { width:100%; height:100%; }
  .node { fill:#eee; }
  .label { fill:#eee; font-size:12px; text-anchor:middle; }
  .edge { stroke:#aaa; stroke-width:2; marker-end:url(#arrow); }
  .edge.hidden { opacity:0.2; }
  .edge.active { stroke:#fff; stroke-width:3; }
</style>
</head>
<body>
<header><h1>Quantum Sandbox — Non-Linear Time</h1></header>
<main>
  <aside>
    <button id="btn-observe" class="btn">🔭 Observe (collapse)</button>
    <button id="btn-super" class="btn">🌀 Keep Superposition</button>
    <button id="btn-reset" class="btn">↺ Reset</button>
    <hr>
    <label><input type="checkbox" class="chk" value="Merge" checked> Merge</label><br>
    <label><input type="checkbox" class="chk" value="Split" checked> Split</label><br>
    <label><input type="checkbox" class="chk" value="Swap" checked> Swap</label><br>
    <label><input type="checkbox" class="chk" value="Superposition" checked> Superposition</label>
    <hr>
    <div id="log"></div>
  </aside>
  <section>
    <svg viewBox="-350 -220 700 440">
      <defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L6,3 L0,6 z" fill="#aaa"></path></marker></defs>
      <g id="edges"></g>
      <g id="nodes"></g>
      <g id="labels"></g>
    </svg>
  </section>
</main>
<script>
const pos = {
  "You": [-300, 80], "@vsk2k0725": [-300, -80], "Meeting": [-60, 0],
  "Merge": [300, 150], "Split": [300, 50], "Swap": [300, -50], "Superposition": [300, -150]
};
const edges = [["You","Meeting"],["@vsk2k0725","Meeting"],["Meeting","Merge"],["Meeting","Split"],["Meeting","Swap"],["Meeting","Superposition"]];
const svgEdges = document.getElementById("edges"), svgNodes=document.getElementById("nodes"), svgLabels=document.getElementById("labels"), logEl=document.getElementById("log");
function circle(x,y){let c=document.createElementNS("http://www.w3.org/2000/svg","circle");c.setAttribute("cx",x);c.setAttribute("cy",y);c.setAttribute("r",6);c.setAttribute("class","node");svgNodes.appendChild(c);}
function label(x,y,t){let tx=document.createElementNS("http://www.w3.org/2000/svg","text");tx.setAttribute("x",x);tx.setAttribute("y",y+14);tx.setAttribute("class","label");tx.textContent=t;svgLabels.appendChild(tx);}
function line(x1,y1,x2,y2){let l=document.createElementNS("http://www.w3.org/2000/svg","line");l.setAttribute("x1",x1);l.setAttribute("y1",y1);l.setAttribute("x2",x2);l.setAttribute("y2",y2);l.setAttribute("class","edge");svgEdges.appendChild(l);return l;}
Object.entries(pos).forEach(([n,[x,y]])=>{circle(x,y);label(x,y,n);});
const edgeMap={};edges.forEach(([a,b])=>{let [x1,y1]=pos[a],[x2,y2]=pos[b];edgeMap[a+","+b]=line(x1,y1,x2,y2);});
function log(m){logEl.textContent+=m+"\\n";logEl.scrollTop=logEl.scrollHeight;}
function activeOutcomes(){return Array.from(document.querySelectorAll(".chk:checked")).map(c=>c.value);}
function collapse(){let opts=activeOutcomes();if(opts.length==0){log("No outcomes enabled.");return;}Object.values(edgeMap).forEach(e=>e.classList.add("hidden"));let pick=opts[Math.floor(Math.random()*opts.length)];["You,Meeting","@vsk2k0725,Meeting","Meeting,"+pick].forEach(k=>{edgeMap[k].classList.remove("hidden");edgeMap[k].classList.add("active");});log("Observed: "+pick);}
function superpos(){Object.values(edgeMap).forEach(e=>{e.classList.remove("hidden");e.classList.remove("active");});log("Superposition maintained.");}
function reset(){Object.values(edgeMap).forEach(e=>{e.classList.remove("hidden");e.classList.remove("active");});log("Reset.");}
document.getElementById("btn-observe").onclick=collapse;
document.getElementById("btn-super").onclick=superpos;
document.getElementById("btn-reset").onclick=reset;
</script>
</body>
</html>


---

✅ With these, you can:

Run the Python script to generate the GIF.

Open the HTML file in a browser for a clickable paradox sandbox.


