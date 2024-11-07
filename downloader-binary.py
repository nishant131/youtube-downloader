from pytube import YouTube, Playlist
import os.path as path

yt_playlist = list(Playlist('https://www.youtube.com/playlist?list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk'))[38:]
for video_url in yt_playlist:
    video = YouTube(video_url)
    file_path = path.join(path.realpath(path.dirname(__file__)), 'downloads/binary-trees')
    print(video.title)
    try:
        video.streams.filter(progressive=True).order_by('resolution').last().download(file_path, filename=f'{video.title}.mp4')
    except FileNotFoundError:
        video.streams.filter(progressive=True).order_by('resolution').last().download(file_path, filename=f'{video.title[:5]}.mp4')
    print(f'Completed downloading {video.title}')
