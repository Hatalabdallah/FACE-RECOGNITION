from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from Employee import Employee
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')



        # first image
        img1 = Image.open("./college images/stanford.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130) 

        # second image
        img2 = Image.open("./college images/facialrecognition.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130) 

        # third image
        img3 = Image.open("./college images/U.jpeg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image = self.photoimg3)
        f_lbl.place(x=1000, y=0, width=550, height=130) 


        # Background  image
        bg = Image.open("./college images/bb.jpg")
        bg = bg.resize((1530, 710), Image.ANTIALIAS)
        self.photobg = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image = self.photobg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=('times new roman', 35,  "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # student Button
        img4 = Image.open("./college images/employee.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command= self.employee_details)
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="EMPLOYEE DETAILS", cursor="hand2",command= self.employee_details, font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


        # Detect Face Button
        img5 = Image.open("./college images/face2.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command= self.face_reco)
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img, text="FACE RECOGNITION", cursor="hand2", command= self.face_reco,font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img6 = Image.open("./college images/attendance2.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="ATTENDANCE", cursor="hand2", font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help Button
        img7 = Image.open("./college images/help.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="HELP", cursor="hand2", font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train Button
        img8 = Image.open("./college images/train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command= self.train_data)
        b5.place(x=200, y=380, width=220, height=220)

        b5_1 = Button(bg_img, text="TRAIN DATA", cursor="hand2",command= self.train_data, font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=580, width=220, height=40)

        # Employee Photo Button
        img9 = Image.open("./college images/open2.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command= self.open_img)
        b6.place(x=500, y=380, width=220, height=220)

        b6_1 = Button(bg_img, text="EMPLOYEE PHOTOS", cursor="hand2", command= self.open_img,font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=580, width=220, height=40)

        # Developer Button
        img10 = Image.open("./college images/developer.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)

        b7_1 = Button(bg_img, text="DEVELOPER", cursor="hand2", font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=580, width=220, height=40)

        # Exit Button
        img11 = Image.open("./college images/exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)

        b8_1 = Button(bg_img, text="EXIT", cursor="hand2", font=('times new roman', 15,  "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=580, width=220, height=40)


    def open_img(self):
        os.startfile('data')
        
        
        
    #---------------------------------Functions Buttons_____
    
    def employee_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Employee(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)  
        
    def face_reco(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)  








# root = Tk()
# obj = Face_Recognition_System(root)
# root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
