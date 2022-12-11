from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # first image
        img1 = Image.open("./college images/emplo4.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130) 

        # second image
        img2 = Image.open("./college images/emplo3.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130) 

        # third image
        img3 = Image.open("./college images/emplo7.png")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image = self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # Background  image
        bg = Image.open("./college images/bb.jpg")
        bg = bg.resize((1530, 710), Image.ANTIALIAS)
        self.photobg = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root, image = self.photobg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="EMPLOYEE MANAGEMENT SYSTEM", font=('times new roman', 35,  "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Employee Details", font=('times new roman', 12, 'bold'))
        left_frame.place(x=10, y=10, width=730,height=580)

        img_left = Image.open("./college images/emplo8.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image = self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130) 
        

        # current position
        current_position_frame = LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="Current Position Information", font=('times new roman', 12, 'bold'))
        current_position_frame.place(x=5, y=135, width=720,height=115)

        # Department

        dep_label = Label(current_position_frame, text="Department",font=('times new roman', 12, 'bold'),bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_position_frame, font=('times new roman', 12),state="readonly", width=17)
        dep_combo['values'] = ("Select Department", "IT", "Operations", "Sales", "Accounts", "Customer Support", "Welfare", "Legal", "Human Resource", "Directors")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Position

        position_label = Label(current_position_frame, text="Position",font=('times new roman', 12, 'bold'),bg="white")
        position_label.grid(row=0, column=2, padx=10, sticky=W)

        position_combo = ttk.Combobox(current_position_frame, font=('times new roman', 12),state="readonly", width=17)
        position_combo['values'] = ("Select Position", "Head of Department", "Manager", "C.E.O", "E.D", "Assistant Manager", "Cheff", "Driver", "Cleaner")
        position_combo.current(0)
        position_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year

        year_label = Label(current_position_frame, text="Year", font=('times new roman', 12, 'bold'), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_entry = ttk.Entry(current_position_frame, text="Year", font=('times new roman', 12), width=17)
        year_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)
    

        # contract status

        contract_label = Label(current_position_frame, text="Contract Status",font=('times new roman', 12, 'bold'),bg="white")
        contract_label.grid(row=1, column=2, padx=10, sticky=W)

        contract_combo = ttk.Combobox(current_position_frame, font=('times new roman', 12),state="readonly", width=17)
        contract_combo['values'] = ("Select Status","Regular", "Contractual", "Suspended")
        contract_combo.current(0)
        contract_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # Employee Information
        employee_info_frame = LabelFrame(left_frame, bd=2,bg="white", relief=RIDGE, text="Employee Information", font=('times new roman', 12, 'bold'))
        employee_info_frame.place(x=5, y=250, width=720,height=300)

        
        # employee ID
        EmployeeID_label = Label(employee_info_frame, text="ID:",font=('times new roman', 12, 'bold'),bg="white")
        EmployeeID_label.grid(row=0, column=0, padx=10,pady=5,  sticky=W)

        EmployeeID_entry = ttk.Entry(employee_info_frame, width=20, font=('times new roman', 13))
        EmployeeID_entry.grid(row=0, column=1,padx=10,pady=5, sticky=W)

        # employee name
        Employee_label = Label(employee_info_frame, text="Name:",font=('times new roman', 12, 'bold'),bg="white")
        Employee_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        Employee_entry = ttk.Entry(employee_info_frame, width=20, font=('times new roman', 13))
        Employee_entry.grid(row=0, column=3,padx=10,pady=5, sticky=W)


        # TIN
        TIN_label = Label(employee_info_frame, text="TIN #:",font=('times new roman', 12, 'bold'),bg="white")
        TIN_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        TIN_entry = ttk.Entry(employee_info_frame, width=20, font=('times new roman', 13))
        TIN_entry.grid(row=1, column=1,padx=10,pady=5, sticky=W)

        # Contact
        contact_label = Label(employee_info_frame, text="Contact #:",font=('times new roman', 12, 'bold'),bg="white")
        contact_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        contact_entry = ttk.Entry(employee_info_frame, width=20, font=('times new roman', 13))
        contact_entry.grid(row=1, column=3,padx=10, pady=5, sticky=W)

        # DOB
        DOB_label = Label(employee_info_frame, text="Date Of Birth:",font=('times new roman', 12, 'bold'),bg="white")
        DOB_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        DOB_entry = DateEntry(employee_info_frame, selectmode = 'day', year=2021, month=7, day=16, width=20, font=('times new roman', 13))
        DOB_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # Email
        email_label = Label(employee_info_frame, text="Email #:",font=('times new roman', 12, 'bold'),bg="white")
        email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(employee_info_frame, width=20, font=('times new roman', 13))
        email_entry.grid(row=2, column=3,padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(employee_info_frame, text="Gender",font=('times new roman', 12, 'bold'),bg="white")
        Gender_label.grid(row=3, column=0, padx=10,pady=5, sticky=W)

        Gender_combo = ttk.Combobox(employee_info_frame, font=('times new roman', 13),state="readonly", width=20)
        Gender_combo['values'] = ("Select Gender", "Male", "Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(employee_info_frame, text="Address:",font=('times new roman', 12, 'bold'),bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(employee_info_frame, width=20, font=('times new roman', 13))
        address_entry.grid(row=3, column=3,padx=10, pady=5, sticky=W)


        # date hired
        hired_label = Label(employee_info_frame, text="Date Hired:",font=('times new roman', 12, 'bold'),bg="white")
        hired_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        hired_entry = DateEntry(employee_info_frame, selectmode = 'day', year=2021, month=7, day=16, width=20, font=('times new roman', 13),state="readonly")
        hired_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        # End of contract
        end_contract_label = Label(employee_info_frame, text="End Of Contract:",font=('times new roman', 12, 'bold'),bg="white")
        end_contract_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        end_contract_entry = DateEntry(employee_info_frame, selectmode = 'day', year=2021, month=7, day=16, width=20, font=('times new roman', 13), state="readonly")
        end_contract_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)


        # radio Buttons
        radiobtn1 = ttk.Radiobutton(employee_info_frame, text="Take Photo Sample" , value='Yes')
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(employee_info_frame, text="No Photo Sample" , value='Yes')
        radiobtn2.grid(row=6, column=1)

        # Buttons frames
        btn_frame = Frame(employee_info_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=200, width=715, height=70)

        save_btn = Button(btn_frame, text="Save",width=19,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        save_btn.grid(row=0, column=0,)

        update_btn = Button(btn_frame, text="Update",width=19,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        update_btn.grid(row=0, column=1,)
    
        delete_btn = Button(btn_frame, text="Delete",width=19,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        delete_btn.grid(row=0, column=2,)

        reset_btn = Button(btn_frame, text="Reset",width=19,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        reset_btn.grid(row=0, column=3,)

        # Buttons frame1
        btn_frame1 = Frame(employee_info_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame1.place(x=0, y=240, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Take Photo",width= 42,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        take_photo_btn.grid(row=0, column=0,)

        update_photo_btn = Button(btn_frame1, text="Update Photo",width=42,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        update_photo_btn.grid(row=0, column=1)

        # right label frame
        right_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Employee Details", font=('times new roman', 12, 'bold'))
        right_frame.place(x=750, y=10, width=725,height=580)

        img_right = Image.open("./college images/emplo6.jpg")
        img_right = img_right.resize((710, 260), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f2_lbl = Label(right_frame, image = self.photoimg_right)
        f2_lbl.place(x=5, y=0, width=710, height=260)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2,bg="white", relief=RIDGE, text="View Employee Details & Search System", font=('times new roman', 12, 'bold'))
        search_frame.place(x=5, y=210, width=710,height=80)

        #search Buttons
        search_by_btn = Button(search_frame, text="Search By:",width=10,  font=('times new roman', 15, 'bold'), bg="red", fg='white')
        search_by_btn.grid(row=0, column=0, padx=2, pady=10, sticky=W)


        search_combo = ttk.Combobox(search_frame, font=('times new roman', 13),state="readonly", width=13)
        search_combo['values'] = ("Select Option", "ID", "Name", "Contact", "TIN", "Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=('times new roman', 12))
        search_entry.grid(row=0, column=2,padx=10, pady=5, sticky=W)
    
        search_btn = Button(search_frame, text="Search",width=12,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        search_btn.grid(row=0, column=3,padx=4)

        show_all_btn = Button(search_frame, text="Show All",width=12,  font=('times new roman', 12, 'bold'), bg="green", fg='white')
        show_all_btn.grid(row=0, column=4, padx=4)

        # Table frame
        table_frame = Frame(right_frame, bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5, y=300, width=710,height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=("dep", "pos", "Year", "Status", "ID",
        "Name", "TIN", "Contact", "DOB", "Email", "Gender", "Address", 'Hired', 'End', 'photo'), xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text="Department")
        self.employee_table.heading('pos', text="Position")
        self.employee_table.heading('Year', text="Year")
        self.employee_table.heading('Status', text="Contract Status")
        self.employee_table.heading('ID', text="ID")
        self.employee_table.heading('Name', text="Name")
        self.employee_table.heading('TIN', text="TIN")
        self.employee_table.heading('Contact', text="Contact")
        self.employee_table.heading('DOB', text="Date Of Birth")
        self.employee_table.heading('Email', text="Email")
        self.employee_table.heading('Gender', text="Gender")
        self.employee_table.heading('Address', text="Address")
        self.employee_table.heading('Hired', text="Date Hired")
        self.employee_table.heading('End', text="End Of Contract")
        self.employee_table.heading('photo', text="PhotoSampleStatus")
        self.employee_table['show'] = 'headings'


        self.employee_table.column('dep', width=100)
        self.employee_table.column('pos', width=100)
        self.employee_table.column('Year', width=100)
        self.employee_table.column('Status', width=100)
        self.employee_table.column('ID', width=100)
        self.employee_table.column('Name', width=100)
        self.employee_table.column('TIN', width=100)
        self.employee_table.column('Contact', width=100)
        self.employee_table.column('DOB', width=100)
        self.employee_table.column('Email', width=100)
        self.employee_table.column('Gender', width=100)
        self.employee_table.column('Address', width=100)
        self.employee_table.column('Hired', width=100)
        self.employee_table.column('End', width=100)
        self.employee_table.column('photo', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)


root = Tk()
obj = Employee(root)
root.mainloop() 