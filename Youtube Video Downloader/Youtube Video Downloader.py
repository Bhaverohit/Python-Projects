from pytube import YouTube

link = "https://www.youtube.com/watch?v=4Rdslfhsdf"
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)

# Resolutions of video in all formats
resolutions = youtube_1.streams.all()

# Resolutions of video in all audio formats only
resolutions = youtube_1.streams.filter(only_audio=True)

res_list = list(enumerate(resolutions))

for i in res_list:
    print(i)


choose_res = int(input("Enter resolution : "))
resolutions[choose_res].download()
print("Video Downloaded Successfully")


# Download whole playlist
from pytube import Playlist

py = Playlist("https://www.youtube.com/playlist?list/skdufgsudfus")
print(f"Downloading : {py.title}")

for video in py.videos:
    video.streams.first().download()