from subprocess import call
call(['ffmpeg','-i', 'https://v.redd.it/ovmj99x4sp551/HLSPlaylist.m3u8', '-c', 'copy', '-bsf:a', 'aac_adtstoasc', 'output.mp4'], shell=False)
