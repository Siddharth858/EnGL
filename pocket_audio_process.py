#!/usr/bin/env python
from pocketsphinx import LiveSpeech, get_model_path, get_data_path, DefaultConfig, Decoder, AudioFile
import json

with open('./file_to_read.json','r') as fo:
    temp_dic = json.load(fo)
    k0 = temp_dic['k0']
    lesson_number = temp_dic['lesson_number']

config = {
    'verbose': False,
    'audio_file': ('./recordings/file%d.wav'%k0),
    #'audio_file': ('./test1.wav'),
    'buffer_size': 1024,
    'no_search': False,
    'full_utt': False,
    #'hmm': os.path.join(model_path, 'en-us'),
    'lm': ('./imdata/lesson_%d/lesson_%d.lm'%(lesson_number,lesson_number)),
    'dict': ('./imdata/lesson_%d/lesson_%d.dic'%(lesson_number,lesson_number))
    #'lm': ('./imdata/lesson_1/lesson_1.lm'),
    #'dict': ('./imdata/lesson_1/lesson_1.dic')
    }
audio = AudioFile(**config)

final_script = open('./output/file1.dat','ab')
for phrase in audio:
    final_script.write(str(phrase))
    with open('./output/file1.json','w+') as f:
        json.dump(str(phrase),f)
    print phrase
final_script.close()