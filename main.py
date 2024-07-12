from pytube import YouTube
link=input("enter youtube link: ")
print("downloading....")
yt = YouTube(link)
yt.streams.get_highest_resolution().download()
print("Video downloaded successfully")
