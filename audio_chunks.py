
##############################################
### DEFINE VARIABLES
### 
###############################################

filepath = "..." #Change "..." for your directory and the name of the clean dataset
audiopath = "..." #change "..." for your audio directory 

################################################
import os
import glob
import pandas as pd
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
################################################   
# Get Audio Chunks                                                                         

df = pd.read_csv(filepath)

for i in range(len(df)):
       file = glob.glob(audiopath + f"""/{df['file'][i]}""", recursive=True)  
       start=((pd.to_numeric(df['mark_start'][i]))/1000) 
       end=((pd.to_numeric(df['mark_end'][i]))-(pd.to_numeric(df['mark_start'][i])))/1000 
       os.system(f"""sox {file[0]} {file[0][:-4]}_{start}_{end}.wav trim {start} {end}""")

       
