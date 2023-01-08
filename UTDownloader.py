from conf import *

from pytube import YouTube

class UToT:
    def __init__(self, utLink):
        self.utLink = utLink

    def save_video(self):
        yt = YouTube(self.utLink)
        yt.streams.get_by_resolution('720p').download(filename=f'{yt.title}.mp4')
        return f'{yt.title}.mp4'

