import pytube
url=input("enter link")
yt=pytube.YouTube(url)

streams=yt.streams.all()
for i in streams:
    print(i)

'''
video=yt.streams.get_by_itag(135)
video.download('C\Users\Rohit')
print("Done")
'''
