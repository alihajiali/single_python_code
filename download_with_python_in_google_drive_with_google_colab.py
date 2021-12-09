# connect to google drive

from google.colab import drive
drive.mount('/content/gdrive')

#-------------------------------

### upload every file in google drive

# get info

url = input("please enter your url : ")
path = input("please enter your path \nfor example : My Drive/folder/pictures/ \n")
file_name = input("please enter your file name \nfor example : video.mp4 \n")

# upload

import requests	
r = requests.get(url, stream = True)

with open("/content/gdrive/"+path+file_name, "wb") as file:
	for block in r.iter_content(chunk_size = 1024):
		if block:
			file.write(block)

#-------------------------------

### upload youtube video in google drive

pip install pytube

# get info

url = input("please enter your url : ")
path = input("please enter your path \nfor example : My Drive/folder/pictures/ \n")

# download video from youtube

from pytube import YouTube

my_video = YouTube(url)

my_video = my_video.streams.get_highest_resolution()

my_video.download(path)
