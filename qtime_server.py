#!/usr/bin/env python3
"""
QTime WebSocket Server
Real-time quantum timeline synchronization server
"""

import asyncio
import websockets
import json
import uuid
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QTimeServer:
    def __init__(self):
        self.clients = {}
        self.timelines = {}
        self.quantum_states = {}
        self.active_sessions = {}
        
    async def register_client(self, websocket, path):
        """Register a new client connection"""
        client_id = str(uuid.uuid4())
        self.clients[client_id] = {
            'websocket': websocket,
            'connected_at': datetime.now().isoformat(),
            'timeline_id': None
        }
        
        logger.info(f"Client {client_id} connected")
        
        # Send welcome message
        await self.send_message(websocket, {
            'type': 'connection_established',
            'client_id': client_id,
            'server_time': datetime.now().isoformat()
        })
        
        try:
            async for message in websocket:
                await self.handle_message(client_id, json.loads(message))
        except websockets.exceptions.ConnectionClosed:
            logger.info(f"Client {client_id} disconnected")
        finally:
            del self.clients[client_id]
    
    async def handle_message(self, client_id, message):
        """Handle incoming messages from clients"""
        msg_type = message.get('type')
        client = self.clients.get(client_id)
        
        if not client:
            return
            
        if msg_type == 'create_timeline':
            await self.create_timeline(client_id, message['data'])
            
        elif msg_type == 'join_timeline':
            await self.join_timeline(client_id, message['timeline_id'])
            
        elif msg_type == 'quantum_event':
            await self.handle_quantum_event(client_id, message)
            
        elif msg_type == 'timeline_update':
            await self.broadcast_timeline_update(client_id, message)
            
        elif msg_type == 'paradox_detected':
            await self.handle_paradox(client_id, message)
            
        elif msg_type == 'observation':
            await self.handle_observation(client_id, message)
    
    async def create_timeline(self, client_id, timeline_data):
        """Create a new collaborative timeline"""
        timeline_id = str(uuid.uuid4())
        
        self.timelines[timeline_id] = {
            'id': timeline_id,
            'creator': client_id,
            'created_at': datetime.now().isoformat(),
            'participants': [client_id],
            'nodes': timeline_data.get('nodes', {}),
            'edges': timeline_data.get('edges', []),
            'quantum_events': [],
            'state': 'superposition'
        }
        
        self.clients[client_id]['timeline_id'] = timeline_id
        
        logger.info(f"Timeline {timeline_id} created by {client_id}")
        
        await self.send_message(self.clients[client_id]['websocket'], {
            'type': 'timeline_created',
            'timeline_id': timeline_id,
            'timeline_data': self.timelines[timeline_id]
        })
    
    async def join_timeline(self, client_id, timeline_id):
        """Join an existing timeline"""
        if timeline_id not in self.timelines:
            await self.send_message(self.clients[client_id]['websocket'], {
                'type': 'error',
                'message': f'Timeline {timeline_id} not found'
            })
            return
            
        timeline = self.timelines[timeline_id]
        
        if client_id not in timeline['participants']:
            timeline['participants'].append(client_id)
            
        self.clients[client_id]['timeline_id'] = timeline_id
        
        # Send current timeline state
        await self.send_message(self.clients[client_id]['websocket'], {
            'type': 'timeline_joined',
            'timeline_id': timeline_id,
            'timeline_data': timeline
        })
        
        # Notify other participants
        await self.broadcast_to_timeline(timeline_id, {
            'type': 'participant_joined',
            'client_id': client_id,
            'participant_count': len(timeline['participants'])
        }, exclude_client=client_id)
        
        logger.info(f"Client {client_id} joined timeline {timeline_id}")
    
    async def handle_quantum_event(self, client_id, message):
        """Handle quantum events and synchronize across clients"""
        timeline_id = self.clients[client_id].get('timeline_id')
        
        if not timeline_id or timeline_id not in self.timelines:
            return
            
        event_data = message.get('data', {})
        event_id = str(uuid.uuid4())
        
        quantum_event = {
            'id': event_id,
            'type': event_data.get('type', 'unknown'),
            'client_id': client_id,
            'timestamp': datetime.now().isoformat(),
            'node': event_data.get('node'),
            'probability': event_data.get('probability', 0.5),
            'resolved': False
        }
        
        self.timelines[timeline_id]['quantum_events'].append(quantum_event)
        
        # Broadcast to all participants
        await self.broadcast_to_timeline(timeline_id, {
            'type': 'quantum_event_added',
            'event': quantum_event
        })
        
        logger.info(f"Quantum event {event_id} added to timeline {timeline_id}")
    
    async def handle_observation(self, client_id, message):
        """Handle quantum observation and collapse wave functions"""
        timeline_id = self.clients[client_id].get('timeline_id')
        
        if not timeline_id or timeline_id not in self.timelines:
            return
            
        timeline = self.timelines[timeline_id]
        observation_data = message.get('data', {})
        
        # Collapse quantum events
        collapsed_events = []
        for event in timeline['quantum_events']:
            if not event['resolved']:
                # Simulate quantum measurement
                import random
                if random.random() < event['probability']:
                    event['resolved'] = True
                    event['observed_by'] = client_id
                    event['collapsed_at'] = datetime.now().isoformat()
                    collapsed_events.append(event)
        
        if collapsed_events:
            timeline['state'] = 'partially_collapsed'
            
            await self.broadcast_to_timeline(timeline_id, {
                'type': 'quantum_collapse',
                'observer': client_id,
                'collapsed_events': collapsed_events,
                'timeline_state': timeline['state']
            })
            
            logger.info(f"Quantum collapse observed by {client_id} in timeline {timeline_id}")
    
    async def handle_paradox(self, client_id, message):
        """Handle paradox detection and resolution"""
        timeline_id = self.clients[client_id].get('timeline_id')
        
        if not timeline_id:
            return
            
        paradox_data = message.get('data', {})
        paradox_id = str(uuid.uuid4())
        
        paradox = {
            'id': paradox_id,
            'type': paradox_data.get('type', 'unknown'),
            'detected_by': client_id,
            'detected_at': datetime.now().isoformat(),
            'severity': paradox_data.get('severity', 'low'),
            'description': paradox_data.get('description', '')
        }
        
        # Broadcast paradox alert
        await self.broadcast_to_timeline(timeline_id, {
            'type': 'paradox_alert',
            'paradox': paradox
        })
        
        logger.warning(f"Paradox {paradox_id} detected in timeline {timeline_id}")
    
    async def broadcast_timeline_update(self, client_id, message):
        """Broadcast timeline updates to all participants"""
        timeline_id = self.clients[client_id].get('timeline_id')
        
        if not timeline_id:
            return
            
        update_data = message.get('data', {})
        
        # Update timeline
        if timeline_id in self.timelines:
            timeline = self.timelines[timeline_id]
            
            if 'nodes' in update_data:
                timeline['nodes'].update(update_data['nodes'])
                
            if 'edges' in update_data:
                timeline['edges'].extend(update_data['edges'])
        
        # Broadcast to all participants except sender
        await self.broadcast_to_timeline(timeline_id, {
            'type': 'timeline_updated',
            'updates': update_data,
            'updated_by': client_id
        }, exclude_client=client_id)
    
    async def broadcast_to_timeline(self, timeline_id, message, exclude_client=None):
        """Broadcast message to all participants in a timeline"""
        if timeline_id not in self.timelines:
            return
            
        timeline = self.timelines[timeline_id]
        
        for participant_id in timeline['participants']:
            if participant_id == exclude_client:
                continue
                
            if participant_id in self.clients:
                client = self.clients[participant_id]
                await self.send_message(client['websocket'], message)
    
    async def send_message(self, websocket, message):
        """Send message to a specific websocket"""
        try:
            await websocket.send(json.dumps(message))
        except websockets.exceptions.ConnectionClosed:
            logger.warning("Attempted to send message to closed connection")
        except Exception as e:
            logger.error(f"Error sending message: {e}")
    
    async def cleanup_inactive_timelines(self):
        """Periodically clean up inactive timelines"""
        while True:
            current_time = datetime.now()
            inactive_timelines = []
            
            for timeline_id, timeline in self.timelines.items():
                # Check if timeline has active participants
                active_participants = [
                    p for p in timeline['participants'] 
                    if p in self.clients
                ]
                
                if not active_participants:
                    inactive_timelines.append(timeline_id)
                else:
                    timeline['participants'] = active_participants
            
            # Remove inactive timelines
            for timeline_id in inactive_timelines:
                del self.timelines[timeline_id]
                logger.info(f"Cleaned up inactive timeline {timeline_id}")
            
            # Wait before next cleanup
            await asyncio.sleep(300)  # 5 minutes

async def main():
    """Start the QTime WebSocket server"""
    server = QTimeServer()
    
    # Start cleanup task
    cleanup_task = asyncio.create_task(server.cleanup_inactive_timelines())
    
    # Start WebSocket server
    logger.info("Starting QTime WebSocket server on localhost:8765")
    
    async with websockets.serve(server.register_client, "localhost", 8765):
        logger.info("QTime server is running...")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("QTime server shutting down...")
