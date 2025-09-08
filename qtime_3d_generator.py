#!/usr/bin/env python3
"""
QTime Interactive 3D Timeline Generator
Creates immersive 3D timeline visualizations with WebGL support
"""

import json
import math
import numpy as np
from datetime import datetime, timedelta

class QTime3D:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.quantum_events = []
        self.dimensions = 3
        
    def add_node(self, name, position, node_type="standard", properties=None):
        """Add a node to the 3D timeline"""
        self.nodes[name] = {
            'position': position,
            'type': node_type,
            'properties': properties or {},
            'id': len(self.nodes)
        }
        
    def add_edge(self, source, target, edge_type="temporal", properties=None):
        """Add an edge between nodes"""
        if source in self.nodes and target in self.nodes:
            self.edges.append({
                'source': source,
                'target': target,
                'type': edge_type,
                'properties': properties or {}
            })
            
    def add_quantum_event(self, node, event_type, probability=0.5):
        """Add quantum event to node"""
        self.quantum_events.append({
            'node': node,
            'type': event_type,
            'probability': probability,
            'timestamp': datetime.now().isoformat()
        })
        
    def generate_3d_html(self, output_file="qtime_3d.html"):
        """Generate interactive 3D HTML visualization"""
        
        html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>QTime 3D — Immersive Timeline Explorer</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
    font-family: 'Consolas', monospace; 
    background: #000; 
    color: #fff; 
    overflow: hidden;
}
#container { position: relative; width: 100vw; height: 100vh; }
#controls {
    position: absolute;
    top: 20px;
    left: 20px;
    z-index: 100;
    background: rgba(0,0,0,0.8);
    padding: 20px;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
}
#info {
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 100;
    background: rgba(0,0,0,0.8);
    padding: 15px;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    min-width: 250px;
}
.control-btn {
    display: block;
    width: 100%;
    margin: 5px 0;
    padding: 10px 15px;
    background: linear-gradient(45deg, #444, #666);
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s;
}
.control-btn:hover {
    background: linear-gradient(45deg, #555, #777);
    transform: translateY(-1px);
}
#stats { font-size: 12px; line-height: 1.6; }
#loading {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    z-index: 1000;
}
</style>
</head>
<body>
<div id="container">
    <div id="loading">
        <h2>Initializing Quantum Timeline...</h2>
        <p>Loading 3D Environment</p>
    </div>
    
    <div id="controls">
        <h3>QTime 3D Controls</h3>
        <button class="control-btn" onclick="resetView()">🏠 Reset View</button>
        <button class="control-btn" onclick="toggleAnimation()">▶️ Toggle Animation</button>
        <button class="control-btn" onclick="quantumCollapse()">🌀 Quantum Collapse</button>
        <button class="control-btn" onclick="showParadox()">⚠️ Generate Paradox</button>
        <button class="control-btn" onclick="toggleWireframe()">🔗 Wireframe Mode</button>
        <button class="control-btn" onclick="exportTimeline()">💾 Export Timeline</button>
    </div>
    
    <div id="info">
        <h3>Timeline Info</h3>
        <div id="stats">
            <p><strong>Nodes:</strong> <span id="nodeCount">0</span></p>
            <p><strong>Connections:</strong> <span id="edgeCount">0</span></p>
            <p><strong>Quantum Events:</strong> <span id="quantumCount">0</span></p>
            <p><strong>Camera Position:</strong> <span id="cameraPos">0,0,0</span></p>
            <p><strong>Selected Node:</strong> <span id="selectedNode">None</span></p>
        </div>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.9/dat.gui.min.js"></script>

<script>
class QTime3DVisualization {
    constructor() {
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.controls = null;
        
        this.nodes = new Map();
        this.edges = [];
        this.nodeObjects = new Map();
        this.edgeObjects = [];
        
        this.animating = true;
        this.wireframe = false;
        this.selectedNode = null;
        
        this.quantumParticles = [];
        
        this.init();
        this.loadTimelineData();
        this.animate();
    }
    
    init() {
        const container = document.getElementById('container');
        
        // Scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x000011);
        this.scene.fog = new THREE.Fog(0x000011, 10, 100);
        
        // Camera
        this.camera = new THREE.PerspectiveCamera(
            75, window.innerWidth / window.innerHeight, 0.1, 1000
        );
        this.camera.position.set(0, 0, 20);
        
        // Renderer
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        container.appendChild(this.renderer.domElement);
        
        // Lighting
        const ambientLight = new THREE.AmbientLight(0x404040, 0.4);
        this.scene.add(ambientLight);
        
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(10, 10, 10);
        directionalLight.castShadow = true;
        this.scene.add(directionalLight);
        
        // Point lights for quantum effects
        const quantumLight1 = new THREE.PointLight(0x00ff88, 1, 50);
        quantumLight1.position.set(-20, 10, 0);
        this.scene.add(quantumLight1);
        
        const quantumLight2 = new THREE.PointLight(0xff0088, 1, 50);
        quantumLight2.position.set(20, -10, 0);
        this.scene.add(quantumLight2);
        
        // Controls
        this.setupControls();
        
        // Event listeners
        window.addEventListener('resize', () => this.onWindowResize());
        this.renderer.domElement.addEventListener('click', (event) => this.onNodeClick(event));
        
        document.getElementById('loading').style.display = 'none';
    }
    
    setupControls() {
        // Mouse controls for camera
        let isMouseDown = false;
        let mouseX = 0, mouseY = 0;
        
        this.renderer.domElement.addEventListener('mousedown', (event) => {
            isMouseDown = true;
            mouseX = event.clientX;
            mouseY = event.clientY;
        });
        
        this.renderer.domElement.addEventListener('mouseup', () => {
            isMouseDown = false;
        });
        
        this.renderer.domElement.addEventListener('mousemove', (event) => {
            if (!isMouseDown) return;
            
            const deltaX = event.clientX - mouseX;
            const deltaY = event.clientY - mouseY;
            
            this.camera.position.x += deltaX * 0.01;
            this.camera.position.y -= deltaY * 0.01;
            
            mouseX = event.clientX;
            mouseY = event.clientY;
            
            this.updateCameraDisplay();
        });
        
        // Zoom with mouse wheel
        this.renderer.domElement.addEventListener('wheel', (event) => {
            this.camera.position.z += event.deltaY * 0.01;
            this.camera.position.z = Math.max(5, Math.min(50, this.camera.position.z));
            this.updateCameraDisplay();
        });
    }
    
    loadTimelineData() {''' + f'''
        // Timeline data from Python
        const timelineData = {json.dumps({
            'nodes': dict(self.nodes),
            'edges': self.edges,
            'quantum_events': self.quantum_events
        }, indent=2)};
        
        this.createNodes(timelineData.nodes);
        this.createEdges(timelineData.edges);
        this.createQuantumEffects(timelineData.quantum_events);
        
        this.updateStats();
    }}
    
    createNodes(nodesData) {{
        const geometries = {{
            standard: new THREE.SphereGeometry(0.5, 16, 16),
            quantum: new THREE.OctahedronGeometry(0.7),
            temporal: new THREE.BoxGeometry(1, 1, 1),
            paradox: new THREE.TetrahedronGeometry(0.8)
        }};
        
        const materials = {{
            standard: new THREE.MeshPhongMaterial({{ color: 0x4CAF50 }}),
            quantum: new THREE.MeshPhongMaterial({{ 
                color: 0xF44336, 
                transparent: true, 
                opacity: 0.8,
                emissive: 0x220000
            }}),
            temporal: new THREE.MeshPhongMaterial({{ color: 0x2196F3 }}),
            paradox: new THREE.MeshPhongMaterial({{ 
                color: 0xFF9800,
                emissive: 0x331100
            }})
        }};
        
        Object.entries(nodesData).forEach(([name, data]) => {{
            const geometry = geometries[data.type] || geometries.standard;
            const material = materials[data.type] || materials.standard;
            
            const mesh = new THREE.Mesh(geometry, material);
            mesh.position.set(...data.position);
            mesh.castShadow = true;
            mesh.receiveShadow = true;
            mesh.userData = {{ name, ...data }};
            
            this.scene.add(mesh);
            this.nodeObjects.set(name, mesh);
            
            // Add label
            this.addNodeLabel(mesh, name);
        }});
    }}
    
    addNodeLabel(node, text) {{
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.width = 256;
        canvas.height = 64;
        
        context.font = '20px Arial';
        context.fillStyle = 'white';
        context.textAlign = 'center';
        context.fillText(text, 128, 32);
        
        const texture = new THREE.CanvasTexture(canvas);
        const material = new THREE.SpriteMaterial({{ map: texture }});
        const sprite = new THREE.Sprite(material);
        sprite.scale.set(2, 0.5, 1);
        sprite.position.copy(node.position);
        sprite.position.y += 1;
        
        this.scene.add(sprite);
    }}
    
    createEdges(edgesData) {{
        edgesData.forEach(edge => {{
            const sourceNode = this.nodeObjects.get(edge.source);
            const targetNode = this.nodeObjects.get(edge.target);
            
            if (!sourceNode || !targetNode) return;
            
            const geometry = new THREE.BufferGeometry().setFromPoints([
                sourceNode.position,
                targetNode.position
            ]);
            
            const material = new THREE.LineBasicMaterial({{ 
                color: edge.type === 'quantum' ? 0xF44336 : 
                       edge.type === 'temporal' ? 0x2196F3 : 0x999999,
                linewidth: 2
            }});
            
            const line = new THREE.Line(geometry, material);
            line.userData = edge;
            
            this.scene.add(line);
            this.edgeObjects.push(line);
        }});
    }}
    
    createQuantumEffects(quantumEvents) {{
        quantumEvents.forEach(event => {{
            const node = this.nodeObjects.get(event.node);
            if (!node) return;
            
            // Create quantum particle system
            const particleGeometry = new THREE.BufferGeometry();
            const particleCount = 50;
            const positions = new Float32Array(particleCount * 3);
            
            for (let i = 0; i < particleCount * 3; i += 3) {{
                positions[i] = node.position.x + (Math.random() - 0.5) * 4;
                positions[i + 1] = node.position.y + (Math.random() - 0.5) * 4;
                positions[i + 2] = node.position.z + (Math.random() - 0.5) * 4;
            }}
            
            particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            
            const particleMaterial = new THREE.PointsMaterial({{
                color: 0x00ffff,
                size: 0.1,
                transparent: true,
                opacity: 0.6
            }});
            
            const particles = new THREE.Points(particleGeometry, particleMaterial);
            this.scene.add(particles);
            this.quantumParticles.push(particles);
        }});
    }}
    
    animate() {{
        requestAnimationFrame(() => this.animate());
        
        if (this.animating) {{
            // Rotate camera around origin
            const time = Date.now() * 0.0005;
            
            // Animate quantum particles
            this.quantumParticles.forEach((particles, index) => {{
                particles.rotation.x += 0.01;
                particles.rotation.y += 0.02;
                
                const positions = particles.geometry.attributes.position.array;
                for (let i = 0; i < positions.length; i += 3) {{
                    positions[i + 1] += Math.sin(time + i) * 0.01;
                }}
                particles.geometry.attributes.position.needsUpdate = true;
            }});
            
            // Pulse quantum nodes
            this.nodeObjects.forEach(node => {{
                if (node.userData.type === 'quantum') {{
                    const scale = 1 + Math.sin(time * 3) * 0.2;
                    node.scale.setScalar(scale);
                }}
            }});
        }}
        
        this.renderer.render(this.scene, this.camera);
    }}
    
    onWindowResize() {{
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }}
    
    onNodeClick(event) {{
        const mouse = new THREE.Vector2();
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
        
        const raycaster = new THREE.Raycaster();
        raycaster.setFromCamera(mouse, this.camera);
        
        const intersects = raycaster.intersectObjects(Array.from(this.nodeObjects.values()));
        
        if (intersects.length > 0) {{
            const selectedNode = intersects[0].object;
            this.selectNode(selectedNode);
        }}
    }}
    
    selectNode(node) {{
        // Reset previous selection
        if (this.selectedNode) {{
            this.selectedNode.material.emissive.setHex(0x000000);
        }}
        
        // Highlight new selection
        this.selectedNode = node;
        node.material.emissive.setHex(0x333333);
        
        document.getElementById('selectedNode').textContent = node.userData.name;
    }}
    
    updateCameraDisplay() {{
        const pos = this.camera.position;
        document.getElementById('cameraPos').textContent = 
            `${{pos.x.toFixed(1)}},${{pos.y.toFixed(1)}},${{pos.z.toFixed(1)}}`;
    }}
    
    updateStats() {{
        document.getElementById('nodeCount').textContent = this.nodeObjects.size;
        document.getElementById('edgeCount').textContent = this.edgeObjects.length;
        document.getElementById('quantumCount').textContent = this.quantumParticles.length;
    }}
}}

