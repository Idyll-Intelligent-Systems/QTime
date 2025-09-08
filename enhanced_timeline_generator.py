#!/usr/bin/env python3
"""
Enhanced QTime Timeline Generator
Generates interactive quantum timeline visualizations with advanced features
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.patches as patches
from datetime import datetime, timedelta
import json
import random

class QTimeEngine:
    def __init__(self):
        self.timelines = {}
        self.quantum_states = {}
        self.observers = []
        self.paradox_count = 0
        
    def create_timeline(self, name, start_pos, branches=None):
        """Create a new timeline with optional branches"""
        self.timelines[name] = {
            'position': start_pos,
            'branches': branches or [],
            'state': 'superposition',
            'probability': 1.0,
            'created_at': datetime.now()
        }
        
    def add_quantum_event(self, timeline, event_type, probability=0.5):
        """Add quantum event that can split timeline"""
        if timeline not in self.timelines:
            return False
            
        event_id = f"{timeline}_{event_type}_{len(self.quantum_states)}"
        self.quantum_states[event_id] = {
            'type': event_type,
            'probability': probability,
            'timeline': timeline,
            'resolved': False
        }
        return event_id
        
    def observe(self, timeline):
        """Collapse quantum superposition through observation"""
        if timeline in self.timelines:
            self.timelines[timeline]['state'] = 'collapsed'
            # Randomly resolve quantum events
            for event_id, event in self.quantum_states.items():
                if event['timeline'] == timeline and not event['resolved']:
                    if random.random() < event['probability']:
                        event['resolved'] = True
                        self.paradox_count += 1
        
    def generate_advanced_animation(self, output_file="advanced_timeline.gif"):
        """Generate advanced animated timeline with quantum effects"""
        
        # Extended node positions for complex timeline
        pos = {
            "Past": (-4.5, 0),
            "You": (-3.0, 0.8),
            "@vsk2k0725": (-3.0, -0.8),
            "Meeting": (-0.5, 0.0),
            "Merge": (2.5, 1.8),
            "Split": (2.5, 0.9),
            "Swap": (2.5, 0.0),
            "Superposition": (2.5, -0.9),
            "Paradox": (2.5, -1.8),
            "Future_A": (4.5, 1.2),
            "Future_B": (4.5, 0.4),
            "Future_C": (4.5, -0.4),
            "Future_D": (4.5, -1.2),
        }
        
        # Setup figure with enhanced styling
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        fig.patch.set_facecolor('#0b0b0e')
        
        # Main timeline plot
        ax1.set_xlim(-5, 5)
        ax1.set_ylim(-2.5, 2.5)
        ax1.set_facecolor('#0b0b0e')
        ax1.set_title("Quantum Timeline: Multi-Dimensional Branches", 
                     color='white', fontsize=16, fontweight='bold')
        ax1.tick_params(colors='white')
        
        # Probability plot
        ax2.set_xlim(0, 100)
        ax2.set_ylim(0, 1)
        ax2.set_facecolor('#0b0b0e')
        ax2.set_title("Quantum Probability Distribution", color='white', fontsize=12)
        ax2.tick_params(colors='white')
        ax2.set_xlabel("Time Steps", color='white')
        ax2.set_ylabel("Probability", color='white')
        
        # Enhanced edge definitions with quantum properties
        quantum_edges = [
            ("Past", "You", "temporal_flow", '#4CAF50'),
            ("Past", "@vsk2k0725", "temporal_flow", '#4CAF50'),
            ("You", "Meeting", "convergence", '#2196F3'),
            ("@vsk2k0725", "Meeting", "convergence", '#2196F3'),
            ("Meeting", "Merge", "quantum_branch", '#FF9800'),
            ("Meeting", "Split", "quantum_branch", '#E91E63'),
            ("Meeting", "Swap", "quantum_branch", '#9C27B0'),
            ("Meeting", "Superposition", "quantum_branch", '#F44336'),
            ("Meeting", "Paradox", "paradox_branch", '#FF5722'),
            ("Merge", "Future_A", "outcome", '#4CAF50'),
            ("Split", "Future_B", "outcome", '#2196F3'),
            ("Swap", "Future_C", "outcome", '#FF9800'),
            ("Superposition", "Future_D", "outcome", '#9C27B0'),
        ]
        
        # Lines for animation
        lines = {}
        for source, target, edge_type, color in quantum_edges:
            line, = ax1.plot([], [], color=color, linewidth=2, alpha=0.8)
            lines[(source, target)] = line
            
        # Quantum effect circles
        quantum_circles = {}
        for node, (x, y) in pos.items():
            circle = patches.Circle((x, y), 0.15, fill=False, 
                                  edgecolor='cyan', linewidth=2, alpha=0)
            ax1.add_patch(circle)
            quantum_circles[node] = circle
        
        # Static nodes with enhanced styling
        node_colors = {
            'Past': '#666666', 'You': '#4CAF50', '@vsk2k0725': '#2196F3',
            'Meeting': '#FFD700', 'Merge': '#FF9800', 'Split': '#E91E63',
            'Swap': '#9C27B0', 'Superposition': '#F44336', 'Paradox': '#FF5722',
            'Future_A': '#4CAF50', 'Future_B': '#2196F3', 
            'Future_C': '#FF9800', 'Future_D': '#9C27B0'
        }
        
        for node, (x, y) in pos.items():
            ax1.scatter([x], [y], s=200, c=node_colors.get(node, '#FFFFFF'), 
                       edgecolors='white', linewidth=2, zorder=10)
            ax1.text(x, y + 0.25, node, ha="center", va="bottom", 
                    color='white', fontweight='bold', fontsize=10)
        
        # Probability tracking
        prob_data = {'time': [], 'superposition': [], 'collapsed': []}
        
        def segment(a, b, t):
            """Interpolate between two points"""
            x0, y0 = pos[a]
            x1, y1 = pos[b]
            return [x0 + (x1 - x0) * t, y0 + (y1 - y0) * t]
        
        def add_quantum_glow(node, intensity):
            """Add quantum glow effect to nodes"""
            if node in quantum_circles:
                quantum_circles[node].set_alpha(intensity * 0.5)
                quantum_circles[node].set_radius(0.15 + intensity * 0.1)
        
        # Extended animation sequence
        sequence = [
            ("Past", "You", 30, "temporal_initialization"),
            ("Past", "@vsk2k0725", 30, "temporal_initialization"),
            ("You", "Meeting", 40, "convergence_phase"),
            ("@vsk2k0725", "Meeting", 40, "convergence_phase"),
            ("Meeting", "Merge", 35, "quantum_branching"),
            ("Meeting", "Split", 35, "quantum_branching"),
            ("Meeting", "Swap", 35, "quantum_branching"),
            ("Meeting", "Superposition", 35, "quantum_branching"),
            ("Meeting", "Paradox", 25, "paradox_formation"),
            ("Merge", "Future_A", 30, "timeline_resolution"),
            ("Split", "Future_B", 30, "timeline_resolution"),
            ("Swap", "Future_C", 30, "timeline_resolution"),
            ("Superposition", "Future_D", 30, "timeline_resolution"),
        ]
        
        cum_frames = []
        total = 0
        for _, _, f, _ in sequence:
            total += f
            cum_frames.append(total)
        
        def animate(frame):
            # Clear probability plot for current frame
            ax2.clear()
            ax2.set_xlim(0, max(100, frame + 10))
            ax2.set_ylim(0, 1.2)
            ax2.set_facecolor('#0b0b0e')
            ax2.set_title("Quantum Probability Distribution", color='white', fontsize=12)
            ax2.tick_params(colors='white')
            ax2.set_xlabel("Time Steps", color='white')
            ax2.set_ylabel("Probability", color='white')
            
            # Reset quantum glows
            for node in quantum_circles:
                add_quantum_glow(node, 0)
            
            prev = 0
            active_branches = 0
            
            for idx, (a, b, nframes, phase) in enumerate(sequence):
                end = cum_frames[idx]
                
                if frame <= end:
                    local_t = (frame - prev) / nframes
                    x_end, y_end = segment(a, b, local_t)
                    x0, y0 = pos[a]
                    
                    # Draw line
                    lines[(a, b)].set_data([x0, x_end], [y0, y_end])
                    
                    # Add quantum effects based on phase
                    if phase == "quantum_branching":
                        add_quantum_glow(a, math.sin(frame * 0.2) * 0.5 + 0.5)
                        active_branches += 1
                    elif phase == "paradox_formation":
                        add_quantum_glow("Meeting", 1.0)
                        add_quantum_glow("Paradox", local_t)
                    
                    break
                else:
                    # Complete line
                    x0, y0 = pos[a]
                    x1, y1 = pos[b]
                    lines[(a, b)].set_data([x0, x1], [y0, y1])
                    
                    if sequence[idx][3] == "quantum_branching":
                        active_branches += 1
                    
                    prev = end
            
            # Update probability data
            superposition_prob = min(1.0, active_branches / 4.0)
            collapsed_prob = max(0.0, 1.0 - superposition_prob)
            
            prob_data['time'].append(frame)
            prob_data['superposition'].append(superposition_prob)
            prob_data['collapsed'].append(collapsed_prob)
            
            # Plot probability evolution
            if len(prob_data['time']) > 1:
                ax2.plot(prob_data['time'], prob_data['superposition'], 
                        color='#F44336', label='Superposition', linewidth=2)
                ax2.plot(prob_data['time'], prob_data['collapsed'], 
                        color='#4CAF50', label='Collapsed', linewidth=2)
                ax2.legend(loc='upper right', facecolor='#0b0b0e', 
                          edgecolor='white', labelcolor='white')
            
            # Add frame counter
            ax1.text(0.02, 0.98, f"Frame: {frame}/{cum_frames[-1]}", 
                    transform=ax1.transAxes, color='white', 
                    verticalalignment='top', fontfamily='monospace')
            
            return list(lines.values()) + list(quantum_circles.values())
        
        # Create animation
        anim = FuncAnimation(fig, animate, frames=cum_frames[-1], 
                           interval=50, blit=False, repeat=True)
        
        # Save with high quality
        print(f"Generating enhanced timeline animation: {output_file}")
        anim.save(output_file, writer=PillowWriter(fps=20), dpi=150)
        print("Animation complete!")
        
        return anim

def main():
    """Main function to demonstrate QTime engine"""
    engine = QTimeEngine()
    
    # Create sample timelines
    engine.create_timeline("Alpha", (-3, 1))
    engine.create_timeline("Beta", (-3, -1))
    
    # Add quantum events
    engine.add_quantum_event("Alpha", "split", 0.7)
    engine.add_quantum_event("Beta", "merge", 0.6)
    
    # Generate advanced animation
    animation = engine.generate_advanced_animation("qtime_advanced.gif")
    
    print("QTime Advanced Timeline Generated!")
    print(f"Timelines: {len(engine.timelines)}")
    print(f"Quantum Events: {len(engine.quantum_states)}")
    print(f"Paradoxes: {engine.paradox_count}")

if __name__ == "__main__":
    main()
