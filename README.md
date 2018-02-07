# EnGL <sub>(Beta)</sub>

## Motivation
Listening is an important part of our communica-
tion, and I always felt there is lack of good project
to improve English efficiently and free. Hundreds
of websites of websites are today online to improve
listening skills, but the way needs to be modified,
They play a passage and ask the question at the
end. Listening skill varies from person to person.
It is examined in various examination such as GRE
and TOEFL.

## Requirements
A PC with internet connection and at least 2GB
RAM with Ubuntu installed. Other Steps are described in further sub-sections.

### Software and library requirement
#### 1) Python 2.7 or higher. In general Python comes
pre-installed with Ububtu, To verify open terminal type python. For further information
check Official website.
#### 2) [PocketSphinx 0.1.13](https://pypi.python.org/pypi/pocketsphinx) converts Speech to Text,
Run these command in terminal:
```$ sudo apt-get update
$ sudo pip install --upgrade pip setuptools wheel
$ sudo pip install --upgrade pocketsphinx
```
#### 3) [Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/) to record and play speech files 
Run these command to install:
```
$ sudo pip install pyaudio
```
If it fails try following,
```
$ sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
$ sudo apt-get install ffmpeg libav-tools
$ sudo pip install pyaudio
```
### 3 Next Step
Download folder from this [link](https://github.com/Siddharth858/EnGL).

## ScreenShots

![alt text](https://github.com/Siddharth858/EnGL/blob/master/data/openscreen.png "Opening Screen")



![alt text](https://github.com/Siddharth858/EnGL/blob/master/data/choose_lesson.png "Choose lesson")



![alt text](https://github.com/Siddharth858/EnGL/blob/master/data/main_screen.png "Main Screen")
