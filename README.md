# Raspberry-Pi-FFmpeg-rtmp
用树莓派实现24小时不间断视频直播(斗鱼、BiliBili)
斗鱼直播间号 6457580、Bilibili 21269569

# 功能
1.电影/电视剧循环播放，可指定播放  
2.推流意外终端判定，发送邮件提醒

# 存在的问题
1、会不定期的会断流，现象就是出现斗鱼/Bilibili的直播码改变了，不知道是因为树莓派端出现问题导致地址改变还是斗鱼/Bilibili自行改变  
2、树莓派会不定期卡死，我安装了watch dog也没用，猜测可能是I/O导致的(因为不推流的时候挂着好几天没卡死)，现在是买了wifi插座实现手机端控制断电重启

# 等待实现的功能
1.由于问题1的原因想实现rtmp地址的自动获取，但是尝试了两个方法都无果：一是尝试Python+selenium+webdriver打开浏览器获取，但是selenium不支持arm架构，想过用vps，但是没有gui的Centos7就是不能运行，最后作罢二是尝试用Python requests实现登录斗鱼，这个我不会  
2.FFmpeg推流携带播放列表（我想实现的是能够和obs一样的效果，观众可以点播）

# 准备
Install FFmpeg and x264 自行Google安装


# 运行方法
1.首先新建一个txt文件，将播放的视频地址一行一行粘贴进去  
2.将Douyu_live.py,Douyu_ffmpeg.py,send_mail.py,Douyu_playlist.txt放到同一个目录下，最好是~  
3.命令行执行python3 Douyu_live.py 0(指定播放视频) rtmpAddress
##### Plus:如果你想实现ssh连接Raspberry Pi并且断开ssh推流仍然运行，用screen:  
```
screen
# press enter
# 执行推流命令
ctrl+a then ctrl+d
# close ssh connection
```
