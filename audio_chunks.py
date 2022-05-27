import os
import glob
import pandas as pd
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
# files                                                                         

df = pd.read_csv("C:/Users/Monica/Desktop/.../df_clean.csv") #Change "..." for your directory and the name of the clean dataset

for i in range(len(df)):
       file = glob.glob(f"""C:/Users/Monica/Desktop/.../{df['file'][i]}""", recursive=True) #change "..." for your audio directory 
       start=((pd.to_numeric(df['mark_start'][i]))/1000)
       end=((pd.to_numeric(df['mark_end'][i]))-(pd.to_numeric(df['mark_start'][i])))/1000
       os.system(f"""sox {file[0]} {file[0][:-4]}_{start}_{end}.wav trim {start} {end}""")
      

