from pytube import YouTube
from tkinter import*
from tkinter import ttk

def baixar(Link):
	video = YouTube(Link)
	video = video.streams.get_highest_resolution()
	video.download()
	
def acao():
	Video = input1.get()
	baixar(Video)
	lb1 = Label(root,text="Download efectuado",fg="white",bg="green")
	lb1.pack(padx=10,pady=10)
	
root = Tk()

ttk.Label(root,text="Cole o seu link aqui:",font="Arial 6").pack(padx=10,pady=10)

input1 = Entry(root)
input1.pack(padx=10,pady=10)

Botao = Button(root,fg = "white",bg = "black",text="Baixar",command=acao)
Botao.pack(padx=10,pady=10)

root.mainloop()