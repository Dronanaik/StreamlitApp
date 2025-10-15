#!/usr/bin/env python3
"""
YouTube Video Downloader Launcher
Simple script to run the Streamlit app with proper configuration
"""

import subprocess
import sys
import os

def main():
    """Launch the YouTube Video Downloader app"""
    print("🎥 Starting YouTube Video Downloader...")
    print("📱 Opening in your default browser...")
    print("🔗 URL: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        # Run streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.headless", "false",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("💡 Make sure you have installed the requirements: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
