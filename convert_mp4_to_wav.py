
##############################################
### Define Variables
### 
###############################################

audiopath = "..." #change "..." for your audio directory 

################################################
### Library

import os
import glob
################################################   
# Convert mp4 format to wav format 

lst = glob.glob("audiopath/*.mp4", recursive=True) 
       
for file in lst:
    os.system(f"""ffmpeg -i {file} -ar 16000 -ac 1 {file[:-4]}.wav""") 
