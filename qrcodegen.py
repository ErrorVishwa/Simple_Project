#Import qrcode and tkinter libraries and Image libraries pillow library
import qrcode
from PIL import Image
from tkinter import*

#Making the primary window
vishwa = Tk()
vishwa.title('vishwa.com')
vishwa.geometry('700x250')
vishwa.config(bg='#99ff66')

#Create a function that takes any text or URL as an input and generates a qrcode 
def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(vishwa, text='File Saved!', bg='#e52165', fg='black', font=('Arial Black', 8)).pack()
    
def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()

#Create a User Interface for the application to Generate Qr Code in python
frame = Frame(vishwa, bg = '#99ff66')
frame.pack(expand = True)

#-----------------Enter the Text Or URL-----------------

Label(frame, text='Enter the Text Or URL :',font=('Arial Black', 16),
      bg='#99ff66').grid(row=0, column=0, sticky='w')
msg = Entry(frame)
msg.grid(row=0, column=1)

#-----------------Enter the file name---------------------

Label(frame, text='File Name(Save As) :',font = ('Arial Black', 16),
      bg = '#99ff66').grid(row=1, column=0, sticky='w')
save_name = Entry(frame)
save_name.grid(row=1, column=1)

#-----------------Button show or Save QRCode----------------------

btn = Button(vishwa, text='Show Qr code', bd='5',command=show,width=15)
btn.pack()
btn= Button(vishwa, text='Save Qr Code', command=generate, bd='5',width=15)
btn.pack()

vishwa.mainloop()