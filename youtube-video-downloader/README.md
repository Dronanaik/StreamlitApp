# 🎥 YouTube Video Downloader

A modern, user-friendly YouTube video downloader built with Streamlit. Download your favorite YouTube videos in various quality options with a beautiful, intuitive interface.

## ✨ Features

- **Modern UI Design**: Beautiful, responsive interface with gradient backgrounds and smooth animations
- **Multiple Quality Options**: Choose from various video qualities (2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, 144p)
- **File Size Estimation**: See estimated file sizes before downloading
- **Progress Tracking**: Real-time download progress with visual indicators
- **Custom Download Path**: Specify where you want to save your videos
- **Video Information**: View video title, duration, uploader, and view count
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **URL Validation**: Automatic validation of YouTube URLs

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd youtube-video-downloader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

## 📖 How to Use

1. **Enter YouTube URL**: Paste any YouTube video URL in the input field
2. **View Video Info**: The app will automatically fetch video information
3. **Select Quality**: Choose your preferred video quality from the dropdown
4. **Set Download Path**: Specify where you want to save the video (default: ~/Downloads)
5. **Download**: Click the "Download Video" button and wait for completion

## 🎨 UI Features

### Main Interface
- **Gradient Header**: Eye-catching header with app title and description
- **Card-based Layout**: Clean, organized content in styled cards
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### Sidebar
- **Settings Panel**: Configure download path and view app information
- **Quick Guide**: Step-by-step instructions for new users
- **Tips Section**: Helpful tips for optimal usage
- **Disclaimer**: Important legal and usage information

### Visual Elements
- **Progress Bars**: Real-time download progress visualization
- **Success Animations**: Celebration balloons on successful downloads
- **Color-coded Messages**: Different message types with appropriate styling
- **Hover Effects**: Interactive buttons with smooth animations

## 🔧 Technical Details

### Dependencies
- **Streamlit**: Web framework for creating the user interface
- **yt-dlp**: YouTube video downloader (fork of youtube-dl)
- **pathlib2**: Enhanced path handling utilities

### Key Functions
- `validate_youtube_url()`: Validates YouTube URLs using regex
- `get_video_info()`: Fetches video metadata without downloading
- `get_available_qualities()`: Extracts available video formats
- `download_video()`: Handles the actual video download process
- `format_file_size()`: Converts bytes to human-readable format

## 🛠️ Customization

### Changing Download Path
You can modify the default download path by editing the `download_path` variable in the sidebar section of `app.py`.

### Adding New Quality Options
The app automatically detects available qualities from the video. To modify quality preferences, edit the `quality_order` list in the `get_available_qualities()` function.

### Styling
The app uses custom CSS for styling. You can modify the appearance by editing the CSS in the `st.markdown()` section at the beginning of the `main()` function.

## ⚠️ Important Notes

### Legal Disclaimer
- This tool is for personal use only
- Please respect copyright laws and YouTube's Terms of Service
- Only download videos you have permission to download
- Be aware of your local laws regarding video downloading

### System Requirements
- **Internet Connection**: Required for downloading videos
- **Storage Space**: Ensure sufficient disk space for video files
- **Python Environment**: Python 3.7+ with pip

### Troubleshooting

#### Common Issues
1. **"No video formats available"**: The video might be private, age-restricted, or region-blocked
2. **Download fails**: Check your internet connection and try again
3. **Permission denied**: Ensure the download path is writable
4. **yt-dlp errors**: Update yt-dlp to the latest version

#### Solutions
```bash
# Update yt-dlp
pip install --upgrade yt-dlp

# Check Python version
python --version

# Verify installation
pip list | grep streamlit
pip list | grep yt-dlp
```

## 🔄 Updates

To update the application:
1. Pull the latest changes from the repository
2. Update dependencies: `pip install --upgrade -r requirements.txt`
3. Restart the Streamlit application

## 📝 License

This project is for educational purposes. Please use responsibly and in accordance with YouTube's Terms of Service and applicable copyright laws.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📞 Support

If you encounter any issues or have questions, please check the troubleshooting section above or create an issue in the repository.

---

**Enjoy downloading your favorite YouTube videos! 🎉**
