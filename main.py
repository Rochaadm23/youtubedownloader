from tkinter import *
from pytube import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Youtube video downloader @main.py_')

Label(root,text='youtube video Downloader', font='arial 28 bold').pack()
Label(root,text='@main.py', font='arial 15 bold').pack()

link = StringVar()
Label(root, text=' Paste Link Here:', font='arial 15 bold').place(x=160, y=70)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=110)

# Função que realiza o download
def Downloader():

    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Baixado', font='arial 15').place(x=180, y=210)


Button(root, text='Download', font='arila 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()
