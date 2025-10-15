#!/usr/bin/env python3
"""
Installation script for YouTube Video Downloader
Automatically installs all required dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages from requirements.txt"""
    print("🔧 Installing YouTube Video Downloader...")
    print("-" * 50)
    
    try:
        # Check if requirements.txt exists
        if not os.path.exists("requirements.txt"):
            print("❌ requirements.txt not found!")
            return False
        
        # Install requirements
        print("📦 Installing dependencies...")
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Installation completed successfully!")
            print("\n🚀 You can now run the application with:")
            print("   python run.py")
            print("   or")
            print("   streamlit run app.py")
            return True
        else:
            print("❌ Installation failed!")
            print("Error output:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error during installation: {e}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python {version.major}.{version.minor} is not supported!")
        print("💡 Please install Python 3.7 or higher")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True

def main():
    """Main installation function"""
    print("🎥 YouTube Video Downloader - Installation")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if install_requirements():
        print("\n🎉 Installation completed!")
        print("📖 Check README.md for usage instructions")
    else:
        print("\n💥 Installation failed!")
        print("🔧 Try installing manually: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
