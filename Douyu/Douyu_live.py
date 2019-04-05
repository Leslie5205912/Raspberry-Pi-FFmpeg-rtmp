import sys
import Douyu_ffmpeg

if __name__ == '__main__':
	if len(sys.argv)!=3:
		print('Usage: python3 Douyu_live.py index rtmpAddress')
		exit(1)
	index=sys.argv[1]
	index=int(index)
	rtmp_add=sys.argv[2]
	Douyu_ffmpeg.Douyu(index,rtmp_add)	


