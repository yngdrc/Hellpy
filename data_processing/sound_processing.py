import numpy as np
import pyaudio
import sys
import wave
import struct
import matplotlib.pyplot as pl
import os
from image_processing import *

#ARGS-------------------------
#audio_file = wave.open(sys.argv[1], 'rb')
#image_file = getImage(sys.argv[1])
#new_file_name = sys.argv[2]
#-----------------------------

def readData( audio_path ):
    audio_file = wave.open(audio_path, 'rb')
    nframes = audio_file.getnframes()
    data = audio_file.readframes(nframes)
    return data

def createWavImage( image_file, new_file_name ):
    #data_asarray = bytearray(readData(audio_file))
    image_data = decodeImage(image_file)
    #for x in range(0,len(readData(audio_file))):
    #    data_asarray[x] = image_data[x]
    nf = wave.open(new_file_name, 'wb')

    nchannels = 2
    sampwidth = 2
    framerate = 48000
    nframe = len(image_data)
    comptype = "NONE"
    compname = "not compressed"

    nf.setparams((nchannels, sampwidth, framerate, nframe, comptype, compname))
    nf.writeframes(image_data)
    nf.close()

def createImageAudio( audio_path, new_name ):
    data = readData(audio_path)
    img = Image.frombytes('RGB', getImage('image.jpg')[0].size, data, 'raw')
    img.save(new_name+".png")