// Global functions for controls
let visualization;

function resetView() {{
    visualization.camera.position.set(0, 0, 20);
    visualization.camera.lookAt(0, 0, 0);
    visualization.updateCameraDisplay();
}}

function toggleAnimation() {{
    visualization.animating = !visualization.animating;
}}

function quantumCollapse() {{
    // Simulate quantum collapse
    visualization.nodeObjects.forEach(node => {{
        if (node.userData.type === 'quantum') {{
            node.material.opacity = Math.random() > 0.5 ? 1.0 : 0.3;
        }}
    }});
}}

function showParadox() {{
    // Create paradox effect
    const paradoxGeometry = new THREE.TorusGeometry(2, 0.5, 8, 16);
    const paradoxMaterial = new THREE.MeshPhongMaterial({{ 
        color: 0xFF5722,
        transparent: true,
        opacity: 0.7,
        emissive: 0x331100
    }});
    
    const paradoxTorus = new THREE.Mesh(paradoxGeometry, paradoxMaterial);
    paradoxTorus.position.set(0, 0, 0);
    
    visualization.scene.add(paradoxTorus);
    
    // Animate and remove after 3 seconds
    const animate = () => {{
        paradoxTorus.rotation.x += 0.1;
        paradoxTorus.rotation.y += 0.05;
    }};
    
    const interval = setInterval(animate, 16);
    setTimeout(() => {{
        clearInterval(interval);
        visualization.scene.remove(paradoxTorus);
    }}, 3000);
}}

