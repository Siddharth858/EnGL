from Tkinter import *
import json
import base64
import tkMessageBox
import main_lis_gui         #File wrriten by me
application_name = "EnGL"
message_first_page = ("This is an application, Which focuses on listening skill, Created for Independent "
"project Fourth Semester\n - EE15BTECH11032")

class Login(object,Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.login_frame = Frame(master,width = 450,height = 200)
        self.master.title('%s - Login' % application_name)
        self.login_frame.configure(bg = 'dark slate gray')
        master.configure(bg = 'dark slate gray')
        self.login_canvas = Canvas(self.master,width = 400,height = 300,bd = 0,relief = RAISED,borderwidth=2,highlightthickness=0)
        self.login_canvas.configure(bg = 'dark violet')
        self.login_button_frame = Frame(self.master)
        self.login_button_frame.configure(bg = 'dark slate gray')
        self.label_username = Label(self.login_canvas,text = 'Username:',font = ("Arial",10,"bold"),bg = 'dark violet',fg = 'white')
        self.label_username.grid(column = 0,row = 0,sticky = W,pady = 15,padx = 10)
        vcmd = (self.register(self.validate_credential),'%P')#For validation purpose
        self.username = StringVar() 
        self.entry_username = Entry(self.login_canvas,textvariable = self.username, validate = "key",
            validatecommand = vcmd,font = ("Arial",10),justify=LEFT,relief = SUNKEN,borderwidth = 5)#__care
        self.entry_username.grid(column = 1,row = 0,sticky = W,padx = 20,pady = 20)
        self.label_password = Label(self.login_canvas,text = 'Password:', font = ("Arial",10,"bold"),bg = 'dark violet',fg = 'white')
        self.label_password.grid(column = 0,row = 1,sticky = W,pady = 15,padx = 10)
        self.password = StringVar()
        self.entry_password = Entry(self.login_canvas,textvariable = self.password,font = ("Arial",10,"bold"), validate = "key",validatecommand = vcmd,
            show = '*',relief = SUNKEN,borderwidth = 5)
        self.entry_password.grid(column = 1,row = 1,sticky = W,padx = 20,pady = 20)#__care
        self.login_button_frame.configure(bg = 'medium orchid')
        self.button_login = Button(self.login_button_frame,text='Login',font = ("Arial",10,"bold"),relief = RAISED,
            borderwidth = 2,justify = CENTER)
        self.button_login.config(height = 2,relief = RAISED)
        self.button_login.configure(bg = 'dark slate gray', fg = 'white')
        self.button_login.pack(side = TOP,fill = X,pady = 0.5)
        self.button_register = Button(self.login_button_frame,text = 'Register',font = ("Arial",10,"bold"),
            relief = RAISED,borderwidth = 2,state = NORMAL)
        self.button_register.config(height = 2)
        self.button_register.configure(bg = 'dark slate gray', fg = 'white')
        self.button_register.pack(side = TOP,fill = X,pady = 0.5)
        # Message Start
        self.message_front = Message(self.login_frame,text = message_first_page,bg = 'royalblue',fg = 'ivory',relief = GROOVE,
            borderwidth = 3)
        self.message_front.config(width = 400)
        self.message_front.pack(side = TOP,pady = 5,anchor = CENTER)
        # Message End
        self.login_button_frame.pack(side = BOTTOM,fill = X,pady = 3)
        self.login_canvas.pack(side = BOTTOM,pady = 20)
        self.login_frame.pack(side = BOTTOM)
        #Authentication
        self.button_login.bind('<Button-1>',lambda event,u = self.username,p = self.password:
            (self.login_action(self)))
        self.button_login.bind('<Return>',lambda event,u = self.username,p = self.password:
            (self.login_action(self)))
        self.button_login.bind('<KP_Enter>',lambda event,u = self.username,p = self.password:
            (self.login_action(self)))
        self.button_register.bind('<Button-1>',lambda event,u = self.username,p = self.password:
            (self.register_action(self)))
        self.button_register.bind('<Return>',lambda event,u = self.username,p = self.password:
            (self.register_action(self)))
        self.button_register.bind('<KP_Enter>',lambda event,u = self.username,p = self.password:
            (self.register_action(self)))
        self.master.resizable(width=False, height=False)#___size of window will not change
    def validate_credential(self,P):
        if len(P) <= 20:
            return True
        else:
            return False
    def login_action(self,event=None):
        self.username1 = base64.b64encode(self.username.get())
        self.password1 = base64.b64encode(self.password.get())
        with open("cauth.json","r") as f:
            self.list_dict = json.load(f)
        try:
            check_password = self.list_dict[self.username1]
            if check_password == self.password1:
                self.remove_frames()
                self.nextf = choose_lesson_page(root)  #New frame
            else:
                self.button_login.configure(relief = RAISED,bd = 2)
                tkMessageBox.showerror(title='Invalid Credential',
                    message='Incorrect Username or password')
        except KeyError:
            self.button_login.configure(relief = RAISED,bd = 2)
            tkMessageBox.showerror('Invalid Credential',
                'Incorrect Username or password')
        self.button_login.configure(relief = RAISED,bd = 2)
    def register_action(self,event=None):
        self.username2 = base64.b64encode(self.username.get())
        self.password2 = base64.b64encode(self.password.get())
        if self.username2 == '' or self.username2 == ' ' or self.password2 == '' or self.password2 == ' ':
            tkMessageBox.showinfo(title = 'Enter data',
                message = 'Enter username and password')
        else:
            with open("cauth.json","r") as f:
                self.list_dict = json.load(f)
                if self.username2 in self.list_dict:
                    tkMessageBox.showerror(title = 'Username exists',
                        message = 'Given username already exists try another')
                else:
                    with open("cauth.json","w+") as f:
                        self.list_dict[self.username2] = self.password2
                        json.dump(self.list_dict,f)
                        tkMessageBox.showinfo(title = 'Registered',message = 'You have registered successfully')
    def remove_frames(self):
        self.login_canvas.pack_forget()
        self.login_frame.pack_forget()
        self.login_button_frame.pack_forget()
        self.button_login.unbind('<Button-1>')
        self.button_login.unbind('<KP_Enter>')
        self.button_login.unbind('<Return>')
class choose_lesson_page(object,Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master.resizable(width = False,height = False)
        self.master.title("Choose Lesson")
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.frame_lesson_list = Frame(master,width = self.screen_width*0.75,height = self.screen_height*0.75,relief = FLAT,bd=0)
        self.frame_lesson_list.configure(bg = 'dark slate gray',highlightthickness = 0)
        self.canvas_lesson_page = Canvas(self.frame_lesson_list,width = '10c',height = '10c')#height and width are random
        self.canvas_lesson_page.configure(bg = 'dark slate gray',highlightthickness = 0)
        self.scroll_x = Scrollbar(self.frame_lesson_list,command=self.canvas_lesson_page.xview,orient = HORIZONTAL)
        self.scroll_y = Scrollbar(self.frame_lesson_list,command = self.canvas_lesson_page.yview,orient = VERTICAL)
        self.canvas_lesson_page.configure(xscrollcommand = self.scroll_x.set)
        self.canvas_lesson_page.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_x.configure(command = self.canvas_lesson_page.xview)
        self.scroll_y.configure(command = self.canvas_lesson_page.yview)
        self.lesson_list = self.get_listening_file()
        self.total_lessons = self.lesson_list['total_lessons']
        self.var = IntVar()
        self.radio_btn_frm = [None]*self.total_lessons 
        for i in xrange(self.total_lessons):
            self.radio_btn_frm[i] = Frame(self.canvas_lesson_page,bd = 2,relief = FLAT,bg = 'floral white')
            j = str(i+1)
            tempi = 100 - len(self.lesson_list["Lesson_%s" %j][0])
            print tempi
            tempj = " " * tempi
            radio_button = Radiobutton(self.radio_btn_frm[i],
                text = "Lesson %d   %50s (%s)%s" %(i+1,self.lesson_list["Lesson_%s" %j][0],self.lesson_list["Lesson_%s" %j][1],tempj),
                value = i+1,variable = self.var,bg = 'old lace')
            self.canvas_lesson_page.create_window(0,50*i,window = self.radio_btn_frm[i],anchor = 'nw')
            radio_button.pack(side = TOP,fill = X,expand = True)
        self.var.set(1)
        self.button_next = Button(self.frame_lesson_list,text = 'Next',relief = FLAT,bd = 2)
        self.button_next.configure(height = 2,bg = 'dark olive green',fg = 'white')
        self.canvas_lesson_page.configure(scrollregion=self.canvas_lesson_page.bbox('all'))
        self.scroll_x.pack(side = BOTTOM,fill = X,expand = False)
        self.button_next.pack(side = BOTTOM,fill = X,expand = False)
        self.canvas_lesson_page.pack(side = LEFT,expand = True,fill = BOTH)
        self.scroll_y.pack(side = RIGHT,fill = Y,expand = False)
        self.canvas_lesson_page.configure(height = self.screen_height*0.75,width = self.screen_width*0.5)
        self.canvas_lesson_page.configure(bg = 'dark slate gray')
        self.frame_lesson_list.pack(fill = BOTH,expand = True)
        self.button_next.bind('<Button-1>',lambda event:
            (self.remove_frames())) 
        self.button_next.bind('<Return>',lambda event:
            (self.remove_frames()))
        self.button_next.bind('<KP_Enter>',lambda event:
            (self.remove_frames()))
    def get_listening_file(self):
        with open("listening_files.json","r") as f:
            self.lesson_list = json.load(f)# The dictionary key are number_of_files,lesson1,lesson2 and so on
        return self.lesson_list
    def remove_frames(self,event = None):
        self.tempvar = self.var.get()
        self.button_next.pack_forget()
        self.button_next.unbind('<Button-1>')
        self.button_next.unbind('<Return>')
        self.button_next.unbind('<KP_Enter>')
        self.canvas_lesson_page.pack_forget()
        self.scroll_x.pack_forget()
        self.scroll_y.pack_forget()
        self.frame_lesson_list.pack_forget()
        self.call_main_gui = main_lis_gui.mainGui(root,'./file_audio/lesson_%d.wav'%self.tempvar,self.tempvar)#Calling next frame
root = Tk()
root.option_readfile('optionDB')#______need to change if required
root.title('EnGL - Login')
imgicon = PhotoImage(file='./data/icon.png')
root.tk.call('wm', 'iconphoto', root._w, imgicon)
if __name__ == "__main__":
    log = Login(root)
    root.mainloop()