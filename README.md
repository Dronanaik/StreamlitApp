# Streamlit Apps Collection

This repository contains a collection of interactive Streamlit applications demonstrating various algorithms and concepts.

## 📱 Applications

### 1. Byte Pair Encoding (BPE) Demo
**File:** `Byte-Pair-Encoding-Algo.py`

An interactive demonstration of the Byte Pair Encoding algorithm used in natural language processing and tokenization. This app shows step-by-step how BPE works by merging the most frequent character pairs in text.

**Features:**
- Interactive text input
- Configurable number of merge operations
- Step-by-step visualization of the BPE process
- Real-time vocabulary updates

### 2. Minimum Edit Distance Calculator
**File:** `minimueditdistance.py`

A calculator that computes the minimum edit distance between two strings using dynamic programming. Shows the exact operations (insert, delete, replace) needed to transform one string into another.

**Features:**
- Interactive string input
- Detailed edit operations breakdown
- Dynamic programming visualization
- Algorithm explanation

### 3. OpenRouter Chatbot
**File:** `openrouter-api-use.py`

A conversational AI chatbot powered by OpenRouter API. Designed as a Python coding assistant that provides structured code examples and explanations.

**Features:**
- Chat-based interface
- Python code generation and explanation
- Structured tutorial format
- OpenRouter API integration

### 4. YouTube Video Downloader
**Directory:** `youtube-video-downloader/`

A modern, user-friendly YouTube video downloader with a beautiful Streamlit interface. Download YouTube videos in various quality options with progress tracking and custom download paths.

**Features:**
- Modern gradient-based UI design
- Multiple quality options (2160p to 144p)
- File size estimation before download
- Real-time download progress tracking
- Custom download path selection
- Video information display (title, duration, uploader, views)
- Comprehensive error handling
- URL validation
- Audio included in all downloads

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Streamlit
- Required dependencies (see individual files for specific imports)

### Installation
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install streamlit pandas numpy openai yt-dlp pathlib2
   ```
3. For YouTube Video Downloader, also install FFmpeg:
   ```bash
   # Ubuntu/Debian
   sudo apt install ffmpeg
   
   # macOS
   brew install ffmpeg
   
   # Windows: Download from https://ffmpeg.org/download.html
   ```

### Running the Apps
Each app can be run independently using Streamlit:

```bash
# Run BPE Demo
streamlit run Byte-Pair-Encoding-Algo.py

# Run Edit Distance Calculator
streamlit run minimueditdistance.py

# Run OpenRouter Chatbot (requires API key setup)
streamlit run openrouter-api-use.py

# Run YouTube Video Downloader
cd youtube-video-downloader
streamlit run app.py
```

## 📋 Requirements

- `streamlit` - Web app framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `openai` - OpenAI API client (for OpenRouter chatbot)
- `yt-dlp` - YouTube video downloader (for YouTube downloader)
- `pathlib2` - Enhanced path handling (for YouTube downloader)
- `ffmpeg` - Audio/video processing (required for YouTube downloader)

## 🔧 Configuration

For the OpenRouter chatbot, you'll need to:
1. Get an API key from [OpenRouter](https://openrouter.ai/)
2. Replace `YOUR_API_KEY` in the code with your actual API key
3. Optionally use Streamlit secrets for secure key management

## 📚 Educational Value

These applications are designed for educational purposes and demonstrate:
- Algorithm visualization
- Interactive web app development with Streamlit
- API integration
- Dynamic programming concepts
- Natural language processing techniques
- Video processing and download management
- Modern UI design with CSS and gradients
- File system operations and path handling

## 🤝 Contributing

Feel free to contribute by:
- Adding new streamlit applications
- Improving existing algorithms
- Enhancing the user interface
- Adding documentation

## 📄 License

This project is open source and available under the MIT License.
