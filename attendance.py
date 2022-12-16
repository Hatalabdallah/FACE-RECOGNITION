from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')
        
        # first image
        img1 = Image.open("./college images/emplo4.png")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200) 

        # second image
        img2 = Image.open("./college images/emplo8.jpg")
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)
        
        # Background  image
        bg = Image.open("./college images/bb.jpg")
        bg = bg.resize((1530, 710), Image.ANTIALIAS)
        self.photobg = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image = self.photobg)
        bg_img.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=('times new roman', 35,  "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1600, height=45)
        

root = Tk()
obj = Attendance(root)
root.mainloop() 