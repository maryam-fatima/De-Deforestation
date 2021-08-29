from random import seed
from random import random
import pyaudio
#import pylab
import datetime
#
import yagmail
import  pytz

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
import sklearn
import mysql.connector

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from pixel_ring import pixel_ring
from gpiozero import LED

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
RECORD_SECONDS = 5
THRESHOLD = 2

# Setup SQL Connection
conn = mysql.connector.connect(host="35.247.164.239",user="deforest",passwd="c3@d3mp0",db="deforest")
cur = conn.cursor()
sql = "INSERT INTO `NODE03` (`timestamp`, `detections`, `alert`) VALUES (%s, %s, %s)"
#  it is node 03 in abv line. it should be node 01


# Setup Stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=6,
                frames_per_buffer=CHUNK)


# Handle Ctrl+C to gracefully exit the software i.e. close all streams and cursors
def sigint_handler(sig, frame):
    # Graceful Exit :)
    print("\nExiting gracefully....\nStopping stream and closing SQL connection...\n")
    stream.stop_stream()
    stream.close()
    p.terminate()
    cur.close()
    conn.close()
    print("Done!\n")
    sys.exit(0)

# Vars
file = []
a = []
signal.signal(signal.SIGINT, sigint_handler)

# Turn on LED Indicators
power = LED(5)
power.on()
pixel_ring.set_brightness(20)
pixel_ring.change_pattern('echo')
pixel_ring.wakeup()

print("Node 1 : 172.29.200.231" + bcolors.OKGREEN + "  [ONLINE]  " + bcolors.ENDC)

# Do it again and again
chainsaw = 0
axe = 0
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nREAL-TIME DEFORESTATION DETECTION USING AI\n\n\n\n\n\n\n\n\n\n\n\n\n")

while(1):
    ts = time.time()
    #timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #timeo = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    #
    dtobj1 = datetime.datetime.utcnow()
    dtobj3 = dtobj1.replace(tzinfo = pytz.UTC)
    dtobj_Islamabad =  dtobj3.astimezone(pytz.timezone("Asia/Karachi"))
    timestamp = dtobj_Islamabad.strftime('%Y-%m-%d %H:%M:%S')


    print("\n"+ bcolors.OKBLUE + timestamp + bcolors.ENDC)
    seed(ts)
    wvoutput = str(int(random()*10000)) + ".wav"
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK,exception_on_overflow = False)
        frames.append(data)
    wf = wave.open(wvoutput, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    a = aT.file_classification(wvoutput, "svmSMtemp","svm")    
    if a[1][0]==max(a[1]):
        chainsaw = chainsaw + 1
        axe = 0
    elif a[1][1]==max(a[1]):
        axe = axe + 1
        chainsaw = 0
    else:
        chainsaw = 0
        axe = 0
    if (chainsaw > 0 and chainsaw % THRESHOLD == 0):
        print(bcolors.FAIL + "Woodcutting sound detected!\n         " + bcolors.ENDC)
        val = (timestamp, "Chainsaw", "True")
        cur.execute(sql, val)
        cur.execute('COMMIT')

	#
        yag = yagmail.SMTP(user='zabit.seecs@gmail.com',password='Stg2006usman')
        contents = ["ALERT: Woodcutting sound detected at Node 1"]
        yag.send('drusmanzabit@gmail.com','ALERT: Woodcutting sound detected', contents)

    elif (axe > 0 and axe % THRESHOLD == 0):
        print(bcolors.FAIL + "Woodcutting sound detected!\n              " + bcolors.ENDC)
        val = (timestamp, "Axe", "True")
        cur.execute(sql, val)
        cur.execute('COMMIT')
    else:
        print(bcolors.WARNING + "Analyzing Latest Sound Samples \n" + bcolors.ENDC)
    if (chainsaw >= THRESHOLD or axe >= THRESHOLD):
        pixel_ring.think()
    else:
        pixel_ring.wakeup()
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    os.remove(wvoutput)

