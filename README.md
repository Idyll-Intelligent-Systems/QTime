# 🌌 QTime - Quantum Timeline Engine

**Advanced time travel visualization toolkit with multi-dimensional reality simulation**

Transform complex temporal relationships into stunning interactive visualizations. QTime combines quantum mechanics principles with cutting-edge visualization technology to create immersive timeline experiences.

## ✨ Features

� **Multiple Visualization Modes**
- **Basic 2D Animations** - Classic timeline branching GIFs
- **Advanced Quantum Visualizations** - Multi-layered timeline with particle effects  
- **Interactive 3D Environments** - WebGL-powered immersive exploration
- **HTML Quantum Sandbox** - Real-time interactive timeline manipulation

🌐 **Multi-Platform Support**
- **Python Engine** - Core timeline generation and quantum simulation
- **Web Interface** - Browser-based interactive sandboxes
- **REST API** - Timeline management and collaboration
- **WebSocket Server** - Real-time multi-user synchronization  
- **CLI Tools** - Command-line interface for automation

🔬 **Quantum Mechanics Simulation**
- **Superposition States** - Multiple timeline branches existing simultaneously
- **Wave Function Collapse** - Observation-based reality selection
- **Quantum Entanglement** - Interconnected timeline relationships
- **Paradox Detection** - Automatic causality violation alerts

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd QTime

# Install dependencies  
python setup.py

# Generate your first timeline
python qtime_cli.py generate basic
```

### Web Interface
```bash
# Start the API server
python qtime_cli.py server api

# Open browser to http://localhost:5000
# Access interactive documentation and timeline management
```

## 📊 Visualization Examples

### 🎞️ Basic Animated Timeline (Python)

Generate branching timeline GIFs with quantum effects:

```python
# Basic Timeline Generation
from enhanced_timeline_generator import QTimeEngine

engine = QTimeEngine()
engine.generate_advanced_animation("my_timeline.gif")
```

### 🌐 Interactive 3D Timeline (WebGL)

Create immersive 3D timeline explorations:

```python
from qtime_3d_generator import create_sample_3d_timeline

timeline = create_sample_3d_timeline()
timeline.generate_3d_html("interactive_3d.html")
# Opens full 3D environment with mouse controls, particle effects
```

### 🧪 Advanced HTML Sandbox

Real-time quantum timeline manipulation:

- **Quantum Operations**: Collapse wave functions, maintain superposition
- **Temporal Controls**: Rewind, fast-forward, create time loops  
- **Paradox Generation**: Grandfather, bootstrap, twin, predestination paradoxes
- **Multi-User Collaboration**: Real-time synchronized timeline editing

### 🎛️ CLI Interface

Complete command-line control:

```bash
# Generate different timeline types
qtime generate basic --output my_timeline.gif
qtime generate advanced --output quantum_timeline.gif  
qtime generate 3d --output timeline_3d.html
qtime generate html --output sandbox.html

# Start servers
qtime server api --port 5000
qtime server websocket --port 8765

# Configuration management
qtime config show
qtime config set auto_open_browser true
```

## 🏗️ Architecture

### Core Components

**QTimeEngine** - Python quantum timeline simulation engine
- Multi-dimensional node positioning
- Quantum state management  
- Probability-based event resolution
- Paradox detection and handling

**Interactive Visualizations**
- WebGL 3D rendering with Three.js
- Real-time particle systems
- Dynamic camera controls
- Quantum effect animations

**Collaboration Infrastructure**  
- REST API for timeline CRUD operations
- WebSocket server for real-time synchronization
- SQLite database for persistence
- Multi-user session management

### File Structure
```
QTime/
├── enhanced_timeline_generator.py  # Advanced Python timeline engine
├── qtime_3d_generator.py          # 3D WebGL timeline generator  
├── quantum_sandbox_advanced.html  # Interactive HTML sandbox
├── qtime_api.py                   # REST API server
├── qtime_server.py               # WebSocket server
├── qtime_cli.py                  # Command-line interface
├── setup.py                      # Installation script
├── requirements.txt              # Python dependencies  
└── README.md                     # This file
```

## 🔬 Advanced Features

### Quantum Mechanics Simulation

**Superposition States**
```python
# Maintain multiple timeline branches simultaneously
timeline.add_quantum_event("Meeting", "superposition", probability=0.8)
```

**Wave Function Collapse**  
```javascript
// JavaScript quantum observation
quantumEngine.observe("Meeting"); // Collapses to single reality
```

**Entanglement Effects**
```python
# Create quantum entangled timeline branches
engine.entangle_timelines(["Branch_A", "Branch_B"])
```

### Multi-User Collaboration

**Real-time Synchronization**
- WebSocket-based timeline sharing
- Collaborative quantum observations
- Synchronized paradox resolution
- Multi-observer quantum effects

**API Integration**
```bash
# Create collaborative timeline
curl -X POST http://localhost:5000/api/timelines \
  -H "Content-Type: application/json" \
  -d '{"name": "Shared Timeline", "nodes": {...}}'
