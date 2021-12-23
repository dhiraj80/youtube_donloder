from tkinter import *
import time,urllib.request
from PIL import Image,ImageTk

root = Tk()
root.geometry('1400x1000+0+0')
root.title("Youtube Video Downloder")
root.wm_iconbitmap("D:\\all icons\\Ytlogo.bmp")

#================== Function Area ===================
def slide():
    global f
    try:       
        f-=2
        if f == (-900):
            f = 1400
        sld_frm.place(x=f,y=85)
        time.sleep(0.02)
        sld_frm.after(1,slide)
    except Exception as a:
        return "None"

def download():
    pass


#============= Title =============
ic = PhotoImage(file='D:\\all icons\\video.png')
ic = ic.subsample(2,2)
Label(text='Youtube Video Downloder',image=ic,font=('impact',"49"),bg="#ff0000",fg="white",compound=LEFT,border=0,padx=60).pack(fill=X)

#=============== Search frame ================
s_frm = Frame(root)
s_frm.pack(fill=X,padx=70,pady=25)

Label(s_frm,text="VIDEO LINK",fg="black",font=('arial',"19","bold")).grid(row=0,column=0,padx=70,pady=35)

vid_link = Entry(s_frm,border=2,relief="raise",width=50,font=('arial',"18"),) 
vid_link.grid(row=0,column=1)

s_btn = Button(s_frm,text='Search',font=('arial',"18","bold"),bg="black",fg='white',width=10,cursor="hand2")
s_btn.grid(row=0,column=2,padx=40)

#==================== slider ================
f = 1400
sld_frm= Frame(root,bg="gray",width=1400,height=30)
sld_frm.place(x=f,y=60)
data = "WELCOME TO FILE SHOTING PROJECT   - DEVLOPED BY DHIRAJ ARYA"
sld_text = Label(sld_frm,text=data,bg='yellow',fg="red",font=("Arial","16"))
sld_text.pack()
slide()
#================ Seprater Add ===================

Frame(root,bg="gray",width=1250,height=2).pack(fill=X,padx=60)
#================ proparty deitels ===================

pro_frm = Frame(root)
pro_frm.pack(fill=X,padx=70)

#====== Audio proparty =======
var = IntVar()

m_icon = PhotoImage(file='D:\\all icons\\audio.png')
audio_lbl = Label(pro_frm,text="Audio",image=m_icon,compound=LEFT,fg="black",font=('arial',"16","bold"),padx=30)
audio_lbl.grid(row=0,column=2,pady=35)

audiovalue = Radiobutton(pro_frm,text="240P",variable=var,value=1,font=("Arial","17"),cursor='hand2').grid(row=1,column=
2,)
audiovalue = Radiobutton(pro_frm,text="360P",variable=var,value=2,font=("Arial","17"),cursor='hand2').grid(row=2,column=
2)
audiovalue = Radiobutton(pro_frm,text="480P",variable=var,value=3,font=("Arial","17"),cursor='hand2').grid(row=3,column=
2)
audiovalue = Radiobutton(pro_frm,text="720P",variable=var,value=4,font=("Arial","17"),cursor='hand2').grid(row=4,column=
2)
#======= video proparty =========
var2 = IntVar()

v_icon = PhotoImage(file='D:\\all icons\\video3.png')
video_lbl = Label(pro_frm,text="Video",image=v_icon,compound=LEFT,fg="black",font=('arial',"16","bold"),padx=30)
video_lbl.grid(row=5,column=2,pady=35)

videovalue = Radiobutton(pro_frm,text="240P",variable=var2,value=1,font=("Arial","17"),cursor='hand2').grid(row=6,column=
2,)
videovalue = Radiobutton(pro_frm,text="360P",variable=var2,value=2,font=("Arial","17"),cursor='hand2').grid(row=7,column=
2)
videovalue = Radiobutton(pro_frm,text="480P",variable=var2,value=3,font=("Arial","17"),cursor='hand2').grid(row=8,column=
2)
videovalue = Radiobutton(pro_frm,text="720P",variable=var2,value=4,font=("Arial","17"),cursor='hand2').grid(row=9,column=
2)
videovalue = Radiobutton(pro_frm,text="1080P",variable=var2,value=5,font=("Arial","17"),cursor='hand2').grid(row=10,column=
2)

#================ Thumbainal Area ==================

th_frm = Frame(root,bg="red")
th_frm.place(x=540,y=300)

#urllib.request.urlretrieve("limk","thum.png") 
#=====================================================================
pic = Image.open("D:\\all icons\\Youtube_icon-icons.com_66802.png")
pic = pic.resize((800,400),Image.ANTIALIAS)
img = ImageTk.PhotoImage(image=pic)

th_pic = Label(th_frm,image=img,relief="raised")
th_pic.pack(fill=BOTH,expand=FALSE)
#=====================================================================

data = "Using enclosing parentheses for continuation across multiple|| lines in context managers is now supported.This allows formatting "
data = data.replace("||","\n") 
video_title = Label(root,text=data,font=("Arial","15"),justify=CENTER)
video_title.place(x=650,y=720)

#==================== Buttom Area =======================

don_btn = Button(root,text="Download",width=15,bg="yellow",bd=2,relief=RAISED,fg="red",font=("arial","18","bold"),command=download)
don_btn.pack(side=BOTTOM,anchor=SW,padx=120,pady=60)

exit = Button(root,text="Exit",width=10,bg="yellow",bd=2,relief=RAISED,fg="red",font=("arial","18","bold"),command=root.destroy)
exit.place(x=1080,y=880)

root.mainloop()
