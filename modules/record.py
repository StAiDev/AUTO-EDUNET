import subprocess
import time

proc = subprocess.Popen(['ffmpeg', '-f', 'gdigrab', '-framerate', '15', '-offset_x', '0', '-offset_y', '0', '-video_size', '1920x1080', '-i', 'desktop', '-c:v', 'libx264', '-vprofile', 'baseline', '-g', '15', '-crf', '1', '-pix_fmt', 'yuv420p', '-threads', '4', 'output.mp4'])
# Start selenium code...
time.sleep(10)
proc.kill()