#!/usr/bin/env python3
"""
QTime Setup Script
Install and configure QTime engine
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    
    directories = [
        "qtime_output",
        "qtime_data",
        "qtime_exports"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"  Created: {directory}")

def setup_cli():
    """Setup CLI command"""
    print("🔧 Setting up CLI...")
    
    # Make CLI executable
    cli_file = Path(__file__).parent / "qtime_cli.py"
    if cli_file.exists():
        os.chmod(cli_file, 0o755)
        print("✅ CLI setup complete")
        print("   Usage: python qtime_cli.py --help")
        return True
    else:
        print("❌ CLI file not found")
        return False

def create_sample_config():
    """Create sample configuration"""
    print("⚙️ Creating sample configuration...")
    
    config = {
        "default_output_dir": "./qtime_output",
        "api_server": "http://localhost:5000",
        "websocket_server": "ws://localhost:8765",
        "auto_open_browser": True,
        "debug_mode": False,
        "themes": {
            "default": {
                "background": "#0b0b0e",
                "primary": "#4CAF50",
                "secondary": "#2196F3",
                "accent": "#F44336"
            }
        }
    }
    
    config_file = Path.home() / ".qtime_config.json"
    
    if not config_file.exists():
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✅ Configuration created: {config_file}")
    else:
        print("ℹ️  Configuration already exists")

def run_tests():
    """Run basic tests"""
    print("🧪 Running basic tests...")
    
    try:
        # Test imports
        import matplotlib
        import json
        import sqlite3
        print("✅ Core imports working")
        
        # Test basic timeline generation
        test_script = '''
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(2, 2))
ax.text(0.5, 0.5, 'QTime Test', ha='center', va='center')
plt.savefig('test_output.png')
plt.close()
print("Basic plot test passed")
'''
        
        exec(test_script)
        
        # Cleanup test file
        if os.path.exists('test_output.png'):
            os.remove('test_output.png')
        
        print("✅ Basic functionality tests passed")
        return True
        
    except Exception as e:
        print(f"❌ Tests failed: {e}")
        return False

def show_next_steps():
    """Show next steps after installation"""
    print("\n🎉 QTime installation complete!")
    print("\n🚀 Next Steps:")
    print("   1. Generate your first timeline:")
    print("      python qtime_cli.py generate basic")
    print("\n   2. Create interactive HTML sandbox:")
    print("      python qtime_cli.py generate html")
    print("\n   3. Start the API server:")
    print("      python qtime_cli.py server api")
    print("\n   4. View all options:")
    print("      python qtime_cli.py --help")
    print("\n📚 Documentation:")
    print("   • API: http://localhost:5000/ (when server running)")
    print("   • Examples in qtime_output/ directory")
    print("   • Configuration: ~/.qtime_config.json")
    print("\n🌌 Happy time traveling!")

def main():
    """Main setup function"""
    print("🌌 QTime Engine Setup")
    print("=" * 40)
    
    steps = [
        ("Install Dependencies", install_requirements),
        ("Create Directories", create_directories),
        ("Setup CLI", setup_cli),
        ("Create Configuration", create_sample_config),
        ("Run Tests", run_tests)
    ]
    
    success_count = 0
    
    for step_name, step_func in steps:
        print(f"\n{step_name}...")
        if step_func():
            success_count += 1
        else:
            print(f"⚠️  Warning: {step_name} had issues")
    
    print(f"\n📊 Setup Summary: {success_count}/{len(steps)} steps completed")
    
    if success_count >= len(steps) - 1:  # Allow for 1 failure
        show_next_steps()
    else:
        print("\n❌ Setup incomplete. Please check errors above.")
        print("   You may need to install dependencies manually:")
        print("   pip install matplotlib numpy pillow flask flask-cors websockets")

if __name__ == "__main__":
    main()
