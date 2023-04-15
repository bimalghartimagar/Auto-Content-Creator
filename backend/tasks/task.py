import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
# import ffmpeg
# import os
import shutil

# audio_home = 'https://www.bensound.com/'
# audio_url = f'{audio_home}royalty-free-music/track/better-days'

# audio_res = requests.get(audio_url)

# bs = BeautifulSoup(audio_res.content, 'html.parser')
# file_url = bs.find(id='freelicense').find('a', string="Download")['href']

# with requests.get(f'{audio_home}{file_url}', stream=True) as req:
#     filename = file_url.split('/')[1]
#     with open(filename, 'wb') as f:
#         shutil.copyfileobj(req.raw, f)

# print(bs)

PEXELS_API_KEY = ''

PEXEL_BASE_URL = 'https://api.pexels.com/videos/'
PEXEL_SEARCH_API = 'search'
PEXEL_GET_VIDEO_API = 'videos/'

video_url = 'https://www.pexels.com/video/slow-motion-footage-of-rain-falling-on-the-ground-4154268/'
video_id = '4154268'
video_res = requests.get(f"{PEXEL_BASE_URL}{PEXEL_GET_VIDEO_API}{video_id}", headers={
    'Authorization': PEXELS_API_KEY
})
vid_json = video_res.json()
video_url = hd_vid[0]['link']
with requests.get(video_url, stream=True) as req:
    with open(f'pexels-{video_id}.mp4', 'wb') as f:
        shutil.copyfileobj(req.raw, f)

print(vid_json)


# pwd = os.getcwd()

# audio_path = '/backend/tmp/bensound-memories.mp3'
# video_path = '/backend/tmp/pexels-videos-1409899.mp4'

# video_stream = ffmpeg.input(f"{pwd}{video_path}")
# audio_stream = ffmpeg.input(f"{pwd}{audio_path}")

# # Process video

# # Save video
# out  = ffmpeg.output(video_stream.video, audio_stream.audio, 'out.mp4')

# # Run the ffmpeg with all the defined steps
# ffmpeg.run(out)

# print(out)


# # ffmpeg -i pexels-videos-1409899.mp4 -i bensound-memories.mp3 -c:v copy -c:a aac output.mp4

# # Loop 11 times, 11 means length of audio in minute divided by length of video
# # ffmpeg -y -stream_loop 11 -i pexels-videos-1409899.mp4 -i bensound-memories.mp3 -c:v copy -c:a aac -t 00:03:50 output.mp4

# # with duration
# ffmpeg -y -stream_loop 11 -i pexels-videos-1409899.mp4 -i bensound-memories.mp3 -c:v copy -c:a aac -t 00:03:50 output.mp4

# ffmpeg -y -stream_loop 27 -i Pexels-Videos-1620052.mp4 -i bensound-acousticbreeze.mp3 -c:v copy -c:a aac -t 00:02:37 output1.mp4


# # FINAL THAT WORKS
# ffmpeg -y -stream_loop 27 -i Pexels-Videos-1620052.mp4 -i bensound-acousticbreeze.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0  -t 00:02:37 output1.mp4
