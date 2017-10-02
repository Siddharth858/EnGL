#!/usr/bin/env python
from Tkinter import *
import audio_process			#Need to change when required
import threading
class mainGui(object,Frame):
	def __init__(self,master=None,audio_file=None,file_number=None):
		Frame.__init__(self,master)
		self.master.resizable(width = True,height = True)
		self.master.title('Welcome - EnGL')
		#self.audio_file_number = file_number
		self.frame_inner_2 = Frame(master, relief = FLAT)
		self.frame_inner_3 = Frame(master, relief = FLAT)
		self.frame_inner_4 = Frame(master, relief = FLAT)
		self.frame_inner_2.configure(bg = 'white')
		self.screen_width = master.winfo_screenwidth()
		self.screen_height = master.winfo_screenheight()
		self.frame_outer = Frame(master,width = self.screen_width,height = self.screen_height,relief = RAISED,bd = 10)
		#Warning hard coded
		global instance3
		global instance4
		instance3 = scroll_text(self.frame_inner_3)		#For the purpose of read only written
		instance4 = scroll_text(self.frame_inner_4)		#For the purpose of write
		self.instance2 = operational_box(self.frame_inner_2,audio_file,file_number)
		self.frame_inner_2.pack(side = TOP,expand = True,anchor = W,padx = 15,pady = 15,fill = BOTH)
		self.frame_inner_3.pack(side = LEFT,expand = True,pady = 10,padx = 10)
		self.frame_inner_4.pack(side = RIGHT,expand = True,pady = 10,padx = 10)
		#self.audi_file = audi_file = audio_file
		#for g in range(10):
		#	pass
		#temp3.sound_object('./file_audio/flag1.wav')
