# Dot Gallery

![](https://raw.githubusercontent.com/siyonomicon/dot-gallery/refs/heads/main/images/image1.webp)
![](https://raw.githubusercontent.com/siyonomicon/dot-gallery/refs/heads/main/images/image2.webp)

This project is a simple Flask application designed to serve as a media gallery, displaying images and videos.

## Features

*   **Image Display**: View various image formats (JPG, JPEG, PNG, GIF).
*   **Video Playback**: Play video files (MP4, WebM).
*   **Automatic Thumbnail Generation**: Videos automatically get thumbnails generated using FFmpeg for quick previews.
*   **Pagination**: Media files are paginated for efficient browsing of large collections.
*   **Dynamic Media Loading**: Fetches media files dynamically via an API endpoint.

## Who is this used for?

This application is ideal for:

*   **Personal Media Collections**: Easily browse and view your personal photos and videos.
*   **Local Development**: Developers needing a simple, self-hosted solution to display media content.
*   **Small-scale Archives**: A straightforward way to organize and access a collection of visual media.

## Technical Specifications

### Python Version

This application is developed with Python 3.8+ in mind. It is recommended to use a recent version of Python 3.

### Flask Version

The application uses the Flask web framework. A compatible version would be Flask 2.x or newer.

### Dependencies

#### Python Dependencies

The following Python libraries are used:

*   **Flask**: The web framework for building the application.
    *   `os`: Standard library for interacting with the operating system.
    *   `glob`: Standard library for finding pathnames matching a specified pattern.
    *   `subprocess`: Standard library for spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.
    *   `mimetypes`: Standard library for mapping filenames to MIME types.

To install the required Python dependencies, you can use pip:

```bash
pip install Flask
```

#### External Dependencies

*   **FFmpeg**: Used for generating thumbnails from video files. FFmpeg must be installed and accessible in your system's PATH.

    You can download FFmpeg from its official website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## How to Run

1.  **Install Python dependencies**:
    ```bash
    pip install Flask
    ```
2.  **Install FFmpeg** and ensure it's in your system's PATH.
3.  **Run the application**:
    ```bash
    python app.py
    ```

The application will typically run on `http://127.0.0.1:5001`.
