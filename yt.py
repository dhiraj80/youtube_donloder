from tkinter import *
from tkinter import ttk
from pytube import *
import urllib.request
from PIL import Image,ImageTk,ImageSequence
import time

#================ play gif =====================
def playing_gif():
    try:
        gif_path = Image.open("D:\\all icons\\yt1.gif")
        for img in ImageSequence.Iterator(gif_path):
            img = gif_path.resize((270,270),Image.ANTIALIAS)
            gif_img = ImageTk.PhotoImage(img)
            gif_lbl.config(image=gif_img)
            root.update()
            time.sleep(0.05)
        root.after(15,playing_gif)
    except :
        return "None"

root = Tk()
root.geometry("1400x1000+0+0")
root.title('YouTube Video Donwloder')
root.config(bg="#ff0077")

#=============== Images ====================

vid_img = PhotoImage(file="D:/all icons/video3.png")
aud_img = PhotoImage(file="D:/all icons/audio.png")

#========================= Home Tab ==================================
def hometab():
    Label(root,text="Welcome",fg='green',font=("times new roman","140","bold"),bg="#ff0077").pack(fill="x",pady=50)

    Label(root,text="Downlode All Youtube Video And\n Playlist With Multipal Strems And Quilty",fg='yellow',font=("times new roman","30","bold"),bg="#ff0077",justify=CENTER).pack(fill="x")

    start_btn = Button(root,text='Start',fg="red",cursor='hand2',font=("times new roman","50","bold"),width=15,bd=5,relief=RAISED)
    start_btn.pack(pady=160)

#======================== Video Function =========================
sel_var = IntVar()
sel_var.set(1)
vid_var = StringVar()
aud_var = StringVar()
vid_link_var = StringVar()

def serch():
    try:
        youtube_ser = YouTube(vid_link_var.get())
        thumb_img()
    except:
        pass
    if sel_var.get() == 1:
        aud_lbl.config(state=DISABLED)
        videos = youtube_ser.streams.filter(res=vid_var.get())
        videos.first().download()

    if sel_var.get() == 2:
        vid_lbl.config(state=DISABLED)
        videos = youtube_ser.streams.filter(res="360p")
        print(videos)


def video_dowl():
    pass



#================== Thumbainal image =========================
def thumb_img():
    global th_img
    youtube_ser = YouTube(vid_link_var.get())
    urllib.request.urlretrieve(youtube_ser.thumbnail_url,"th_img.png")
    img_path = Image.open("th_img.png")
    img_path = img_path.resize((950,600),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image=img_path)
    th_img.config(image=img)

title = Label(root,text="Youtube Video Downloder",fg='white',bg='crimson',font=("times new roman","66","bold"))
title.pack(side=TOP,anchor=N,fill=X)

donl_frm = Frame(root,bg="#ffd700")
donl_frm.place(x=270,y=105,width=1200,height=900)

stauts_bar = Frame(root,bg="#1AB1C4",height=25)
stauts_bar.pack(side=BOTTOM,fill=X)

dtl_frm = Frame(root,bg="#1AB1C4",width=310,relief=RIDGE,bd=7)
dtl_frm.pack(side=LEFT,anchor=NW,fill=Y)
#=== Gif Frame ===
gif_frm = Frame(dtl_frm,bg="red")
gif_frm.place(x=19,y=30,width=270,height=200)
gif_lbl = Label(gif_frm,bd=5,relief=GROOVE)
gif_lbl.pack()
#===== Button ======
# h_btn = Button(dtl_frm,text='Home',fg="red",cursor='hand2',font=("times new roman","20","bold"),width=15,bd=5,relief=RAISED,activebackground='gray',activeforeground="red",command=hometab)
# h_btn.place(x=25,y=280)
v_btn = Button(dtl_frm,text='Video',fg="red",cursor='hand2',font=("times new roman","20","bold"),width=15,bd=5,relief=RAISED,activebackground='gray',activeforeground="red",)
v_btn.place(x=25,y=380)
pl_btn = Button(dtl_frm,text='Playlist',fg="red",cursor='hand2',font=("times new roman","20","bold"),width=15,bd=5,relief=RAISED,activebackground='gray',activeforeground="red")
pl_btn.place(x=25,y=480)
ab_btn = Button(dtl_frm,text='About',fg="red",cursor='hand2',font=("times new roman","20","bold"),width=15,bd=5,relief=RAISED,activebackground='gray',activeforeground="red")
ab_btn.place(x=25,y=580)

#========================= video Tab ================================

Label(donl_frm,text=f"Get Link",fg='red',font=("arial","20","bold"),bg="#ffd700").place(x=80,y=40)

get_link = Entry(donl_frm,width=55,font=("arial","15","bold"),textvariable=vid_link_var)
get_link.place(x=220,y=40)

serch_btn = Button(donl_frm,text='Search',fg="red",cursor='hand2',font=("times new roman","18","bold"),width=10,bd=5,relief=RAISED,command=serch)
serch_btn.place(x=880,y=30)

sel_qty = Radiobutton(donl_frm,variable=sel_var,bg="#ffd700",text="     ",value=1)
sel_qty.place(x=240,y=118)
sel_qty = Radiobutton(donl_frm,variable=sel_var,bg="#ffd700",text="     ",value=2)
sel_qty.place(x=600,y=118)

Label(donl_frm,image=vid_img,compound=LEFT,padx=7,text=f"Video Qulity",fg='white',font=("arial","16","bold"),bg="#ffd700",justify=CENTER).place(x=260,y=110)
vid_lbl = ttk.Combobox(donl_frm,width=20,font=("times new roman","15","bold"),textvariable=vid_var,justify=CENTER,)
vid_lbl["values"]= ("144p","240p","360p","480p","720p HD","1080p FHD")
vid_lbl.place(x=235,y=165)
vid_lbl.set("Select Video Quilty")

Label(donl_frm,image=aud_img,compound=LEFT,padx=7,text=f"Audio Qulity",fg='white',font=("arial","16","bold"),bg="#ffd700",justify=CENTER).place(x=620,y=110)
aud_lbl = ttk.Combobox(donl_frm,width=20,font=("times new roman","15","bold"),textvariable=aud_var,justify=CENTER)
aud_lbl["values"]= ("144p","240p","360p","480p")
aud_lbl.place(x=595,y=165)
aud_lbl.set("Select Audio Quilty")

down_btn = Button(donl_frm,text='Download',fg="red",cursor='hand2',font=("times new roman","18","bold"),width=10,bd=5,relief=RAISED)
down_btn.place(x=880,y=130)

#====Thembail====
#Label(donl_frm,text=f">> Video Title: ",fg='white',font=("times new roman","16","bold"),bg="#ffd700",justify=CENTER).place(x=60,y=780)

th_frm = Frame(donl_frm,bg="white")
th_frm.place(x=120,y=230,width=930,height=570)
th_img = Label(th_frm,bd=0)
th_img.pack()
#========================= video Tab Close ================================

thumb_img()
#hometab()
#playing_gif()
root.mainloop()







    #videos = youtube_ser.streams.filter(res=vid_var.get())   
    #vid = list(videos.get_by_resolution("360p"))
    #youtube_ser.streams.filter(res="360p").first().download()
    # for i in videos:
    #     print(i)
    #print(youtube_ser.video_id)