```

### Paradox Detection System

Automatic detection and handling of temporal paradoxes:

- **Grandfather Paradox**: Preventing your own existence
- **Bootstrap Paradox**: Information without origin
- **Twin Paradox**: Relativistic time dilation  
- **Predestination Paradox**: Effects preceding causes

## 🎨 Customization

### Themes and Styling
```python
# Custom visualization themes
config = {
    "theme": {
        "background": "#0b0b0e",
        "quantum_color": "#F44336", 
        "temporal_color": "#2196F3",
        "paradox_color": "#FF9800"
    }
}
```

### Node Types and Properties
```python
# Advanced node configuration  
engine.add_node("Quantum_Gate", [2, 3, 1], "quantum", {
    "probability": 0.7,
    "entangled": True,
    "paradox_potential": "high"
})
```

## 📖 API Reference

### REST Endpoints

- `GET /api/timelines` - List all timelines
- `POST /api/timelines` - Create new timeline
- `GET /api/timelines/{id}` - Get specific timeline  
- `PUT /api/timelines/{id}` - Update timeline
- `DELETE /api/timelines/{id}` - Delete timeline
- `POST /api/timelines/{id}/quantum-events` - Add quantum event
- `POST /api/timelines/{id}/observe` - Collapse quantum states

### WebSocket Events

- `create_timeline` - Create collaborative timeline
- `join_timeline` - Join existing timeline
- `quantum_event` - Broadcast quantum events
- `observation` - Sync quantum observations  
- `paradox_detected` - Alert all participants

## 🤝 Contributing

QTime is designed for extensibility:

1. **Timeline Generators** - Add new visualization types
2. **Quantum Effects** - Implement additional quantum mechanics
3. **Paradox Types** - Define new temporal paradox categories
4. **Visualization Themes** - Create custom visual styles
5. **Collaboration Features** - Enhance multi-user capabilities

## 📜 License

See [LICENSE](LICENSE) file for details.

---

## 🎯 Original Simple Examples

### 🎞️ Basic Animated GIF (Python)

```python
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

# Create animation
fig, ax = plt.subplots(figsize=(6, 4))
# ... animation code ...
anim.save("timeline_branches.gif", writer=PillowWriter(fps=30))
```

### 🧪 Simple HTML Sandbox

```html

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
function superpos(){Object.values(edgeMap).forEach(e=>{e.classList.remove("hidden");e.<!DOCTYPE html>
<html>
<head><title>Quantum Timeline Sandbox</title></head>
<body>
  <!-- Interactive SVG timeline with quantum controls -->
  <button onclick="collapse()">🔭 Observe</button>
  <button onclick="superposition()">🌀 Superposition</button>
  <svg viewBox="-350 -220 700 440"><!-- Timeline visualization --></svg>
</body>
</html>
```

---

## 🎉 Ready to Explore?

**Get started with QTime:**

1. **Clone the repository**
2. **Run `python setup.py`** to install
3. **Execute `python qtime_cli.py info`** for next steps
4. **Generate your first quantum timeline!**

**Advanced users:**
- Explore the API documentation at `http://localhost:5000`
- Join collaborative timelines via WebSocket  
- Create custom quantum effects and paradox types
- Build your own temporal visualization plugins

Transform your understanding of time and causality with QTime's quantum timeline engine. Whether you're visualizing complex temporal relationships, exploring quantum mechanics concepts, or building collaborative timeline experiences, QTime provides the tools to make time travel tangible.

🌌 **Happy time traveling!**


