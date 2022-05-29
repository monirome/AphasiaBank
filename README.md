# Preprocessing of transcripts and audios of AphasiaBank 

This repository aims to: clean and pre-process transcripts and obtain their corresponding audio chunks from ApahasiaBank. 

# Codes

This repository contains three python scripst for preprocessing and cleaning the data obtained from [AphasiaBank](https://talkbank.org.html). These codes should be run in the following order:

1) clean_transcriptions.ipynb: script for reading, cleaning and creating the dataframe used later to generate the audio slices where the patient speaks. 
2) convert_mp4_wav.py: script that converts the videos of the conversations between researcher and patient from mp4 to wav. 
3) aduio_chunks.py: script that generates the audio chunk where the patient speaks. 

# Example

We provide a test file....
