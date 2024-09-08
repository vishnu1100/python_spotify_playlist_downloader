import subprocess

def download_spotify_playlist(playlist_url, output_directory):
    # Full path to spotdl executable
    spotdl_path = r'C:\Users\yourname\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\spotdl.exe'

    # Create the command to download the playlist
    command = [
        spotdl_path, '--playlist', playlist_url,
         '--output', f'{output_directory}/Spotify  Playlist'
    ]

    try:
        # Run the command using subprocess
        subprocess.run(command, check=True)
        print("Download completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("Error: spotdl not found. Please ensure it's installed and in your PATH.")

if __name__ == "__main__":
    link = input("Paste spotify  playlist URL link: ")
    playlist_url = link;
    output_directory = r"C:\Users\yourname\Desktop\musik"

    download_spotify_playlist(playlist_url, output_directory)
