
import os
import glob
import subprocess
import mimetypes
from flask import Flask, render_template, send_from_directory, jsonify, request, Response, send_file

app = Flask(__name__)

MEDIA_FOLDER = os.path.dirname(os.path.abspath(__file__))
THUMBNAIL_FOLDER = os.path.join(MEDIA_FOLDER, 'thumbnails')
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm']

def create_thumbnail(video_path, thumbnail_path):
    try:
        subprocess.run([
            'ffmpeg',
            '-i', video_path,
            '-ss', '00:00:01',
            '-vframes', '1',
            '-vf', 'scale=240:-1',
            '-q:v', '8',
            thumbnail_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error creating thumbnail for {video_path}: {e}")

def get_media_files():
    media_files_data = []
    all_files = []
    for ext in SUPPORTED_EXTENSIONS:
        all_files.extend(glob.glob(os.path.join(MEDIA_FOLDER, f'*{ext}')))
    
    all_files.sort(key=os.path.getmtime, reverse=True)

    for file_path in all_files:
        filename = os.path.basename(file_path)
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in ['.mp4', '.webm']:
            thumbnail_filename = f"{filename}.jpg"
            thumbnail_path = os.path.join(THUMBNAIL_FOLDER, thumbnail_filename)
            if not os.path.exists(thumbnail_path):
                create_thumbnail(file_path, thumbnail_path)
            
            media_files_data.append({
                'filename': filename,
                'type': 'video',
                'thumbnail': thumbnail_filename
            })
        elif file_ext in ['.jpg', '.jpeg', '.png', '.gif']:
            media_files_data.append({
                'filename': filename,
                'type': 'image'
            })
            
    return media_files_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/media')
def api_media():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    media_files = get_media_files()
    
    start = (page - 1) * per_page
    end = start + per_page
    paginated_files = media_files[start:end]
    
    return jsonify({
        'media_files': paginated_files,
        'has_next': end < len(media_files)
    })




if __name__ == '__main__':
    os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)
    app.run(host='127.0.0.1', port=5001)
