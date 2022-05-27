import os
import glob
# files                                                                         
lst = glob.glob("C:/Users/Monica/Desktop/.../Audios/*.mp4", recursive=True) #change "..." for your audio directory 
       
for file in lst:
    os.system(f"""ffmpeg -i {file} -ar 16000 -ac 1 {file[:-4]}.wav""") 
