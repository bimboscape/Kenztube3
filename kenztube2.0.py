import yt_dlp #imports yt-dlp as a module
input1 = input("Mp3, mp4, playlist (mp4), playlist (mp3), wav, flv (buggy) :  ") 
#prompts you to put in format, and whether you want to download a playlist or not
video_input = input("OWO What would you like to download? :  ") #promps you to put in your URL
sep = ("*********************************************") #seperator :3
def download_video(url, output_path='.'): #func for downloading mp4
    # Options for downloading
    ydl_opts = {
        'format': 'best',  # Download the best quality video
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with video title as filename
        'noplaylist': True,  # Download only the single video, not the entire playlist
    }
    try:
        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
def download_audio_as_mp3(url, output_path='.'): #func for downloading mp3
    # Options for downloading
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best audio quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with video title as filename
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
            'preferredcodec': 'mp3',      # Convert audio to MP3
            'preferredquality': '320',    # Set the audio quality to 320kbps for better sound
        }],
        'postprocessor_args': [
            '-ar', '44100'  # Set audio sample rate to 44.1kHz (standard for MP3s)
        ],
        'noplaylist': True,  # Download only the single video
    }
    try:
        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
def download_playlist_as_mp4(url, output_path='.'): #func for downloading mp4 as playlist
    # Define the playlist URL
    playlist_url = video_input
    # Create a dictionary to specify options
    ydl_opts = {
        'format': 'best',  # Download the best quality format
        'outtmpl': '%(title)s.%(ext)s',  # Filename template
    }
    # Initialize yt-dlp with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        ydl.download([playlist_url])
def download_playlist_as_mp3(url, output_path='.'): #func for downloading mp3 as playlist
        # Define the playlist URL
    playlist_url = video_input
    # Define options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio format
        'extractaudio': True,  # Download only audio
        'audioformat': 'mp3',  # Convert to MP3
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template
        'postprocessors': [{  # Post-processing options
            'key': 'FFmpegExtractAudio',  # Use ffmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # Set bitrate to 192 kbps
        }],
        'noplaylist': False,  # Ensure the playlist is processed
    }
    # Initialize yt-dlp with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download the playlist
        ydl.download([playlist_url])
def download_as_wav(url, output_path='.'): #func for downloading as wav
        #define audio output
    playlist_url = video_input
    #define options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best', #downloads best audio
        'extractaudio': True, #downloads only audio
        'audioformat': 'wav', #convert to wav
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', #use ffmpeg to extract audio
            'preferredcodec': 'wav', #convert to wav
            'preferredquality': '192', #sets bitrate to 192 kbps
        }],
        'noplaylist': True, #Ensure playlist is not processed
    }
    #initialize yt-dlp with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #download the audio
        ydl.download([playlist_url])
def download_playlist_as_wav(url, output_path='.'): #func for downloading wav as playlist 
        #define playlist output
    playlist_url = video_input
    #define options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best', #downloads best audio
        'extractaudio': True, #downloads only audio
        'audioformat': 'wav', #converts to wav
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', #use ffmpeg to extract audio
            'preferredcodec': 'wav', #convert to wav
            'preferredquality': '192', #sets bitrate to 192
        }],
        'noplaylist': False, #ensure playlist is processed
    }
    #initialize with yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
def download_as_flv(url, output_path='.'): #func for downloading flv file
    try:    #defile playlist output
        playlist_url = video_input
        #define options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best', #downloads best audio
            'extractaudio': False, #downloads full video
            'audioformat': 'flv', #converts to flv
            'outtmpl': '%(title)s.%(ext)s',  # Output filename template
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', #use ffmpeg to extract audio
                'preferredcodec': 'flv', #converts to flv
                'preferredquality': '192', #sets bitrate to 192
            }],
            'noplaylist': True, #ensure playlist is not processed
        }
        #initialize with yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except:
        print(sep)
        print("oof :< it appears the script can't download this.")
        print("it might be a bug, or the script simply can't convert the URL into flv")
        print("Your download might have been downloaded as something else? go check idk")
def download_playlist_as_flv(url, output_path='.'): #func for downloading flv file
    try:    #defile playlist output
        playlist_url = video_input
        #define options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best', #downloads best audio
            'extractaudio': False, #downloads full video
            'audioformat': 'flv', #converts to flv
            'outtmpl': '%(title)s.%(ext)s',  # Output filename template
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', #use ffmpeg to extract audio
                'preferredcodec': 'flv', #converts to flv
                'preferredquality': '192', #sets bitrate to 192
            }],
            'noplaylist': False, #ensure playlist is processed
        }
        #initialize with yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except:
        print(sep)
        print("oof :< it appears the script can't download this.")
        print("it might be a bug, or the script simply can't convert the URL into flv")
        print("Your download might have been downloaded as something else? go check idk")
if __name__ == "__main__":
    if input1 == "mp4": 
        download_video(video_input, '.') #mp4 
    elif input1 == 'mp3':
        download_audio_as_mp3(video_input, '.') #mp3
    elif input1 == "playlist":
        download_playlist_as_mp4(video_input, '.') #mp4 playlist
    elif input1 == "playlist_mp3":
        download_playlist_as_mp3(video_input, '.') #mp3 playlist
    elif input1 == "wav":
        download_as_wav(video_input, '.') #wav
    elif input1 == "playlist_wav":
        download_playlist_as_wav(video_input, '.') #wav playlist
    elif input1 == "flv":
        download_as_flv(video_input, '.') #flv
    elif input1 == "playlist_flv":
        download_playlist_as_flv(video_input, '.') #flv playlist
    else:
        print("Oof :< it appears that's not an option (yet)")
        print(sep)
        print("Your choices are mp3, mp4, playlist (mp4), playlist_mp3 (mp3),")
        print('wav, playlist (wav), flv')
