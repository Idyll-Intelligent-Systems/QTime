#!/usr/bin/env python3
"""
QTime API - REST API for timeline management
"""

from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import json
import uuid
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# Database setup
DATABASE = 'qtime.db'

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS timelines (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            data TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quantum_events (
            id TEXT PRIMARY KEY,
            timeline_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            node TEXT NOT NULL,
            probability REAL NOT NULL,
            resolved BOOLEAN DEFAULT FALSE,
            created_at TEXT NOT NULL,
            FOREIGN KEY (timeline_id) REFERENCES timelines (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """API documentation page"""
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>QTime API Documentation</title>
    <style>
        body { 
            font-family: 'Consolas', monospace; 
            background: #0b0b0e; 
            color: #eee; 
            padding: 20px; 
            line-height: 1.6;
        }
        .container { max-width: 1000px; margin: 0 auto; }
        h1, h2 { color: #4CAF50; }
        .endpoint { 
            background: #1a1a22; 
            padding: 15px; 
            margin: 10px 0; 
            border-radius: 8px; 
            border: 1px solid #333;
        }
        .method { 
            display: inline-block; 
            padding: 4px 8px; 
            border-radius: 4px; 
            font-weight: bold; 
            margin-right: 10px;
        }
        .get { background: #4CAF50; }
        .post { background: #2196F3; }
        .put { background: #FF9800; }
        .delete { background: #F44336; }
        pre { 
            background: #111; 
            padding: 10px; 
            border-radius: 5px; 
            overflow-x: auto;
            border: 1px solid #333;
        }
        .status { color: #00ff88; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌌 QTime API Documentation</h1>
        <p class="status">Server Status: Online | Quantum Engine: Active</p>
        
        <h2>📚 Endpoints</h2>
        
        <div class="endpoint">
            <span class="method get">GET</span><strong>/api/timelines</strong>
            <p>Retrieve all timelines</p>
            <pre>Response: [{"id": "uuid", "name": "Timeline Name", "created_at": "ISO-8601", ...}]</pre>
        </div>
        
        <div class="endpoint">
            <span class="method post">POST</span><strong>/api/timelines</strong>
            <p>Create a new timeline</p>
            <pre>Body: {"name": "Timeline Name", "nodes": {...}, "edges": [...]}</pre>
        </div>
        
        <div class="endpoint">
            <span class="method get">GET</span><strong>/api/timelines/&lt;id&gt;</strong>
            <p>Retrieve specific timeline</p>
        </div>
        
        <div class="endpoint">
            <span class="method put">PUT</span><strong>/api/timelines/&lt;id&gt;</strong>
            <p>Update timeline</p>
            <pre>Body: {"name": "New Name", "data": {...}}</pre>
        </div>
        
        <div class="endpoint">
            <span class="method delete">DELETE</span><strong>/api/timelines/&lt;id&gt;</strong>
            <p>Delete timeline</p>
        </div>
        
        <div class="endpoint">
            <span class="method post">POST</span><strong>/api/timelines/&lt;id&gt;/quantum-events</strong>
            <p>Add quantum event to timeline</p>
            <pre>Body: {"type": "split", "node": "Meeting", "probability": 0.7}</pre>
        </div>
        
        <div class="endpoint">
            <span class="method get">GET</span><strong>/api/timelines/&lt;id&gt;/quantum-events</strong>
            <p>Get all quantum events for timeline</p>
        </div>
        
        <div class="endpoint">
            <span class="method post">POST</span><strong>/api/timelines/&lt;id&gt;/observe</strong>
            <p>Collapse quantum superposition</p>
        </div>
        
        <div class="endpoint">
            <span class="method get">GET</span><strong>/api/health</strong>
            <p>API health check</p>
        </div>
        
        <h2>🚀 Quick Start</h2>
        <pre>
# Create a timeline
curl -X POST http://localhost:5000/api/timelines \\
  -H "Content-Type: application/json" \\
  -d '{"name": "My Timeline", "nodes": {"start": [0,0]}, "edges": []}'

# Add quantum event  
curl -X POST http://localhost:5000/api/timelines/TIMELINE_ID/quantum-events \\
  -H "Content-Type: application/json" \\
  -d '{"type": "split", "node": "start", "probability": 0.5}'

# Observe timeline (collapse superposition)
curl -X POST http://localhost:5000/api/timelines/TIMELINE_ID/observe
        </pre>
    </div>
</body>
</html>
    ''')

@app.route('/api/health')
def health_check():
    """API health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0',
        'quantum_engine': 'active'
    })

@app.route('/api/timelines', methods=['GET'])
def get_timelines():
    """Get all timelines"""
    conn = get_db_connection()
    timelines = conn.execute('SELECT * FROM timelines ORDER BY created_at DESC').fetchall()
    conn.close()
    
    result = []
    for timeline in timelines:
        result.append({
            'id': timeline['id'],
            'name': timeline['name'],
            'created_at': timeline['created_at'],
            'updated_at': timeline['updated_at']
        })
    
    return jsonify(result)

@app.route('/api/timelines', methods=['POST'])
def create_timeline():
    """Create a new timeline"""
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Timeline name is required'}), 400
    
    timeline_id = str(uuid.uuid4())
    timeline_data = {
        'nodes': data.get('nodes', {}),
        'edges': data.get('edges', []),
        'quantum_events': [],
        'created_by': 'api'
    }
    
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO timelines (id, name, data, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
        (timeline_id, data['name'], json.dumps(timeline_data), 
         datetime.now().isoformat(), datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    
    return jsonify({
        'id': timeline_id,
        'name': data['name'],
        'message': 'Timeline created successfully'
    }), 201

@app.route('/api/timelines/<timeline_id>', methods=['GET'])
def get_timeline(timeline_id):
    """Get specific timeline"""
    conn = get_db_connection()
    timeline = conn.execute(
        'SELECT * FROM timelines WHERE id = ?', (timeline_id,)
    ).fetchone()
    conn.close()
    
    if not timeline:
        return jsonify({'error': 'Timeline not found'}), 404
    
    timeline_data = json.loads(timeline['data'])
    
    return jsonify({
        'id': timeline['id'],
        'name': timeline['name'],
        'data': timeline_data,
        'created_at': timeline['created_at'],
        'updated_at': timeline['updated_at']
    })

@app.route('/api/timelines/<timeline_id>', methods=['PUT'])
def update_timeline(timeline_id):
    """Update timeline"""
    data = request.get_json()
    
    conn = get_db_connection()
    timeline = conn.execute(
        'SELECT * FROM timelines WHERE id = ?', (timeline_id,)
    ).fetchone()
    
    if not timeline:
        conn.close()
        return jsonify({'error': 'Timeline not found'}), 404
    
    # Update timeline
    timeline_data = json.loads(timeline['data'])
    
    if 'name' in data:
        name = data['name']
    else:
        name = timeline['name']
    
    if 'data' in data:
        timeline_data.update(data['data'])
    
    conn.execute(
        'UPDATE timelines SET name = ?, data = ?, updated_at = ? WHERE id = ?',
        (name, json.dumps(timeline_data), datetime.now().isoformat(), timeline_id)
    )
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Timeline updated successfully'})

@app.route('/api/timelines/<timeline_id>', methods=['DELETE'])
def delete_timeline(timeline_id):
    """Delete timeline"""
    conn = get_db_connection()
    
    # Check if timeline exists
    timeline = conn.execute(
        'SELECT * FROM timelines WHERE id = ?', (timeline_id,)
    ).fetchone()
    
    if not timeline:
        conn.close()
        return jsonify({'error': 'Timeline not found'}), 404
    
    # Delete timeline and associated quantum events
    conn.execute('DELETE FROM quantum_events WHERE timeline_id = ?', (timeline_id,))
    conn.execute('DELETE FROM timelines WHERE id = ?', (timeline_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Timeline deleted successfully'})

@app.route('/api/timelines/<timeline_id>/quantum-events', methods=['GET'])
def get_quantum_events(timeline_id):
    """Get quantum events for timeline"""
    conn = get_db_connection()
    
    # Check if timeline exists
    timeline = conn.execute(
        'SELECT * FROM timelines WHERE id = ?', (timeline_id,)
    ).fetchone()
    
    if not timeline:
        conn.close()
        return jsonify({'error': 'Timeline not found'}), 404
    
    events = conn.execute(
        'SELECT * FROM quantum_events WHERE timeline_id = ? ORDER BY created_at DESC',
        (timeline_id,)
    ).fetchall()
    conn.close()
    
    result = []
    for event in events:
        result.append({
            'id': event['id'],
            'type': event['event_type'],
            'node': event['node'],
            'probability': event['probability'],
            'resolved': bool(event['resolved']),
            'created_at': event['created_at']
        })
    
    return jsonify(result)

@app.route('/api/timelines/<timeline_id>/quantum-events', methods=['POST'])
def add_quantum_event(timeline_id):
    """Add quantum event to timeline"""
    data = request.get_json()
    
    if not data or not all(k in data for k in ['type', 'node', 'probability']):
        return jsonify({'error': 'type, node, and probability are required'}), 400
    
    conn = get_db_connection()
    
    # Check if timeline exists
    timeline = conn.execute(
        'SELECT * FROM timelines WHERE id = ?', (timeline_id,)
    ).fetchone()
    
    if not timeline:
        conn.close()
        return jsonify({'error': 'Timeline not found'}), 404
    
    event_id = str(uuid.uuid4())
    
    conn.execute(
        'INSERT INTO quantum_events (id, timeline_id, event_type, node, probability, created_at) VALUES (?, ?, ?, ?, ?, ?)',
        (event_id, timeline_id, data['type'], data['node'], 
         data['probability'], datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    
    return jsonify({
        'id': event_id,
        'message': 'Quantum event added successfully'
    }), 201

@app.route('/api/timelines/<timeline_id>/observe', methods=['POST'])
def observe_timeline(timeline_id):
    """Collapse quantum superposition through observation"""
    import random
    
    conn = get_db_connection()
    
    # Check if timeline exists
    timeline = conn.execute(
        'SELECT * FROM timelines WHERE id = ?', (timeline_id,)
    ).fetchone()
    
    if not timeline:
        conn.close()
        return jsonify({'error': 'Timeline not found'}), 404
    
    # Get unresolved quantum events
    events = conn.execute(
        'SELECT * FROM quantum_events WHERE timeline_id = ? AND resolved = FALSE',
        (timeline_id,)
    ).fetchall()
    
    collapsed_events = []
    
    # Simulate quantum measurement
    for event in events:
        if random.random() < event['probability']:
            conn.execute(
                'UPDATE quantum_events SET resolved = TRUE WHERE id = ?',
                (event['id'],)
            )
            collapsed_events.append({
                'id': event['id'],
                'type': event['event_type'],
                'node': event['node'],
                'probability': event['probability']
            })
    
    conn.commit()
    conn.close()
    
    return jsonify({
        'message': 'Quantum observation complete',
        'collapsed_events': collapsed_events,
        'total_collapsed': len(collapsed_events)
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run the API server
    print("🌌 Starting QTime API Server...")
    print("📚 API Documentation: http://localhost:5000/")
    print("🔍 Health Check: http://localhost:5000/api/health")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
