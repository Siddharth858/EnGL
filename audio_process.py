#!/usr/bin/env python
#WARNING : First press finish button then cut program
import main_lis_gui
import json
import pyaudio
from os.path import join, dirname
from pocketsphinx import LiveSpeech, AudioFile
import wave
import threading                   # multi threading
import os                          # for listing directories
import sys                         # system calls
import time
#k is used as global variable, ONE_STEPS_RECORD_TIME
class sound_object(object):#create only one instance
    def __init__(self,audio_file_to_be_read,file_number=None):
        with open('./file_to_read.json',"w+") as f:
            ter = {'k0':0,'lesson_number':file_number}
            json.dump(ter,f)
        self.final_script_temp = open('./output/file1.dat','w')
        self.final_script_temp.write(" ")
        self.final_script_temp.close()
        self.fi = open('./transcript/lesson_%d.txt'%file_number)
        self.words =self.fi.read().split(' ')
        #print lines
        self.word_counter = 0
        self.destroy_transcript_thread = 0#if this is one transcript will not work
        self.counter_play_button = 0
        self.k0 = 0         #MAke sure value of k1 = 1 for playing
        self.value_play_button = 0          #One represent audio will be played and run 0 represent stop has change function 
        self.k1 = 0                         #will not play initially
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100   #Fixed need not to be changed
        self.CHUNK = 1024   #Fixed value
        self.TOTAL_TIME_OF_AUDIO = 60        #IN SECOND - WAVE OUTPUT FILE
        self.SPEAK_TIME = 10
        self.RECORD_TIME = 10
        #global ONE_STEPS_RECORD_TIME
        self.ONE_STEPS_RECORD_TIME = 5       #Number of attempts
        #NUMBER_RECORD_LOOP = 2
        self.NUMBER_RECORD_LOOP = self.SPEAK_TIME/self.ONE_STEPS_RECORD_TIME
        #self.store_file = './result/flag1.json'
        self.lesson_hear = audio_file_to_be_read
        self.wf = wave.open(self.lesson_hear,'rb')
        self.p = pyaudio.PyAudio()
        self.stream_listen = self.p.open(format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(), rate = self.wf.getframerate(),output = True)
        self.data_listen = self.wf.readframes(self.CHUNK)
        self.t0 = time.time()
    def running_function(self):
        self.t0 = time.time()
        while self.data_listen != '':
            #time.sleep(1)
            if self.value_play_button == 0:
                time.sleep(1)
            elif self.value_play_button == 1:
                self.t1 = time.time()
                self.stream_listen.write(self.data_listen)
                self.data_listen = self.wf.readframes(self.CHUNK)
                if(int(self.t1 - self.t0)%self.RECORD_TIME+1 == self.RECORD_TIME):
                    #for self.k in range(0,self.NUMBER_RECORD_LOOP):
                    self.record_audi()
                    #self.get_transcript()
                    self.t1 = time.time()
                    self.t0 = self.t1
            elif self.value_play_button == 2:             #Creates exit situtation
                print "Thread destroyed"
                sys.exit()
            if not self.data_listen != '':
                self.value_play_button = 2
                print "Exited : : "
        self.stream_listen.close()
        self.p.terminate()
    def record_audi(self):
        self.pyaudio_init = pyaudio.PyAudio()#For storing audio file
        self.stream = self.pyaudio_init.open(format=pyaudio.paInt16, channels = 1,rate=44100,input=True, frames_per_buffer = self.CHUNK)
        self.frames = []
        
        for i in range(0,int(self.RATE / self.CHUNK * self.ONE_STEPS_RECORD_TIME)):
            self.data = self.stream.read(self.CHUNK)
            self.frames.append(self.data)
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio_init.terminate()
        #print "Sending"
        self.waveFile = wave.open("./recordings/file%d.wav" %self.k1,'wb')
        #self.waveFile = wave.open("./test1.wav" %self.k1,'wb')
        self.waveFile.setnchannels(self.CHANNELS)
        self.waveFile.setsampwidth(self.pyaudio_init.get_sample_size(self.FORMAT))
        self.waveFile.setframerate(self.RATE)
        self.waveFile.writeframes(b''.join(self.frames))
        self.waveFile.close()
        self.k1 = self.k1 + 1
        threading.Thread(target=self.get_transcript).start()
        return
    def get_transcript(self):
        #global k0       #k0 is global and defined later in main code 
        #k0 = 0
        if self.destroy_transcript_thread == 1:
            sys.exit()
        os.system('python pocket_audio_process.py')
        with open('./file_to_read.json','r') as f:
            self.temp_dic = json.load(f)
            self.previousK0 = self.temp_dic['k0']
            self.temp_dic['k0'] = self.previousK0 + 1
            #json.dump(temp_dic,f)
        with open('./file_to_read.json','w+') as f:
            json.dump(self.temp_dic,f)
        with open('./output/file1.json','r') as f:
            self.phrase_temp = json.load(f)
        main_lis_gui.write_text_outer(self.phrase_temp,'bold_only')
        for j in range(7):
            main_lis_gui.write_text_outer_3(self.words[self.word_counter],'bold_only')
            self.word_counter = self.word_counter + 1
        #main_lis_gui.write_text_outer(phrase)
        
        self.k0 = self.k0 + 1
        
        print "hello"
        return
    def exit_sound_object(self):
        sys.exit()  #Exit the thread::::
    def button_play_change_value(self,valuein):
        self.value_play_button = valuein
        #if self.counter_play_button == 0:
        #    #Runs only once to initialize function
        #    self.running_function()
        #    self.counter_play_button = self.counter_play_button + 1
        #print valuein
        #print "I am called"