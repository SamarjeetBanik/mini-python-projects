from tkinter import *
from pytube import YouTube

base = Tk()
base.geometry("500x300")
base.resizable(0, 0)
base.title("YT Video Downloader")

Label(base, text = "Youtube Video Downloader", font = "arial 20 bold").pack()

link = StringVar()

Label(base, text = "Paste Link Here:", font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(base, width = 70, textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(base, text = "DOWNLOADED", font = "arial 15").place(x = 180 , y = 210)  

Button(base, text = "DOWNLOAD", font = "arial 15 bold", bg = "pale violet red", padx = 2, command = Downloader).place(x = 180, y = 150)

base.mainloop()