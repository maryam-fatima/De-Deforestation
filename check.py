from random import seed
from random import random
import pyaudio
import wave
#import pylab
import datetime
#
#import yagmail
#import  pytz

import time
import sys
import os
import signal
#import numpy as np
#import matplotlib as plt
#from pyAudioAnalysis.pyAudioAnalysis import audioTrainTest as aT
from random import seed
from random import random
import pyaudio
import wave

#import pylab
import datetime
#
#import yagmail
#import  pytz

import time
import sys
import os
import signal
#import numpy as np
#import matplotlib as plt
#from pyAudioAnalysis.pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioTrainTest as aT
#

import wave
#import sklearn
#import mysql.connector

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#from pixel_ring import pixel_ring
#from gpiozero import LED

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
RECORD_SECONDS = 5
THRESHOLD = 2

# Setup SQL Connection
#conn = mysql.connector.connect(host="35.247.164.239",user="deforest",passwd="c3@d3mp0",db="deforest")
#cur = conn.cursor()
#sql = "INSERT INTO `NODE03` (`timestamp`, `detections`, `alert`) VALUES (%s, %s, %s)"
#  it is node 03 in abv line. it should be node 01

# Handle Ctrl+C to gracefully exit the software i.e. close all streams and cursors
def sigint_handler(sig, frame):
    # Graceful Exit :)
    print("\nExiting gracefully....\nStopping stream and closing SQL connection...\n")
    stream.stop_stream()
    stream.close()
    p.terminate()
    #cur.close()
    #conn.close()
    print("Done!\n")
    sys.exit(0)

# Vars
file = []
a = []

# Turn on LED Indicators
# Do it again and again
chainsaw = 0
axe = 0
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nREAL-TIME DEFORESTATION DETECTION USING AI\n\n\n\n\n\n\n\n\n\n\n\n\n")

wvoutput = '5761.wav'
f = wave.open(wvoutput, 'r')

c, a, a_nam = aT.file_classification(wvoutput, "svmSMtemp","svm")   

for i in range(len(a_nam)):
    print(f'P({a_nam[i]}={a[i]})')
print()

if a[0]==max(a):
    chainsaw = chainsaw + 1
    axe = 0
elif a[1]==max(a):
    axe = axe + 1
    chainsaw = 0
else:
    chainsaw = 0
    axe = 0
    
if (chainsaw > 0):
    print(bcolors.FAIL + "Woodcutting sound detected!\n         " + bcolors.ENDC)  
elif (axe > 0):
    print(bcolors.FAIL + "Woodcutting sound detected!\n              " + bcolors.ENDC)
else:
    print(bcolors.WARNING + "Analyzing Latest Sound Samples \n" + bcolors.ENDC)
