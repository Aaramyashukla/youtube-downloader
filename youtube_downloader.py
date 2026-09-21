##------------------
# 1. Library import
##------------------
import os
import yt_dlp

##---------------
# Make folder
##---------------
os.makedirs('downloads', exist_ok=True)

##-------------
# 2. Take URL
##-------------
url=input('enter youtube video URL:')

##------------------------
# 3. Download settings
##------------------------
ydll_opts={'outtmpl':'downloads/%(title)s.%(ext)s',
           'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',# best quality with audio
           'merge_output_format': 'mp4',
           'noplaylist':True}

# outmpl-- it means save the downloaded file in the downloads folder.
# %(title)s -> title of video
# %(ext)s -> file extension


##-----------------------
# 4.  Downloaded object
##-----------------------
with yt_dlp.YoutubeDL(ydll_opts) as ydl:   ## yt-dlp initializes with our download settings.
    ydl.download([url])                   ## start a actual download operation
print('Download completed')