class scroll_text(object,Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.frame_outer_text = Frame(master,relief = FLAT,bd = 2)
		self.text_written = ''
		self.text = Text(self.frame_outer_text,height = 30,width = 65,bg = "mint cream",relief = FLAT,bd = 5)
		self.scroll_y_t = Scrollbar(self.frame_outer_text,command = self.text.yview)
		self.text.configure(yscrollcommand = self.scroll_y_t.set)
		self.text.tag_configure('bold_italics',font =('Verdana',14,'bold','italic'))
		self.text.tag_configure('big',font=('Verdana',24,'bold'))
		self.text.tag_configure('color', foreground = 'blue',font=('Tempus Sans ITC',14))
		self.text.tag_configure('bold_only',font =('Verdana',14,'bold'))
		self.scroll_y_t.pack(side = RIGHT,fill = Y,expand = False)
		self.frame_outer_text.config(highlightbackground='snow')
		self.text.config(highlightbackground='snow')
		self.text.pack(side = BOTTOM,expand = True,fill = BOTH)
		self.frame_outer_text.grid(row = 0, column = 0,sticky=SW)
	
	def write_text_inner(self,string_in,formating_in):
		self.text.insert(END,string_in+' ',formating_in)

def write_text_outer(string_in,formating_in):
	global instance4
	instance4.write_text_inner(string_in,formating_in)
	return
def write_text_outer_3(string_in,formating_in):
	global instance3
	instance3.write_text_inner(string_in,formating_in)
	return
	#pass

class operational_box(object,Frame):
	def __init__(self,master=None,audio_file=None,file_number=None):
		Frame.__init__(self,master)
		self.audio_file_number = file_number
		self.time_lis_delay = IntVar()
		self.time_speak_delay = IntVar()
		self.time_lis_delay.set(6)		#______Default value
		self.time_speak_delay.set(6)
		self.savo = IntVar()
		self.synco = IntVar()
		self.button_play_var = IntVar()
		self.button_start_var = IntVar()
		self.button_play_var.set(0)
		self.button_start_var.set(1)
		self.scale_listening_delay = Scale(master,orient = HORIZONTAL,
			length=250,from_= 0, to=12, tickinterval=2,command=lambda d=self.time_lis_delay.get():self.setval(d))
		self.scale_listening_delay.configure(bg = 'dark olive green',fg = 'blue4')
		self.label = Label(master,text="Delay audio play",bg = 'white',fg = 'dim gray')
		self.label.grid(row = 0,column = 2,sticky=E,padx = 2)
		self.scale_speaking_delay = Scale(master,orient=HORIZONTAL,length=250,from_=0, to = 12,tickinterval=2,
			command=lambda d=self.time_speak_delay.get():self.setval(d))
		self.scale_speaking_delay.configure(bg = 'dark olive green',fg = 'blue4')
		self.label_speak = Label(master,text="Time to speak",bg = 'white',fg = 'dim gray')
		self.label_speak.grid(row=1,column=2,sticky=W,padx = 2)
		self.scale_listening_delay.grid(row=0,column=3,sticky=E,padx = 50,pady = 25)
		self.scale_speaking_delay.grid(row=1,column=3,sticky = E,padx = 50,pady = 5)
		self.checkbutton_save_voice = Checkbutton(master,text = "Save voice",
			state = DISABLED, anchor = W, variable = self.savo,bg = 'white',highlightthickness = 0)
		self.checkbutton_sync_transcript = Checkbutton(master,text = "Syn Transcript",state = DISABLED,
			anchor = W, variable = self.synco,bg = 'white',highlightthickness = 0)
		self.checkbutton_sync_transcript.grid(row = 0,column = 1,sticky = W,padx = 25)
		self.checkbutton_save_voice.grid(row = 1,column = 1,sticky = W, padx = 25)
		self.button_start = Button(master,text = "START",height = 2,width = 10)
		self.button_play = Button(master,text = "PLAY",height = 2,width = 10,state = DISABLED)
		self.button_start.grid(row = 0,column = 0,rowspan = 1,sticky = W,padx = 5)
		self.button_play.grid(row = 1,column = 0,rowspan = 1,sticky = W,padx = 5,pady = 5)
		self.button_play.configure(bg = 'dark slate gray',fg = 'white')
		self.button_start.configure(bg = 'dark slate gray',fg = 'white')
		self.button_start.bind('<Button-1>',lambda event:(threading.Thread(target=self.button_start_action).start()))
		self.button_start.bind('<Return>',lambda event:(threading.Thread(target=self.button_start_action).start()))
		self.button_start.bind('<KP_Enter>',lambda event:(threading.Thread(target=self.button_start_action).start()))
		#self.button_start.bind('<Button-1>',lambda event:(self.button_start_action))
		#self.button_start.bind('<Return>',lambda event:(self.button_start_action))
		#self.button_start.bind('<KP_Enter>',lambda event:(self.button_start_action))
		self.audio_file = audio_file
		#global audi_file
		#self.created_object = temp3.sound_object(audio_file)
	def setval(self,d):
		d = int(d)
		self.time_lis_delay.set(d)
	def button_change(self):
		self.button_play.configure(state = NORMAL)
		if self.button_start['text'] == "START":
			self.button_start.configure(text="FINISH")
		else:
			self.button_play.configure(text = "START")
	def button_start_action(self,event=None):
		self.button_change()
		#self.created_object = temp3.sound_object(audi_file)
		self.button_start.unbind('<Button-1>')
		self.button_start.unbind('<Return>')
		self.button_start.unbind('<KP_Enter>')
		self.button_start.bind('<Button-1>',lambda event:(self.button_finish_action()))
		self.button_start.bind('<Return>',lambda event:(self.button_finish_action()))
		self.button_start.bind('<KP_Enter>',lambda event:(self.button_finish_action()))
		self.button_play.bind('<Button-1>',lambda event:(self.button_play_action()))
		self.button_play.bind('<Return>',lambda event:(self.button_play_action()))
		self.button_play.bind('<KP_Enter>',lambda event:(self.button_play_action()))
		#self.button_play.bind('<Button-1>',lambda event:(threading.Thread(target = self.button_play_action).start()))
		#self.button_play.bind('<Return>',lambda event:(self.button_play_action()))
		#self.button_play.bind('<KP_Enter>',lambda event:(self.button_play_action()))
		global created_object#problem in created object
		created_object = audio_process.sound_object(self.audio_file,self.audio_file_number)
		created_object.running_function()
	def button_finish_action(self,event=None):
		self.button_play.configure(state=DISABLED)
		#created_object.button_play_change_value(2)
		created_object.destroy_transcript_thread = 1#will destroy transcript thread
		created_object.button_play_change_value(2)
		print "Done"
	def scale_speak_time(self):
		pass
		#####sys.exit()
		#del self.created_object
		#print "hello world"
		#exit(0)
	def button_play_action(self,event=None):
		r = self.button_play_var.get()#no direct association with button
		r = not(r)
		r = int(r)
		if r == 1:
			self.button_play.configure(text="PAUSE")
		else:
			self.button_play.configure(text="PLAY")
		self.button_play_var.set(r)
		global created_object
		created_object.button_play_change_value(r)
'''
I wanted to note a point about this error 
it is due to reason object is not created and trying to access
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1540, in __call__
    return self.func(*args)
  File "/home/siddharth/EnGL/Codes/main_lis_gui.py", line 105, in <lambda>
    self.button_play.bind('<Button-1>',lambda event:(self.button_play_action()))
  File "/home/siddharth/EnGL/Codes/main_lis_gui.py", line 119, in button_play_action
    self.created_object.button_play_change_value(r)
AttributeError: 'operational_box' object has no attribute 'created_object'
./recordings/file0.wav

'''



#root = Tk()
#root.option_readfile('optionDB')#______need to change if required
#imgicon = PhotoImage(file='./data/icon.png')
#root.tk.call('wm', 'iconphoto', root._w, imgicon)
#if __name__ == "__main__":
#    #Example(root).pack(fill="both", expand=True)
#    #frm = Frame(root)
#    #log = scroll_text(frm)
#    #frm.pack()
#    #Pmw.initialise()
#    log1 = mainGui(root)
#    root.mainloop()
'''
text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 24, 'bold'))
text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
'''
