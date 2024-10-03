import subprocess

def download_spotify_playlist(playlist_url, output_directory):
    # Full path to spotdl executable
    spotdl_path = r'C: path of \spotdl.exe'

    # Create the command to download the playlist
    command = [
        spotdl_path, '--playlist', playlist_url,
        '--output', f'{output_directory}/Spotify Playlist'
    ]

    try:
        # Run the command using subprocess
        subprocess.run(command, check=True)
        print(f"Download completed for playlist: {playlist_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading {playlist_url}: {e}")
    except FileNotFoundError:
        print("Error: spotdl not found. Please ensure it's installed and in your PATH.")

def main():
    # Ask how many playlists to download
    num_playlists = int(input("How many playlists would you like to download? "))

    # Collect playlist URLs
    playlist_urls = []
    for i in range(num_playlists):
        playlist_url = input(f"Paste Spotify playlist URL link for playlist {i + 1}: ")
        playlist_urls.append(playlist_url)

    # Get the output directory
    output_directory = r" your path to save "

    # Download all playlists after collecting URLs
    for playlist_url in playlist_urls:
        download_spotify_playlist(playlist_url, output_directory)

if __name__ == "__main__":
    main()
