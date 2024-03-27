"""
Author: Aadil Ali
Date: 2024-03-27
Purpose: This script is designed to download a video from a YouTube link provided by the user. 
It asks the user to input a URL, downloads the video to the current working directory,
and then opens the file location where the video was saved.
"""
import sys
import webbrowser
import os
from pytube import YouTube

print(f'Using Python at: {sys.executable}')

# Try to install pytube if not already installed
try:
    from pytube import YouTube
except ModuleNotFoundError:
    print('Pytube module not found, installing now...')
    os.system(f'{sys.executable} -m pip install pytube')
    from pytube import YouTube

# Ask the user to enter the video URL
video_link = input('Please enter the YouTube video URL: ')

# Initialize the YouTube object with the link
yt = YouTube(video_link)

# Download the first stream available for the provided video link
print(f'Downloading video from {video_link}...')
video = yt.streams.first().download()
print('Download completed!')

# Open the directory where the file is downloaded
print(f'Opening location of downloaded file: {video}')
webbrowser.open(f'file://{os.path.dirname(os.path.abspath(video))}')
