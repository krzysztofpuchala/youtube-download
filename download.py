import os
import sys
import subprocess

def download_audio(youtube_url, output_path="downloads"):
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, "%(title)s.%(ext)s")

    try:
        # Pobieranie samego audio w formacie mp3 (obsługuje playlisty i pojedyncze filmy)
        subprocess.run([
            "yt-dlp", "-x", "--audio-format", "mp3",
            "--ffmpeg-location", "/opt/homebrew/bin/ffmpeg",
            "-o", output_file, youtube_url
        ], check=True)
        print(f"Pobrano plik(i) do {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Użycie: python script.py <URL YouTube lub URL playlisty>")
    else:
        download_audio(sys.argv[1])
