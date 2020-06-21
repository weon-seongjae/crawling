import pytube
import os
import subprocess

yt = pytube.YouTube('https://www.youtube.com/watch?v=M8XUM-Z1XSw') # 다운받을 동영상 URL 지정

videos = yt.streams.all()

# print('videos ', videos)

for i in range(len(videos)):
    print(i, ' , ', videos[i])

down_dir = f'C:\youtube'

cNum = int(input('다운받을 화질은?(0~21번 입력) '))

videos[cNum].download(down_dir)

newFileName = input('변환할 mp3 파일명은? ')
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName),
])

print('동양상 다운로드 및 mp3 변환 완료')
