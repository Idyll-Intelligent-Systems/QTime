#!/usr/bin/env python3
"""
QTime CLI - Command Line Interface for QTime Engine
"""

import argparse
import sys
import json
import os
from datetime import datetime
import subprocess
import webbrowser

class QTimeCLI:
    def __init__(self):
        self.version = "1.0.0"
        self.config_file = os.path.expanduser("~/.qtime_config.json")
        self.config = self.load_config()
    
    def load_config(self):
        """Load CLI configuration"""
        default_config = {
            "default_output_dir": "./qtime_output",
            "api_server": "http://localhost:5000",
            "websocket_server": "ws://localhost:8765",
            "auto_open_browser": True,
            "debug_mode": False
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except:
                pass
        
        return default_config
    
    def save_config(self):
        """Save CLI configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def create_output_dir(self):
        """Create output directory if it doesn't exist"""
        output_dir = self.config["default_output_dir"]
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_dir
    
    def generate_basic(self, args):
        """Generate basic timeline visualization"""
        print("🎞️ Generating basic QTime timeline...")
        
        # Create Python script for basic timeline
        script_content = '''
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
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.2, 2.2)
ax.axis("off")
ax.set_title("QTime: Quantum Timeline Branches")

# Create animation
lines = {}
for edge in [("You", "Meeting"), ("@vsk2k0725", "Meeting"), 
             ("Meeting", "Merge"), ("Meeting", "Split"), 
             ("Meeting", "Swap"), ("Meeting", "Superposition")]:
    lines[edge] = ax.plot([], [])[0]

# Static nodes
for node, (x, y) in pos.items():
    ax.scatter([x], [y], s=100, c='lightblue', edgecolors='navy')
    ax.text(x, y + 0.15, node, ha="center", fontweight='bold')

def animate(frame):
    # Simple animation logic
    for (a, b), line in lines.items():
        t = min(1.0, frame / 60.0)
        x0, y0 = pos[a]
        x1, y1 = pos[b]
        line.set_data([x0, x0 + (x1-x0)*t], [y0, y0 + (y1-y0)*t])
    return list(lines.values())

anim = FuncAnimation(fig, animate, frames=120, interval=50, blit=True)
''' + f'''
anim.save("{args.output or 'qtime_basic.gif'}", writer=PillowWriter(fps=20))
print("✅ Basic timeline generated: {args.output or 'qtime_basic.gif'}")
'''
        
        output_dir = self.create_output_dir()
        script_path = os.path.join(output_dir, "generate_basic.py")
        
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Run the script
        try:
            subprocess.run([sys.executable, script_path], check=True, cwd=output_dir)
            print(f"✅ Basic timeline generated in: {output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error generating timeline: {e}")
            return False
        
        return True
    
    def generate_advanced(self, args):
        """Generate advanced timeline visualization"""
        print("🌌 Generating advanced QTime timeline...")
        
        try:
            from enhanced_timeline_generator import QTimeEngine
            
            engine = QTimeEngine()
            engine.generate_advanced_animation(args.output or "qtime_advanced.gif")
            print(f"✅ Advanced timeline generated: {args.output or 'qtime_advanced.gif'}")
            return True
            
        except ImportError:
            print("❌ Enhanced timeline generator not found. Please ensure all dependencies are installed.")
            print("   Run: pip install -r requirements.txt")
            return False
        except Exception as e:
            print(f"❌ Error generating advanced timeline: {e}")
            return False
    
    def generate_3d(self, args):
        """Generate 3D timeline visualization"""
        print("🎨 Generating 3D QTime timeline...")
        
        try:
            from qtime_3d_generator import create_sample_3d_timeline
            
            timeline = create_sample_3d_timeline()
            output_file = args.output or "qtime_3d.html"
            timeline.generate_3d_html(output_file)
            
            print(f"✅ 3D timeline generated: {output_file}")
            
            if self.config["auto_open_browser"]:
                webbrowser.open(f"file://{os.path.abspath(output_file)}")
                print("🌐 Opened in browser")
            
            return True
            
        except ImportError:
            print("❌ 3D timeline generator not found. Please ensure all dependencies are installed.")
            return False
        except Exception as e:
            print(f"❌ Error generating 3D timeline: {e}")
            return False
    
    def generate_html(self, args):
        """Generate interactive HTML sandbox"""
        print("🌐 Generating HTML quantum sandbox...")
        
        output_file = args.output or "quantum_sandbox.html"
        
        # Copy the advanced HTML file
        try:
            if os.path.exists("quantum_sandbox_advanced.html"):
                import shutil
                shutil.copy("quantum_sandbox_advanced.html", output_file)
                print(f"✅ HTML sandbox generated: {output_file}")
                
                if self.config["auto_open_browser"]:
                    webbrowser.open(f"file://{os.path.abspath(output_file)}")
                    print("🌐 Opened in browser")
                
                return True
            else:
                print("❌ Advanced HTML template not found")
                return False
                
        except Exception as e:
            print(f"❌ Error generating HTML sandbox: {e}")
            return False
    
    def start_server(self, args):
        """Start QTime API server"""
        print("🚀 Starting QTime API server...")
        
        try:
            from qtime_api import app, init_db
            
            # Initialize database
            init_db()
            
            # Configure server
            host = args.host or '0.0.0.0'
            port = args.port or 5000
            debug = args.debug or self.config["debug_mode"]
            
            print(f"📚 API Documentation: http://{host}:{port}/")
            print(f"🔍 Health Check: http://{host}:{port}/api/health")
            print("Press Ctrl+C to stop")
            
            # Start server
            app.run(debug=debug, host=host, port=port)
            
        except ImportError:
            print("❌ QTime API not found. Please ensure Flask is installed.")
            print("   Run: pip install -r requirements.txt")
        except KeyboardInterrupt:
            print("\n👋 Server stopped")
        except Exception as e:
            print(f"❌ Error starting server: {e}")
    
    def start_websocket(self, args):
        """Start QTime WebSocket server"""
        print("🔌 Starting QTime WebSocket server...")
        
        try:
            subprocess.run([sys.executable, "qtime_server.py"], check=True)
        except FileNotFoundError:
            print("❌ QTime server not found")
        except KeyboardInterrupt:
            print("\n👋 WebSocket server stopped")
        except Exception as e:
            print(f"❌ Error starting WebSocket server: {e}")
    
    def config_command(self, args):
        """Handle configuration commands"""
        if args.action == "show":
            print("🔧 QTime Configuration:")
            for key, value in self.config.items():
                print(f"  {key}: {value}")
        
        elif args.action == "set":
            if not args.key or not args.value:
                print("❌ Usage: qtime config set <key> <value>")
                return
            
            self.config[args.key] = args.value
            self.save_config()
            print(f"✅ Set {args.key} = {args.value}")
        
        elif args.action == "reset":
            if os.path.exists(self.config_file):
                os.remove(self.config_file)
            self.config = self.load_config()
            print("✅ Configuration reset to defaults")
    
    def info(self, args):
        """Show QTime information"""
        print(f"""
🌌 QTime Engine v{self.version}
   Time travel visualization toolkit

📁 Output Directory: {self.config['default_output_dir']}
🌐 API Server: {self.config['api_server']}
🔌 WebSocket Server: {self.config['websocket_server']}

📚 Available Commands:
   qtime generate basic     - Generate basic timeline GIF
   qtime generate advanced  - Generate advanced timeline GIF  
   qtime generate 3d        - Generate 3D interactive timeline
   qtime generate html      - Generate HTML quantum sandbox
   qtime server api         - Start REST API server
   qtime server websocket   - Start WebSocket server
   qtime config show        - Show configuration
   qtime --help            - Show detailed help

🚀 Quick Start:
   qtime generate basic
   qtime generate html
   qtime server api

💡 Tip: Use --output to specify custom filenames
        """)

def main():
    """Main CLI entry point"""
    cli = QTimeCLI()
    
    parser = argparse.ArgumentParser(
        description="QTime - Quantum Timeline Engine CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--version', action='version', version=f'QTime {cli.version}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Generate commands
    gen_parser = subparsers.add_parser('generate', help='Generate timeline visualizations')
    gen_subparsers = gen_parser.add_subparsers(dest='gen_type', help='Generation type')
    
    basic_parser = gen_subparsers.add_parser('basic', help='Generate basic timeline')
    basic_parser.add_argument('--output', '-o', help='Output filename')
    
    advanced_parser = gen_subparsers.add_parser('advanced', help='Generate advanced timeline')
    advanced_parser.add_argument('--output', '-o', help='Output filename')
    
    td_parser = gen_subparsers.add_parser('3d', help='Generate 3D timeline')
    td_parser.add_argument('--output', '-o', help='Output filename')
    
    html_parser = gen_subparsers.add_parser('html', help='Generate HTML sandbox')
    html_parser.add_argument('--output', '-o', help='Output filename')
    
    # Server commands
    server_parser = subparsers.add_parser('server', help='Start servers')
    server_subparsers = server_parser.add_subparsers(dest='server_type', help='Server type')
    
    api_parser = server_subparsers.add_parser('api', help='Start API server')
    api_parser.add_argument('--host', default='0.0.0.0', help='Server host')
    api_parser.add_argument('--port', type=int, default=5000, help='Server port')
    api_parser.add_argument('--debug', action='store_true', help='Debug mode')
    
    ws_parser = server_subparsers.add_parser('websocket', help='Start WebSocket server')
    
    # Config commands
    config_parser = subparsers.add_parser('config', help='Configuration management')
    config_subparsers = config_parser.add_subparsers(dest='action', help='Config action')
    
    config_subparsers.add_parser('show', help='Show configuration')
    
    set_parser = config_subparsers.add_parser('set', help='Set config value')
    set_parser.add_argument('key', help='Config key')
    set_parser.add_argument('value', help='Config value')
    
    config_subparsers.add_parser('reset', help='Reset configuration')
    
    # Info command
    subparsers.add_parser('info', help='Show QTime information')
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command == 'generate':
        if args.gen_type == 'basic':
            cli.generate_basic(args)
        elif args.gen_type == 'advanced':
            cli.generate_advanced(args)
        elif args.gen_type == '3d':
            cli.generate_3d(args)
        elif args.gen_type == 'html':
            cli.generate_html(args)
        else:
            gen_parser.print_help()
    
    elif args.command == 'server':
        if args.server_type == 'api':
            cli.start_server(args)
        elif args.server_type == 'websocket':
            cli.start_websocket(args)
        else:
            server_parser.print_help()
    
    elif args.command == 'config':
        cli.config_command(args)
    
    elif args.command == 'info':
        cli.info(args)
    
    else:
        if len(sys.argv) == 1:
            cli.info(args)
        else:
            parser.print_help()

if __name__ == '__main__':
    main()
