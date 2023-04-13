# Import moviepy
from moviepy.editor import *

# Load the video and the audio (Video = video.mp4, Audio = audio.mp3)
video = VideoFileClip(VIDEO_FILE)
audio = AudioFileClip(AUDIO_FILE)

# Remove the original audio from the video
video = video.without_audio()

# Add the new audio to the video
video = video.set_audio(audio)

# Save the output video
video.write_videofile("output.mp4")
