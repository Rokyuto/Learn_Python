import pytube
import os

save_path = ""
video = ""

# Function to Choose Save Location/Directory for the YouTue Content
def f_chooseSavePath(path_to_save):
    global save_path
    save_path = path_to_save
    print(save_path)
    return save_path

# Function to Download the YouTue Content
def f_DownloadContent(link,content_type):
    global video # Initialize YouTube Video Variable
    try:
        video = pytube.YouTube(link) # Get the YouTube video from the YouTube URL
        # Check the Chosen video type - mp3 or mp4
        if content_type == "mp4": # If mp4
            video = video.streams.get_highest_resolution() # Get Highest Video Resolution
            video.download(output_path=save_path) # Download the Video in mp4 format
        elif content_type == "mp3": # If mp3
            audio=video.streams.filter(only_audio=True).first() # Extract the Audio from the Video
            audio_file = audio.download(output_path=save_path) # Download the Audio
            #save the file
            base,extros = os.path.splitext(audio_file) # Split the audio file name to Title and Format
            new_file_name = base+'.mp3' # Change the audio file format to .mp3
            os.rename(audio_file,new_file_name) # Rename the audio file with the new name (new_file_name)
    except:
        pass
      
# Test Functions  
# f_chooseSavePath(temp)
# f_DownloadContent(temp_link,temp_video_type)
