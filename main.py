from pytube import YouTube
link = YouTube("https://www.youtube.com/watch?v=jNQXAC9IVRw")
print("*********************Video Title************************")
print(link.title)
print("********************Thumb nail Image***********************")
print(link.thumbnail_url)
print("********************Download video*************************")
video=link.streams.get_highest_resolution()
video.download()