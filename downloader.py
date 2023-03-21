from pytube import YouTube
import os.path as path

video = YouTube('youtube_video_link')
file_path = path.join(path.realpath(path.dirname(__file__)), 'downloads/')
audio = video.streams.filter(only_audio=True).first().download(file_path, filename='aarti.mp3')
