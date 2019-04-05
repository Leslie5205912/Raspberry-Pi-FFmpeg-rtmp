import time
import random
import os
import send_mail
def list_add(movie_set):
    global playlist
    playlist=[]
    movie_dir=open(movie_set)
    for i in movie_dir:
        i=i.strip('\n')
        playlist.append(i)
    movie_dir.close()
def ffmpeg(rtmp_add,current_play):
    os.system('ffmpeg -re -i "'+current_play+
              '" -vcodec copy -acodec aac -b:a 192k -f flv "'+
        rtmp_add+'"')

def Douyu(index,rtmp_add):
    movie_set="Douyu_playlist.txt"
    list_add(movie_set)
    nums=len(playlist)
    while True:
        current_play=playlist[index]
        index=(index+1)%nums
        print(current_play)
        print(rtmp_add)
        start_time=time.time()
        ffmpeg(rtmp_add, current_play)
        end_time=time.time()
        if(end_time-start_time<600):
            send_mail.send_mail()
            break