function toggleWireframe() {{
    visualization.wireframe = !visualization.wireframe;
    visualization.nodeObjects.forEach(node => {{
        node.material.wireframe = visualization.wireframe;
    }});
}}

function exportTimeline() {{
    const data = {{
        nodes: Array.from(visualization.nodeObjects.entries()).map(([name, node]) => ({{
            name,
            position: node.position.toArray(),
            type: node.userData.type
        }})),
        edges: visualization.edgeObjects.map(edge => edge.userData),
        camera: visualization.camera.position.toArray()
    }};
    
    const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'qtime_3d_export.json';
    a.click();
    URL.revokeObjectURL(url);
}}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {{
    visualization = new QTime3DVisualization();
}});
</script>
</body>
</html>'''
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"3D timeline visualization saved to: {output_file}")

def create_sample_3d_timeline():
    """Create a sample 3D timeline"""
    qt = QTime3D()
    
    # Add nodes in 3D space
    qt.add_node("Origin", [0, 0, 0], "temporal")
    qt.add_node("You", [-5, 2, 1], "standard")
    qt.add_node("@vsk2k0725", [-5, -2, -1], "standard")
    qt.add_node("Meeting", [-1, 0, 0], "quantum")
    qt.add_node("Split", [3, 3, 2], "quantum")
    qt.add_node("Merge", [3, -3, -2], "standard")
    qt.add_node("Superposition", [5, 0, 3], "quantum")
    qt.add_node("Paradox", [2, 2, -3], "paradox")
    qt.add_node("Future_A", [8, 4, 1], "temporal")
    qt.add_node("Future_B", [8, 0, 0], "temporal")
    qt.add_node("Future_C", [8, -4, -1], "temporal")
    
    # Add edges
    qt.add_edge("Origin", "You", "temporal")
    qt.add_edge("Origin", "@vsk2k0725", "temporal")
    qt.add_edge("You", "Meeting", "convergence")
    qt.add_edge("@vsk2k0725", "Meeting", "convergence")
    qt.add_edge("Meeting", "Split", "quantum")
    qt.add_edge("Meeting", "Merge", "quantum")
    qt.add_edge("Meeting", "Superposition", "quantum")
    qt.add_edge("Split", "Paradox", "paradox")
    qt.add_edge("Split", "Future_A", "outcome")
    qt.add_edge("Merge", "Future_B", "outcome")
    qt.add_edge("Superposition", "Future_C", "outcome")
    
    # Add quantum events
    qt.add_quantum_event("Meeting", "superposition", 0.8)
    qt.add_quantum_event("Split", "bifurcation", 0.6)
    qt.add_quantum_event("Superposition", "entanglement", 0.9)
    qt.add_quantum_event("Paradox", "causality_violation", 0.3)
    
    return qt

if __name__ == "__main__":
    # Create sample 3D timeline
    timeline = create_sample_3d_timeline()
    timeline.generate_3d_html("qtime_3d_immersive.html")
    print("QTime 3D Timeline generated successfully!")
    print("Open qtime_3d_immersive.html in a modern web browser to explore the 3D timeline.")
