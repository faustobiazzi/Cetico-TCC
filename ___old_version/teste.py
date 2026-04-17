from tkinter import *
from PIL import Image, ImageTk

class ScrolledCanvas(Frame):

    def __init__(self, parent=None):
         Frame.__init__(self, parent)
         self.interface = Tk()
         self.interface.title("Spectrogram Viewer")
         self.pack(expand=YES, fill=BOTH)
         self.canvas = Canvas(self, relief=SUNKEN)
         self.canvas.config(width=400, height=200)

         self.canvas.config(highlightthickness=0)
         sbarV = Scrollbar(self, orient=VERTICAL)
         sbarH = Scrollbar(self, orient=HORIZONTAL)

         sbarV.config(command=self.canvas.yview)
         sbarH.config(command=self.canvas.xview)

         self.canvas.config(yscrollcommand=sbarV.set)
         self.canvas.config(xscrollcommand=sbarH.set)

         sbarV.pack(side=RIGHT, fill=Y)
         sbarH.pack(side=BOTTOM, fill=X)

         self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)
         self.im=Image.open("/home/fausto/Dropbox/Aline/Fotos celular/WP_20151219_22_22_32_Pro.jpg")
         width,height=self.im.size
         self.canvas.config(scrollregion=(0,0,width,height))
         self.im2=ImageTk.PhotoImage(self.im)
         self.imgtag=self.canvas.create_image(0,0,anchor="nw",image=self.im2)

ScrolledCanvas().mainloop()