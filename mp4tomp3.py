import os, sys, hashlib, math, subprocess


root = "C:\\Users\\felixdgaypc\\Desktop\\"

for filename in os.listdir(root):
    name = filename[:-4]
    s = filename[-4:]
    if s == '.mp4' or s == '.webm' or s == '.wav':
        subprocess.call(['ffmpeg', '-i', filename, '-ac', '1', '-acodec', 'pcm_s16le', '-ar', '11025', '-f', 'wav', '-vn', 'new'+filename+'.wav'])
