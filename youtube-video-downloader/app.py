import streamlit as st
import yt_dlp
import os
import tempfile
import re
from pathlib import Path
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .download-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    
    .error-message {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    
    .info-message {
        background: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def validate_youtube_url(url):
    """Validate if the URL is a valid YouTube URL"""
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    return youtube_regex.match(url) is not None

def get_video_info(url):
    """Get video information without downloading"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as e:
        st.error(f"Error getting video info: {str(e)}")
        return None

def get_available_qualities(info):
    """Extract available video qualities with audio support"""
    qualities = []
    formats = info.get('formats', [])
    
    # Get all unique video qualities from available formats
    video_qualities = set()
    for fmt in formats:
        vcodec = fmt.get('vcodec', 'none')
        if vcodec != 'none':
            quality = fmt.get('format_note', '')
            if quality:
                video_qualities.add(quality)
    
    # Create quality options based on available video qualities
    quality_order = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']
    
    for quality in quality_order:
        if quality in video_qualities:
            # Estimate file size (we'll use a placeholder since exact size depends on format selection)
            estimated_size = estimate_file_size(quality)
            qualities.append({
                'quality': quality,
                'resolution': quality,
                'filesize': estimated_size,
                'format_id': quality,  # We'll use the quality name for format selection
                'has_audio': True,  # We'll ensure audio in download function
                'has_video': True
            })
    
    # If no standard qualities found, add a generic "Best Available" option
    if not qualities:
        qualities.append({
            'quality': 'Best Available',
            'resolution': 'Variable',
            'filesize': 0,
            'format_id': 'best',
            'has_audio': True,
            'has_video': True
        })
    
    return qualities

def estimate_file_size(quality):
    """Estimate file size based on quality (rough estimates)"""
    size_estimates = {
        '2160p': 500 * 1024 * 1024,  # ~500MB
        '1440p': 300 * 1024 * 1024,  # ~300MB
        '1080p': 200 * 1024 * 1024,  # ~200MB
        '720p': 100 * 1024 * 1024,   # ~100MB
        '480p': 50 * 1024 * 1024,    # ~50MB
        '360p': 25 * 1024 * 1024,    # ~25MB
        '240p': 15 * 1024 * 1024,    # ~15MB
        '144p': 10 * 1024 * 1024,    # ~10MB
    }
    return size_estimates.get(quality, 50 * 1024 * 1024)  # Default to 50MB

def format_file_size(size_bytes):
    """Convert bytes to human readable format"""
    if size_bytes == 0:
        return "Unknown"
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def download_video(url, quality, download_path):
    """Download video with specified quality and audio"""
    # Create a more robust format selection with fallbacks
    quality_height = quality.replace('p', '')
    
    # Try multiple format selection strategies in order of preference
    format_strategies = [
        # Strategy 1: Best video + best audio for specific quality
        f"bestvideo[height<={quality_height}]+bestaudio/best[height<={quality_height}]",
        # Strategy 2: Best video + best audio (any quality)
        "bestvideo+bestaudio/best",
        # Strategy 3: Best combined format
        "best",
        # Strategy 4: Any format with video and audio
        "best[ext=mp4]/best[ext=webm]/best",
        # Strategy 5: Most basic fallback - any available format
        "worst"
    ]
    
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'progress_hooks': [lambda d: update_progress(d)],
        'merge_output_format': 'mp4',  # Merge video and audio into mp4
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'writesubtitles': False,
        'writeautomaticsub': False,
        'ignoreerrors': False,
    }
    
    # Try each format strategy until one works
    for i, format_selector in enumerate(format_strategies):
        ydl_opts['format'] = format_selector
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # If we get here, download was successful
            if i > 0:
                st.info(f"Downloaded using fallback format strategy {i+1}")
            return True
            
        except Exception as e:
            error_msg = str(e)
            if "Requested format is not available" in error_msg:
                # Try next strategy
                continue
            else:
                # Different error, show it
                st.error(f"Download failed: {error_msg}")
                return False
    
    # If all strategies failed, show available formats for debugging
    st.error("All format selection strategies failed. The video might be unavailable or restricted.")
    
    # Show available formats for debugging
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            if formats:
                st.info("Available formats for debugging:")
                format_list = []
                for fmt in formats[:10]:  # Show first 10 formats
                    vcodec = fmt.get('vcodec', 'none')
                    acodec = fmt.get('acodec', 'none')
                    quality = fmt.get('format_note', 'Unknown')
                    format_id = fmt.get('format_id', 'Unknown')
                    format_list.append(f"ID: {format_id} | Quality: {quality} | Video: {vcodec} | Audio: {acodec}")
                
                st.text("\n".join(format_list))
    except:
        pass
    
    return False

def update_progress(d):
    """Update download progress"""
    if d['status'] == 'downloading':
        if 'total_bytes' in d:
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            st.progress(percent / 100)
        elif '_percent_str' in d:
            percent_str = d['_percent_str'].replace('%', '')
            try:
                percent = float(percent_str) / 100
                st.progress(percent)
            except:
                pass

def main():
    # Beautiful Color Grid Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 2rem;
            border: 1px solid rgba(255,255,255,0.2);
        ">
            <h1 style="
                color: white;
                font-size: 3rem;
                font-weight: bold;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                background: linear-gradient(45deg, #fff, #f0f0f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">🎥 YouTube Video Downloader</h1>
            <p style="
                color: rgba(255,255,255,0.9);
                font-size: 1.2rem;
                margin: 1rem 0 0 0;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            ">Download your favorite YouTube videos in high quality with audio</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for settings
    with st.sidebar:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        ">
            <h2 style="color: white; margin: 0;">⚙️ Settings</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Download path selection
        download_path = st.text_input(
            "📁 Download Path",
            value=os.path.expanduser("~/Downloads"),
            help="Path where videos will be downloaded"
        )
        
        # Create download directory if it doesn't exist
        if download_path and not os.path.exists(download_path):
            try:
                os.makedirs(download_path, exist_ok=True)
                st.success(f"✅ Created directory: {download_path}")
            except Exception as e:
                st.error(f"❌ Error creating directory: {str(e)}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="download-card">', unsafe_allow_html=True)
        
        # URL input
        st.subheader("🔗 Enter YouTube URL")
        url = st.text_input(
            "YouTube URL",
            placeholder="https://www.youtube.com/watch?v=...",
            help="Paste the YouTube video URL here"
        )
        
        if url:
            if validate_youtube_url(url):
                st.success("✅ Valid YouTube URL")
                
                # Get video information
                with st.spinner("Getting video information..."):
                    video_info = get_video_info(url)
                
                if video_info:
                    # Display video information
                    col_info1, col_info2 = st.columns(2)
                    
                    with col_info1:
                        st.metric("Title", video_info.get('title', 'Unknown'))
                        st.metric("Duration", f"{video_info.get('duration', 0) // 60}:{video_info.get('duration', 0) % 60:02d}")
                    
                    with col_info2:
                        st.metric("Uploader", video_info.get('uploader', 'Unknown'))
                        st.metric("Views", f"{video_info.get('view_count', 0):,}")
                    
                    # Get available qualities
                    qualities = get_available_qualities(video_info)
                    
                    if qualities:
                        st.subheader("🎯 Select Video Quality")
                        
                        # Create quality options with file size and audio info
                        quality_options = []
                        for q in qualities:
                            size_str = format_file_size(q['filesize']) if q['filesize'] else "Unknown"
                            audio_info = "🎵" if q.get('has_audio', False) else "🔇"
                            quality_options.append(f"{audio_info} {q['quality']} ({q['resolution']}) - {size_str}")
                        
                        selected_quality = st.selectbox(
                            "Choose quality:",
                            options=quality_options,
                            help="Select the desired video quality. 🎵 indicates audio included, 🔇 indicates no audio"
                        )
                        
                        if selected_quality:
                            # Extract quality from selection (remove emoji and get quality name)
                            selected_quality_name = selected_quality.split(' (')[0].replace('🎵 ', '').replace('🔇 ', '')
                            selected_format_id = next(q['format_id'] for q in qualities if q['quality'] == selected_quality_name)
                            
                            # Download button
                            if st.button("🚀 Download Video", type="primary"):
                                st.markdown("</div>", unsafe_allow_html=True)
                                
                                # Download progress
                                st.subheader("📥 Download Progress")
                                progress_bar = st.progress(0)
                                status_text = st.empty()
                                
                                status_text.text("Starting download...")
                                
                                # Start download
                                success = download_video(url, selected_format_id, download_path)
                                
                                if success:
                                    progress_bar.progress(100)
                                    status_text.text("✅ Download completed successfully!")
                                    
                                    st.markdown("""
                                    <div class="success-message">
                                        <h4>🎉 Download Complete!</h4>
                                        <p>Your video has been saved to: <strong>{}</strong></p>
                                    </div>
                                    """.format(download_path), unsafe_allow_html=True)
                                    
                                    # Show download info
                                    st.balloons()
                                else:
                                    st.markdown("""
                                    <div class="error-message">
                                        <h4>❌ Download Failed</h4>
                                        <p>Please check the URL and try again.</p>
                                    </div>
                                    """, unsafe_allow_html=True)
                    else:
                        st.warning("No video formats available for this URL")
            else:
                st.error("❌ Please enter a valid YouTube URL")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        ">
            <h3 style="color: white; margin: 0 0 1rem 0;">🚀 Ready to Download!</h3>
            <p style="color: rgba(255,255,255,0.9); margin: 0;">
                Simply paste a YouTube URL and select your preferred quality to get started.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            text-align: center;
        ">
            <h4 style="color: white; margin: 0 0 1rem 0;">🎵 Audio Included</h4>
            <p style="color: rgba(255,255,255,0.9); margin: 0;">
                All downloads include high-quality audio automatically merged with video.
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
