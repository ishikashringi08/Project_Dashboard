import tkinter as tk
from tkinter import*
from tkinter import ttk, Menu, messagebox
import mysql.connector
from PIL import Image, ImageTk


root = tk.Tk()
root.title("STUDENT DASHBOARD")
root.geometry("1100x700")
bg_img = Image.open("C:/Users/Hi/OneDrive/Pictures/PROJECT/school_student_scene.jpg")
bg_img = bg_img.resize((1500, 800))          # match root.geometry() exactly
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = tk.Label(root, image = bg_photo)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
bg_label.lower()   



               # Keep it above the background

bg_img2 = Image.open(r"C:\Users\Hi\OneDrive\Pictures\PROJECT\GD_International_School_Logo.jpg")
bg_img2 = bg_img2.resize((300, 100))
bg_photo2 = ImageTk.PhotoImage(bg_img2)

bg_label2 = tk.Label(root, image=bg_photo2, bd=0)
bg_label2.image = bg_photo2    # Keep a reference
bg_label2.place(x=800, y=10)
bg_label2.lift() 


def connect():   
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Project_Ishika"
    )
    return conn

current_admin_username = None
current_admin_password = None


#-----------------------------------------------------------------------continue_profile------------------------------------------------------------------------------------------------------------------------
def continue_profile():
    name_var = tk.StringVar()
    password_var = tk.StringVar()
    username_var = tk.StringVar()
    adminname_var = tk.StringVar()
    adminpassword_var = tk.StringVar()
    adminusername_var = tk.StringVar()
    adminstpassword_var = tk.StringVar()
    adminstusername_var = tk.StringVar()
    DOB_var = tk.StringVar()
    email_var = tk.StringVar()
    phoneno_var = tk.StringVar()
    gender_var = tk.StringVar()
    address_var = tk.StringVar()
    course_var = tk.StringVar()
    oldpass_var = tk.StringVar()
    newpass_var = tk.StringVar()
    olduser_var = tk.StringVar()
    conpass_var = tk.StringVar()
    father_var = tk.StringVar()
    mother_var = tk.StringVar()
    email_var1 = tk.StringVar()
    phoneno_var1 = tk.StringVar()
    address_var1 = tk.StringVar()
    password_var1 = tk.StringVar()
    username_var1 = tk.StringVar()



    tcfee_var = tk.StringVar()
    ttfee_var = tk.StringVar()
    pcfee_var = tk.StringVar()
    ptfee_var = tk.StringVar()
    lcfee_var = tk.StringVar()
    ltfee_var = tk.StringVar()
    tm_var = tk.StringVar()
    mo_var = tk.StringVar()
    rank_var = tk.StringVar()
    td_var = tk.StringVar()
    da_var = tk.StringVar()
    remark_var = tk.StringVar()

    course_var = tk.StringVar()
    confirmpassword_var = tk.StringVar()
    if continuebtn.winfo_exists():
        continuebtn.destroy()

    if 'btnback' in globals() and btnback.winfo_exists():
        btnback.destroy()
        for widget in (note17, username_label, username_entry, password_label, password_entry, btnback, btnsubmit):
            widget.destroy()

    if 'adminbackbtn' in globals() and adminbackbtn.winfo_exists():
        adminbackbtn.destroy()
        for widget in (adminnote3, adminname_label, adminname_entry, adminpassword_label, adminpassword_entry, adminusername_label, adminusername_entry, adminstpassword_entry, adminstpassword_label, adminstusername_label, adminstusername_entry, adminbackbtn, adminsubmitbtn):
            widget.destroy()

    if 'adminbtnback' in globals() and adminbtnback.winfo_exists():
        adminbtnback.destroy()
        for widget in (adminnote17, adminusername_label, adminusername_entry, adminpassword_label, adminpassword_entry, adminbtnsubmit, adminstusername_label, adminstusername_entry, adminstpassword_label, adminstpassword_entry):
            widget.destroy()



    if 'backbtn' in globals() and backbtn.winfo_exists():
        backbtn.destroy()
        for widget in (note3, father_entry, father_label, mother_label, mother_entry,
                        name_label, name_entry, username_label, username_entry,
                        password_label, password_entry, DOB_label, DOB_entry,
                        email_label, email_entry, phoneno_label, phoneno_entry,
                        gender_label, gender_entry, address_label, address_entry,
                        course_label, course_entry, submitbtn,
                        confirmpassword_label, confirmpassword_entry, backbtn):
            widget.destroy()

    if 'loginagainbtn1' in globals() and loginagainbtn1.winfo_exists():
        loginagainbtn1.destroy()

    def clear_btn():
        widgets = [
        globals().get("pasbtn"), globals().get("updbtn"),
        globals().get("paybtn"), globals().get("attbtn"),
        globals().get("mrkbtn"), globals().get("lgout"),
        globals().get("infobtn")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()

    def clear_adminbtn():
        widgets = [
        globals().get("infobtn1"), globals().get("paybtn1"),
        globals().get("mrkbtn1"), globals().get("attbtn1"),
        globals().get("lgoutbtn1")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()

    def clear_info():
        widgets = [
        globals().get("note4"), globals().get("note5"),
        globals().get("note6"), globals().get("note7"),
        globals().get("note8"), globals().get("note9"),
        globals().get("note10"), globals().get("note11"),
        globals().get("note12"), globals().get("note13"),
        globals().get("note14"), globals().get("note15"),
        globals().get("note16")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()

    def clear_password():
        widgets = [
        globals().get("note18"),
        globals().get("old_label"),
        globals().get("old_entry"),
        globals().get("olduser_label"),
        globals().get("olduser_entry"),
        globals().get("new_label"),
        globals().get("new_entry"),
        globals().get("con_label"),
        globals().get("con_entry"),
        globals().get("newpassbtn")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()

    def clear_update():
        widgets = [
        globals().get("note19"),
        globals().get("username_label1"),
        globals().get("username_entry1"),
        globals().get("password_label1"),
        globals().get("password_entry1"),
        globals().get("email_label1"),
        globals().get("email_entry1"),
        globals().get("phoneno_label1"),
        globals().get("phoneno_entry1"),
        globals().get("address_label1"),
        globals().get("address_entry1"),
        globals().get("btnupdate")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()


    def clear_payments2():
        widgets = [
        globals().get("adminnote20"),
        globals().get("tcf_label"),
        globals().get("tcf_entry"),
        globals().get("ttfee_label"),
        globals().get("ttfee_entry"),
        globals().get("pcfee_label"),
        globals().get("pcfee_entry"),
        globals().get("ptfee_label"),
        globals().get("ptfee_entry"),
        globals().get("lcfee_label"),
        globals().get("lcfee_entry"),
        globals().get("ltfee_label"),
        globals().get("ltfee_entry"),
        globals().get("adminpaymentbtnsubmit")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()


    def clear_attendence2():
        widgets = [
        globals().get("adminnote21"), globals().get("td_label"),
        globals().get("td_entry"), globals().get("da_label"),
        globals().get("da_entry"),globals().get("adminattbtnsubmit")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()


    def clear_admininfo():
        widgets = [
        globals().get("adminnote4"),
        globals().get("adminnote5"),
        globals().get("adminnote6"),
        globals().get("adminnote7"),
        globals().get("adminnote8"),
        globals().get("adminnote9"),
        globals().get("adminnote10"),
        globals().get("adminnote11"),
        globals().get("adminnote12"),
        globals().get("adminnote13"),
        globals().get("adminnote14"),
        globals().get("adminnote15")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()


    def clear_marks2():
        widgets = [
        globals().get("adminnote22"), globals().get("tm_label"),
        globals().get("tm_entry"), globals().get("mo_label"),
        globals().get("mo_entry"),globals().get("adminmarkbtnsubmit"),
        globals().get("rank_entry"),globals().get("rank_label"),
        globals().get("remark_entry"),globals().get("remark_label")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()


    def clear_payment1():
        widgets = [
        globals().get("note23"), globals().get("note24"),
        globals().get("note25"), globals().get("note26"),
        globals().get("note27"),globals().get("note28"), globals().get("note29")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()

    def clear_attendence1():
        widgets = [
        globals().get("note30"), globals().get("note31"),
        globals().get("note32")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()
    
    
    def clear_mark1():
        widgets = [
        globals().get("note33"), globals().get("note34"),
        globals().get("note35"), globals().get("note36"), globals().get("note37")
    ]

        for widget in widgets:
            if widget and widget.winfo_exists():
                widget.destroy()


    if 'lgoutbtn' in globals() and lgoutbtn.winfo_exists():
        clear_info()
        clear_password()
        clear_update()
        clear_payments2()
        clear_attendence2()
        clear_admininfo()
        clear_marks2()
        clear_payment1()
        clear_attendence1()
        clear_mark1()
        clear_btn()
        clear_adminbtn()
        lgoutbtn.destroy()

    if 'lgoutbtn1' in globals() and lgoutbtn1.winfo_exists():
        clear_info()
        clear_password()
        clear_update()
        clear_payments2()
        clear_attendence2()
        clear_admininfo()
        clear_marks2()
        clear_payment1()
        clear_attendence1()
        clear_mark1()
        clear_btn()
        clear_adminbtn()

    global note, note1, note2, btnlogin, btnsignin
#-----------------------------------------------------------------------Submit New Password------------------------------------------------------------------------------------------------------------------------  


    def submitnewpass():
        oldpasw = oldpass_var.get()
        newpasw = newpass_var.get()
        olduser = olduser_var.get()
        newcon = conpass_var.get()

        conn = connect()
        cursor = conn.cursor()

        if oldpasw == "" or olduser == "" or newpasw == "" or newcon == "":
            messagebox.showerror("Empty Fields", "Please Fill The Required Details")
            oldpass_var.set("")
            newpass_var.set("")
            olduser_var.set("")
            conpass_var.set("")
            cursor.close()
            conn.close()
            return
        
        if newpasw != newcon:
            messagebox.showerror("Password Error", "Password and Confirm Password did not match.")
            oldpass_var.set("")
            newpass_var.set("")
            olduser_var.set("")
            conpass_var.set("")
            password_entry.focus()
            cursor.close()
            conn.close()
            return
        
        sql2 = """
                UPDATE project_dashboard
                SET Password = %s, Confirm_Password = %s
                WHERE Username=%s AND Password=%s"""
                            
        cursor.execute(sql2, (newpasw, newcon, olduser, oldpasw))

        if cursor.rowcount > 0:
            # Cascade the new password into project_admin_dashboard too,
            # so any admin linked to this student stays in sync.
            sql3 = """
                    UPDATE project_admin_dashboard
                    SET Password = %s
                    WHERE Username = %s AND Password = %s"""
            cursor.execute(sql3, (newpasw, olduser, oldpasw))

            conn.commit()
            messagebox.showinfo("Success", "Password changed successfully!")
            oldpass_var.set("")
            newpass_var.set("")
            olduser_var.set("")
            conpass_var.set("")
        else:
            messagebox.showerror("Error", "Username or old password is incorrect.")
            oldpass_var.set("")
            newpass_var.set("")
            olduser_var.set("")
            conpass_var.set("")

        cursor.close()
        conn.close()



#-----------------------------------------------------------------------Submit New Password//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Password1------------------------------------------------------------------------------------------------------------------------


    def password1():
        
        global note18, old_label, old_entry, olduser_label, olduser_entry, new_label, new_entry, con_label, con_entry, newpassbtn

        clear_info()
        clear_update()
        clear_password() 
        clear_payment1()     
        clear_attendence1() 
        clear_mark1()

        note18 = tk.Label(root, text = "Change Password", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
        note18.place(x = 280, y = 0)
        old_label = tk.Label(root, text = "Your Password", font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white", padx = 10, pady = 10)
        old_label.place(x = 180, y = 200)
        old_entry = tk.Entry(root, textvariable = oldpass_var, font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5)
        old_entry.place(x = 430, y = 200)

        olduser_label = tk.Label(root, text = "Username", font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white", padx = 10, pady = 10)
        olduser_label.place(x = 180, y = 250)
        olduser_entry = tk.Entry(root, textvariable = olduser_var, font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5)
        olduser_entry.place(x = 430, y = 250)

        new_label = tk.Label(root, text = "New Password", font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white", padx = 10, pady = 10)
        new_label.place(x = 180, y = 300)
        new_entry = tk.Entry(root, textvariable = newpass_var, font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5, show = "*")
        new_entry.place(x = 430, y = 300)

        con_label = tk.Label(root, text = "Confirm Password", font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white", padx = 10, pady = 10)
        con_label.place(x = 180, y = 350)
        con_entry = tk.Entry(root, textvariable = conpass_var, font = ("arial", 15, "bold"), relief = "solid", borderwidth = 5, show = "*")
        con_entry.place(x = 430, y = 350)

        newpassbtn = tk.Button(root, text = "Submit", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = submitnewpass)
        newpassbtn.place(x=470, y=500)      


#-----------------------------------------------------------------------Password1//------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------Submit In Update1------------------------------------------------------------------------------------------------------------------------


    def submitinupdate():

        email1 = email_var1.get()
        phone1 = phoneno_var1.get()
        address1 = address_var1.get()
        user = username_var1.get().strip()
        pasw = password_var1.get().strip()
        conn = connect()
        cursor = conn.cursor()

        if email1 == "" or phone1 == "" or address1 == "":
            messagebox.showerror("Empty Fields", "Please Fill The Required Details")
            email_var1.set("")
            phoneno_var1.set("")
            address_var1.set("")
            return
        
        sql3 = """
                UPDATE project_dashboard
                SET Email = %s, Phone_Number = %s, Address = %s
                WHERE Username=%s AND Password=%s"""
                            
        cursor.execute(sql3, (email1, phone1, address1, user, pasw))
        if cursor.rowcount > 0:
            conn.commit()
            messagebox.showinfo("Success", "Record Updated successfully!")
            email_var1.set("")
            phoneno_var1.set("")
            address_var1.set("")
        else:
            messagebox.showerror("Error","Username or Password is incorrect.")
            email_var1.set("")
            phoneno_var1.set("")
            address_var1.set("")
        cursor.close()
        conn.close()


#-----------------------------------------------------------------------Submit In Update1//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Update1------------------------------------------------------------------------------------------------------------------------------

    def update1():
        clear_info()
        clear_password()
        clear_update()
        clear_payment1()
        clear_attendence1()
        clear_mark1()


        global note19, username_label1, username_entry1, password_label1, password_entry1, email_label1, email_entry1, phoneno_label1, phoneno_entry1, address_entry1, address_label1, btnupdate

        
        note19 = tk.Label(root, text = "Update", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
        note19.place(x = 280, y = 0)
        username_label1 = tk.Label(root, text="Username", font=("arial", 15, "bold"), relief="solid",
                                   borderwidth=5, bg="darkgreen", fg="white")
        username_label1.place(x=170, y=100)
        username_entry1 = tk.Entry(root, textvariable=username_var1, font=("arial", 15, "bold"),
                                   relief="solid", borderwidth=5)
        username_entry1.place(x=320, y=100)

        password_label1 = tk.Label(root, text="Password", font=("arial", 15, "bold"), relief="solid",
                                   borderwidth=5, bg="darkgreen", fg="white")
        password_label1.place(x=170, y=170)
        password_entry1 = tk.Entry(root, textvariable=password_var1, font=("arial", 15, "bold"),
                                   relief="solid", borderwidth=5, show="*")
        password_entry1.place(x=320, y=170)

        email_label1 = tk.Label(root, text="Email", font=("arial", 15, "bold"), relief="solid",
                                borderwidth=5, bg="darkgreen", fg="white")
        email_label1.place(x=170, y=240)
        email_entry1 = tk.Entry(root, textvariable=email_var1, font=("arial", 15, "bold"),
                                relief="solid", borderwidth=5)
        email_entry1.place(x=320, y=240)

        phoneno_label1 = tk.Label(root, text="Contact Number", font=("arial", 12, "bold"), relief="solid",
                                  borderwidth=5, bg="darkgreen", fg="white", width=13, height=2)
        phoneno_label1.place(x=170, y=310)
        phoneno_entry1 = tk.Entry(root, textvariable=phoneno_var1, font=("arial", 15, "bold"),
                                  relief="solid", borderwidth=5)
        phoneno_entry1.place(x=320, y=310)

        address_label1 = tk.Label(root, text="Address", font=("arial", 15, "bold"), relief="solid",
                                  borderwidth=5, bg="darkgreen", fg="white")
        address_label1.place(x=170, y=380)
        address_entry1 = tk.Entry(root, textvariable=address_var1, font=("arial", 15, "bold"),
                                  relief="solid", borderwidth=5)
        address_entry1.place(x=320, y=380)

        btnupdate = tk.Button(root, text = "Update", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = submitinupdate)
        btnupdate.place(x=470, y=470)



#-----------------------------------------------------------------------Update1//----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Payment1----------------------------------------------------------------------------------------------------------------------------
    def payment1():
        global note23, note24, note25 , note26, note27, note28, note29
        clear_admininfo()
        clear_attendence2()
        clear_info()
        clear_marks2()
        clear_password()
        clear_payments2()
        clear_update()
        clear_payment1()
        clear_attendence1()
        clear_mark1()

        user = username_var.get()
        pasw = password_var.get()
        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_admin_dashboard WHERE Username=%s and Password=%s"
        result = (user,pasw)

        cursor.execute(sql, result)
        result = cursor.fetchone()

        if result: 
            
            note23 = tk.Label(root, text = "Payment Status", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            note23.place(x = 280, y = 0)
            note24 = tk.Label(root, text = f"Total Course Fees:   {result[3]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note24.place(x = 180, y = 100)
            note25 = tk.Label(root, text = f"Total Tuition Fees:   {result[4]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note25.place(x = 180, y = 150)
            note26 = tk.Label(root, text = f"Paid Course Fees:   {result[5]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note26.place(x = 180, y = 200)
            note27 = tk.Label(root, text = f"Paid Tuition Fees:   {result[6]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note27.place(x = 180, y = 250)
            note28 = tk.Label(root, text = f"Left Course Fees:   {result[7]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note28.place(x = 180, y = 300)
            note29 = tk.Label(root, text = f"Left Tuition Fees:  {result[8]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note29.place(x = 180, y = 350)

            cursor.close()
            conn.close()
            

#-----------------------------------------------------------------------Payment1//----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Attendence1----------------------------------------------------------------------------------------------------------------------------


    def attendence1():
        global note30, note31, note32
        clear_admininfo()
        clear_attendence2()
        clear_info()
        clear_marks2()
        clear_password()
        clear_payments2()
        clear_update()
        clear_payment1()
        clear_attendence1()
        clear_mark1()

        user = username_var.get()
        pasw = password_var.get()
        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_admin_dashboard WHERE Username=%s and Password=%s"
        result = (user,pasw)

        cursor.execute(sql, result)
        result = cursor.fetchone()

        if result: 
            
            note30 = tk.Label(root, text = "Attendence", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            note30.place(x = 280, y = 0)
            note31 = tk.Label(root, text = f"Total Working Days:   {result[13]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note31.place(x = 180, y = 200)
            note32 = tk.Label(root, text = f"Days Present:   {result[14]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note32.place(x = 180, y = 300)

            cursor.close()
            conn.close()


#-----------------------------------------------------------------------Attendence1//----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Marks And Rank1----------------------------------------------------------------------------------------------------------------------------


    def markrank1():
        global note33, note34, note35, note36, note37
        clear_admininfo()
        clear_attendence2()
        clear_info()
        clear_marks2()
        clear_password()
        clear_payments2()
        clear_update()
        clear_payment1()
        clear_attendence1()
        clear_mark1()

        user = username_var.get()
        pasw = password_var.get()
        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_admin_dashboard WHERE Username=%s and Password=%s"
        result = (user,pasw)

        cursor.execute(sql, result)
        result = cursor.fetchone()

        if result: 
            
            note33 = tk.Label(root, text = "Marks And Rank", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            note33.place(x = 280, y = 0)
            note34 = tk.Label(root, text = f"Total Marks:   {result[9]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note34.place(x = 180, y = 100)
            note35 = tk.Label(root, text = f"Marks Obtained:   {result[10]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note35.place(x = 180, y = 200)
            note36 = tk.Label(root, text = f"Rank:   {result[11]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note36.place(x = 180, y = 300)
            note37 = tk.Label(root, text = f"Remarks:   {result[12]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note37.place(x = 180, y = 400)
            

            cursor.close()
            conn.close()


#-----------------------------------------------------------------------Marks And Rank1//----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Student Info1----------------------------------------------------------------------------------------------------------------------------


    def info1():
        global note4, note5, note6, note7, note8, note9, note10, note11, note12, note13, note14, note15, note16
        clear_admininfo()
        clear_attendence2()
        clear_info()
        clear_marks2()
        clear_password()
        clear_payments2()
        clear_update()
        clear_payment1()
        clear_attendence1()
        clear_mark1()

        user = username_var.get()
        pasw = password_var.get()
        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_dashboard WHERE Username=%s and Password=%s"
        result = (user,pasw)

        cursor.execute(sql, result)
        result = cursor.fetchone()

        if result: 
            
            note4 = tk.Label(root, text = "Student Dashboard", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            note4.place(x = 280, y = 0)
            note5 = tk.Label(root, text = f"NAME:  {result[0]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note5.place(x = 180, y = 100)
            note6 = tk.Label(root, text = f"USERNAME:  {result[1]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note6.place(x = 180, y = 150)
            note7 = tk.Label(root, text = f"PASSWORD:  {result[2]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note7.place(x = 180, y = 200)
            note8 = tk.Label(root, text = f"CONFIRM PASSWORD:  {result[3]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note8.place(x = 180, y = 250)
            note9 = tk.Label(root, text = f"FATHER NAME:  {result[4]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note9.place(x = 180, y = 300)
            note10 = tk.Label(root, text = f"MOTHER NAME:  {result[5]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note10.place(x = 180, y = 350)
            note11 = tk.Label(root, text = f"DOB:  {result[6]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note11.place(x = 180, y = 400)
            note12 = tk.Label(root, text = f"EMAIL:  {result[7]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note12.place(x = 180, y = 450)
            note13 = tk.Label(root, text = f"CONTACT NUMBER:  {result[8]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note13.place(x = 180, y = 500)
            note14 = tk.Label(root, text = f"ADDRESS:  {result[9]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note14.place(x = 180, y = 550)
            note15 = tk.Label(root, text = f"GENDER:  {result[10]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note15.place(x = 180, y = 600)
            note16 = tk.Label(root, text = f"COURSE:  {result[11]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note16.place(x = 180, y = 650)
            

            cursor.close()
            conn.close()


#-----------------------------------------------------------------------Student Info1//----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Submit In Log In------------------------------------------------------------------------------------------------------------------------


    def submitinlogin():
        global note4, note5, note6, note7, note8, note9, note10, note11, note12, note13, note14, note15, note16
        global pasbtn, updbtn, paybtn, attbtn, mrkbtn, lgoutbtn, infobtn

        user = username_var.get()
        pasw = password_var.get()
        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_dashboard WHERE Username=%s and Password=%s"
        result = (user,pasw)

        cursor.execute(sql, result)
        result = cursor.fetchone()
        if user == "" or pasw == "":
            messagebox.showerror("Empty Fields", "Please Fill The Required Details")
            return
        if result: 
            
            for widget in (username_label, username_entry, password_label, password_entry, note17):
                widget.destroy()
            if btnback.winfo_exists():
                btnback.destroy()
            messagebox.showinfo("Success", "Login Successfully!")
            note4 = tk.Label(root, text = "Student Dashboard", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            note4.place(x = 280, y = 0)
            note5 = tk.Label(root, text = f"NAME:  {result[0]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note5.place(x = 180, y = 100)
            note6 = tk.Label(root, text = f"USERNAME:  {result[1]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note6.place(x = 180, y = 150)
            note7 = tk.Label(root, text = f"PASSWORD:  {result[2]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note7.place(x = 180, y = 200)
            note8 = tk.Label(root, text = f"CONFIRM PASSWORD:  {result[3]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note8.place(x = 180, y = 250)
            note9 = tk.Label(root, text = f"FATHER NAME:  {result[4]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note9.place(x = 180, y = 300)
            note10 = tk.Label(root, text = f"MOTHER NAME:  {result[5]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note10.place(x = 180, y = 350)
            note11 = tk.Label(root, text = f"DOB:  {result[6]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note11.place(x = 180, y = 400)
            note12 = tk.Label(root, text = f"EMAIL:  {result[7]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note12.place(x = 180, y = 450)
            note13 = tk.Label(root, text = f"CONTACT NUMBER:  {result[8]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note13.place(x = 180, y = 500)
            note14 = tk.Label(root, text = f"ADDRESS:  {result[9]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note14.place(x = 180, y = 550)
            note15 = tk.Label(root, text = f"GENDER:  {result[10]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note15.place(x = 180, y = 600)
            note16 = tk.Label(root, text = f"COURSE:  {result[11]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            note16.place(x = 180, y = 650)

            infobtn = tk.Button(root, text = "Info", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = info1)
            infobtn.place(x = 1, y = 70)
            pasbtn = tk.Button(root, text = "Password", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = password1)
            pasbtn.place(x = 1, y = 150)
            updbtn = tk.Button(root, text = "Update", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = update1)
            updbtn.place(x = 1, y = 230)
            paybtn = tk.Button(root, text = "Payments", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = payment1)
            paybtn.place(x = 1, y = 310)
            attbtn = tk.Button(root, text = "Attendence", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2,command = attendence1)
            attbtn.place(x = 1, y = 390)
            mrkbtn = tk.Button(root, text = "Marks/Rank", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = markrank1)
            mrkbtn.place(x = 1, y = 470)
            lgoutbtn = tk.Button(root, text = "Log-Out", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = continue_profile)
            lgoutbtn.place(x = 1, y = 550)

            

            btnsubmit.destroy()
            cursor.close()
            conn.close()

        else:
            messagebox.showerror("Incorrect","Incorrect! Username or Password")
            username_var.set("")
            password_var.set("")
            return

        

#-----------------------------------------------------------------------Submit In Log In//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Log In------------------------------------------------------------------------------------------------------------------------


    def login():
        widgets = [note, note1, note2, btnlogin, btnsignin, btnadminlogin, btnadminsignup]

        if 'loginagainbtn1' in globals() and loginagainbtn1.winfo_exists():
            widgets.append(loginagainbtn1)

        for widget in widgets:
            if widget.winfo_exists():
                widget.destroy()

        
        global note17, username_label, username_entry, password_label, password_entry, btnback, btnsubmit
        note17 = tk.Label(root, text = "LOGIN", font = ("arial", 15, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 5, padx = 5, pady = 15)
        note17.place(x = 470, y =0)

        username_label = tk.Label(root, text = "Username", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        username_label.place(x = 220, y = 250)
        username_entry = tk.Entry(root, textvariable = username_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        username_entry.place(x = 420, y = 250)

        password_label = tk.Label(root, text = "Password", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        password_label.place(x = 220, y = 350)
        password_entry = tk.Entry(root, textvariable = password_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, show = "*")
        password_entry.place(x = 420, y = 350)

        btnsubmit = tk.Button(root, text = "Submit", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = submitinlogin)
        btnsubmit.place(x=470, y=500)
        btnback = tk.Button(root, text = "Back", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = continue_profile)
        btnback.place(x=710, y=500)



#-----------------------------------------------------------------------Log In//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Submit In Sign Up------------------------------------------------------------------------------------------------------------------------


    def submitinsignup():

        global loginagainbtn1

        name = name_var.get().strip()
        username = username_var.get().strip()
        password = password_var.get().strip()
        conpass = confirmpassword_var.get().strip()
        father = father_var.get().strip()
        mother = mother_var.get().strip()
        DOB = DOB_var.get().strip()
        email = email_var.get().strip()
        phno = phoneno_var.get().strip()
        gender = gender_var.get().strip()
        address = address_var.get().strip()
        course = course_var.get().strip()

        if (name == "" or username == "" or password == "" or conpass == "" or
            father == "" or mother == "" or DOB == "" or email == "" or
            phno == "" or address == "" or
            gender in ("", "Select Option") or
            course in ("", "Select Course")):
            messagebox.showerror("Empty Fields", "Please fill all the required fields.")
            return

        if password != conpass:
            messagebox.showerror("Password Error", "Password and Confirm Password did not match.")
            password_var.set("")
            confirmpassword_var.set("")
            password_entry.focus()
            return

        try:
            conn = connect()
            cursor = conn.cursor()

            sql = """
            INSERT INTO project_dashboard
            (Name, Username, Password, Confirm_Password,
            Father_Name, Mother_Name, DOB, Email,
            Phone_Number, Address, Gender, Course)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                name, username, password, conpass,
                father, mother, DOB, email,
                phno, address, gender, course
            )

            cursor.execute(sql, values)
            conn.commit()

            messagebox.showinfo("Success", "Account created successfully!")

            # Destroy Signup Widgets
            for widget in (
                note3,
                father_entry, father_label,
                mother_label, mother_entry,
                name_label, name_entry,
                username_label, username_entry,
                password_label, password_entry,
                DOB_label, DOB_entry,
                email_label, email_entry,
                phoneno_label, phoneno_entry,
                gender_label, gender_entry,
                address_label, address_entry,
                course_label, course_entry,
                submitbtn,
                confirmpassword_label,
                confirmpassword_entry,
                backbtn
                ):
                if widget.winfo_exists():
                    widget.destroy()

            loginagainbtn1 = tk.Button(root, text="Login",
                font=("arial", 15, "bold"),
                relief="sunken",
                bg="darkgreen",
                fg="white",
                borderwidth=4,
                padx=2,
                pady=5,
                command=login
            )
            loginagainbtn1.place(x=500, y=350)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Could not save your details:\n{err}")

        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass



#-----------------------------------------------------------------------Submit In Sign Up//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Sign Up------------------------------------------------------------------------------------------------------------------------


    def signup():
        global name_label, name_entry, username_label, username_entry, password_label, password_entry, confirmpassword_label, confirmpassword_entry, father_label, father_entry, mother_label, mother_entry, DOB_label, DOB_entry, phoneno_label, phoneno_entry, phoneno_entry, email_label, email_entry, address_label, address_entry, course_label, course_entry, gender_label, gender_entry, note3, submitbtn, backbtn
        for widget in [note, note1, note2, btnlogin, btnsignin, btnadminsignup, btnadminlogin]:
            widget.destroy()

        note3 = tk.Label(root, text="SIGN UP", font=("arial", 15, "bold"), relief="solid",
                          bg="darkgreen", fg="white", borderwidth=5, padx=5, pady=15)
        note3.place(x=470, y=0)

        name_label = tk.Label(root, text="Full Name", font=("arial", 15, "bold"), relief="solid",
                               borderwidth=5, bg="darkgreen", fg="white")
        name_label.place(x=170, y=100)
        name_entry = tk.Entry(root, textvariable=name_var, font=("arial", 15, "bold"),
                               relief="solid", borderwidth=5)
        name_entry.place(x=320, y=100)

        username_label = tk.Label(root, text="Username", font=("arial", 15, "bold"), relief="solid",
                                   borderwidth=5, bg="darkgreen", fg="white")
        username_label.place(x=170, y=170)
        username_entry = tk.Entry(root, textvariable=username_var, font=("arial", 15, "bold"),
                                   relief="solid", borderwidth=5)
        username_entry.place(x=320, y=170)

        password_label = tk.Label(root, text="Password", font=("arial", 15, "bold"), relief="solid",
                                   borderwidth=5, bg="darkgreen", fg="white")
        password_label.place(x=170, y=240)
        password_entry = tk.Entry(root, textvariable=password_var, font=("arial", 15, "bold"),
                                   relief="solid", borderwidth=5, show="*")
        password_entry.place(x=320, y=240)

        confirmpassword_label = tk.Label(root, text="Confirm_Password", font=("arial", 15, "bold"),
                                          relief="solid", borderwidth=5, bg="darkgreen", fg="white")
        confirmpassword_label.place(x=170, y=310)
        confirmpassword_entry = tk.Entry(root, textvariable=confirmpassword_var, font=("arial", 15, "bold"),
                                          relief="solid", borderwidth=5, show="*")
        confirmpassword_entry.place(x=320, y=310)

        father_label = tk.Label(root, text="Father_Name", font=("arial", 15, "bold"), relief="solid",
                                 borderwidth=5, bg="darkgreen", fg="white")
        father_label.place(x=170, y=380)
        father_entry = tk.Entry(root, textvariable=father_var, font=("arial", 15, "bold"),
                                 relief="solid", borderwidth=5)
        father_entry.place(x=320, y=380)

        mother_label = tk.Label(root, text="Mother_Name", font=("arial", 15, "bold"), relief="solid",
                                 borderwidth=5, bg="darkgreen", fg="white")
        mother_label.place(x=170, y=450)
        mother_entry = tk.Entry(root, textvariable=mother_var, font=("arial", 15, "bold"),
                                 relief="solid", borderwidth=5)
        mother_entry.place(x=320, y=450)

        DOB_label = tk.Label(root, text="DOB", font=("arial", 15, "bold"), relief="solid",
                              borderwidth=5, bg="darkgreen", fg="white")
        DOB_label.place(x=170, y=520)
        DOB_entry = tk.Entry(root, textvariable=DOB_var, font=("arial", 15, "bold"),
                              relief="solid", borderwidth=5)
        DOB_entry.place(x=320, y=520)

        email_label = tk.Label(root, text="Email", font=("arial", 15, "bold"), relief="solid",
                                borderwidth=5, bg="darkgreen", fg="white")
        email_label.place(x=650, y=100)
        email_entry = tk.Entry(root, textvariable=email_var, font=("arial", 15, "bold"),
                                relief="solid", borderwidth=5)
        email_entry.place(x=780, y=100)

        phoneno_label = tk.Label(root, text="Contact Number", font=("arial", 12, "bold"), relief="solid",
                                  borderwidth=5, bg="darkgreen", fg="white", width=13, height=2)
        phoneno_label.place(x=650, y=170)
        phoneno_entry = tk.Entry(root, textvariable=phoneno_var, font=("arial", 15, "bold"),
                                  relief="solid", borderwidth=5)
        phoneno_entry.place(x=780, y=170)

        address_label = tk.Label(root, text="Address", font=("arial", 15, "bold"), relief="solid",
                                  borderwidth=5, bg="darkgreen", fg="white")
        address_label.place(x=650, y=240)
        address_entry = tk.Entry(root, textvariable=address_var, font=("arial", 15, "bold"),
                                  relief="solid", borderwidth=5)
        address_entry.place(x=780, y=240)

        gender_label = tk.Label(root, text="Gender", font=("arial", 15, "bold"), relief="solid",
                                 borderwidth=5, bg="darkgreen", fg="white")
        gender_label.place(x=650, y=310)
        gender_options = ["Male", "Female", "Other"]

        gender_entry = ttk.Combobox(root, values=gender_options, textvariable=gender_var,
                                     font=("arial", 15, "bold"), state="readonly", width=20, height=2)
        gender_entry.place(x=780, y=310)

        course_label = tk.Label(root, text="Course", font=("arial", 15, "bold"), relief="solid",
                                 borderwidth=5, bg="darkgreen", fg="white")
        course_label.place(x=650, y=380)
        course_options = ["Medical(PCB)", "Non-Medical(PCM)", "Commerce", "Humanities"]
        course_entry = ttk.Combobox(root, values=course_options, textvariable=course_var,
                                     font=("arial", 15, "bold"), state="readonly", width=20, height=2)
        course_entry.place(x=780, y=380)

        submitbtn = tk.Button(root, text="SUBMIT", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = submitinsignup)
        submitbtn.place(x=470, y=600)
        backbtn = tk.Button(root, text = "Back", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = continue_profile)
        backbtn.place(x=710, y=600)

        name_var.set("")
        password_var.set("")
        username_var.set("")
        DOB_var.set("")
        email_var.set("")
        phoneno_var.set("")
        address_var.set("")
        father_var.set("")
        mother_var.set("")
        gender_var.set("Select Option")
        course_var.set("Select Course")
        confirmpassword_var.set("")


#-----------------------------------------------------------------------Sign Up//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Submit In Admin Signup------------------------------------------------------------------------------------------------------------------------



    def submitinadminsignup():
        global loginagainbtn
        adminname = adminname_var.get()
        adminusername = adminusername_var.get()
        adminpassword = adminpassword_var.get()
        adminstusername = adminstusername_var.get()
        adminstpassword = adminstpassword_var.get()
        
        if (adminname == "" or adminusername == "" or adminpassword == "" or 
            adminstusername == "" or adminstpassword == ""):
            messagebox.showerror("Empty Fields", "Please fill all the required fields.")
            return

        try:
            conn = connect()
            cursor = conn.cursor()

            # Check whether the student exists
            sql = "SELECT * FROM project_dashboard WHERE Username=%s and Password=%s"
            result = (adminstusername, adminstpassword)
            cursor.execute(sql, result)
            student = cursor.fetchone()

            if student:

                # Check whether the student is already assigned to an admin
                sql = "SELECT * FROM project_admin_dashboard WHERE Username=%s"
                cursor.execute(sql, (adminstusername,))
                existing = cursor.fetchone()

                if existing:
                    messagebox.showerror("Error", "This student already has an admin.")
                    return

                # Insert admin details
                sql = """
                INSERT INTO project_admin_dashboard
                (Admin_Name, Admin_Username, Admin_Password, Username, Password)
                VALUES (%s,%s,%s,%s,%s)
                """
                values = (
                    adminname,
                    adminusername,
                    adminpassword,
                    adminstusername,
                    adminstpassword
                )

                cursor.execute(sql, values)
                conn.commit()

                messagebox.showinfo("Success", "Admin Account created successfully!")

                for widget in (
                    adminnote3,
                    adminname_label,
                    adminname_entry,
                    adminpassword_label,
                    adminpassword_entry,
                    adminusername_label,
                    adminusername_entry,
                    adminstpassword_entry,
                    adminstpassword_label,
                    adminstusername_label,
                    adminstusername_entry,
                    adminbackbtn,
                    adminsubmitbtn
                ):
                    widget.destroy()

                loginagainbtn = tk.Button(
                    root,
                    text="Login",
                    font=("arial", 15, "bold"),
                    relief="sunken",
                    bg="darkgreen",
                    fg="white",
                    borderwidth=4,
                    padx=2,
                    pady=5,
                    command=adminlogin
                )
                loginagainbtn.place(x=500, y=350)

            else:
                messagebox.showerror("Error", "Student Username or Password is incorrect.")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Could not save your details:\n{err}")
            return

        finally:
            try:
                cursor.close()
                conn.close()
            except Exception:
                pass




#-----------------------------------------------------------------------Submit In Admin Signup//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Save Attendence2------------------------------------------------------------------------------------------------------------------------


    def saveattendence():
        td = td_var.get()
        da = da_var.get()

        if td == "" or da == "":
            messagebox.showerror("Failure", "Enter Desired Details!")
            return

        conn = connect()
        cursor = conn.cursor()
        sql = """
            UPDATE project_admin_dashboard
            SET Total_WorkingDayss=%s, Days_Attended=%s
            WHERE Admin_Username=%s AND Admin_Password=%s"""
        values = (td, da, current_admin_username, current_admin_password)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Details Submitted successfully!")
        else:
            messagebox.showerror("Error", "Could not find your record to update.")

        td_var.set("")
        da_var.set("")
        cursor.close()
        conn.close()



#-----------------------------------------------------------------------Save Attendence2//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Attendence2------------------------------------------------------------------------------------------------------------------------


    def attendence2():

        global adminnote21, td_label, td_entry, da_label, da_entry, adminattbtnsubmit

        clear_attendence2()
        clear_payments2()
        clear_admininfo()
        clear_marks2()

        adminnote21 = tk.Label(root, text = "Attendence", font = ("arial", 15, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 5, padx = 5, pady = 15)
        adminnote21.place(x = 470, y =0)

        td_label = tk.Label(root, text = "Total Days", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        td_label.place(x = 220, y = 150)
        td_entry = tk.Entry(root, textvariable = td_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        td_entry.place(x = 520, y = 150)

        da_label = tk.Label(root, text = "Days Attended", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        da_label.place(x = 220, y = 250)
        da_entry = tk.Entry(root, textvariable = da_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        da_entry.place(x = 520, y = 250)

        adminattbtnsubmit = tk.Button(root, text = "Save", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = saveattendence)
        adminattbtnsubmit.place(x=470, y=350)


#-----------------------------------------------------------------------Attendence2//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Save Payment2-----------------------------------------------------------------------------------------------------------------------------------


    def savepayment():
        tcfee = tcfee_var.get()
        ttfee = ttfee_var.get()
        pcfee = pcfee_var.get()
        ptfee = ptfee_var.get()
        lcfee = lcfee_var.get()
        ltfee = ltfee_var.get()

        if tcfee == "" or ttfee == "" or pcfee == "" or ptfee == "" or lcfee == "" or ltfee == "":
            messagebox.showerror("Failure", "Enter Desired Details!")
            return

        conn = connect()
        cursor = conn.cursor()
        sql = """
            UPDATE project_admin_dashboard
            SET Total_CourseFee=%s, Total_TuitionFee=%s, Paid_CourseFee=%s,
                Paid_TuitionFee=%s, Left_CourseFee=%s, Left_TuitionFee=%s
            WHERE Admin_Username=%s AND Admin_Password=%s"""
        values = (tcfee, ttfee, pcfee, ptfee, lcfee, ltfee, current_admin_username, current_admin_password)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Details Submitted successfully!")
        else:
            messagebox.showerror("Error", "Could not find your record to update.")

        tcfee_var.set("")
        ttfee_var.set("")
        pcfee_var.set("")
        ptfee_var.set("")
        lcfee_var.set("")
        ltfee_var.set("")
        cursor.close()
        conn.close()

#-----------------------------------------------------------------------Save Payment2//-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Payment2-----------------------------------------------------------------------------------------------------------------------------------


    def payment2():
        
        global adminnote20, tcf_label, tcf_entry, ttfee_label, ttfee_entry, pcfee_label, pcfee_entry, ptfee_label, ptfee_entry, adminpaymentbtnsubmit, lcfee_label, lcfee_entry, ltfee_label, ltfee_entry

        clear_attendence2()
        clear_payments2()
        clear_admininfo()
        clear_marks2()

        adminnote20 = tk.Label(root, text = "Payments", font = ("arial", 15, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 5, padx = 5, pady = 15)
        adminnote20.place(x = 470, y =0)

        tcf_label = tk.Label(root, text = "Total Course Fees", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        tcf_label.place(x = 220, y = 100)
        tcf_entry = tk.Entry(root, textvariable = tcfee_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        tcf_entry.place(x = 520, y = 100)

        ttfee_label = tk.Label(root, text = "Total Tuition Fees", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        ttfee_label.place(x = 220, y = 200)
        ttfee_entry = tk.Entry(root, textvariable = ttfee_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        ttfee_entry.place(x = 520, y = 200)

        pcfee_label = tk.Label(root, text = "Paid Course Fees", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        pcfee_label.place(x = 220, y = 300)
        pcfee_entry = tk.Entry(root, textvariable = pcfee_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        pcfee_entry.place(x = 520, y = 300)

        ptfee_label = tk.Label(root, text = "Paid Tuition Fees", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        ptfee_label.place(x = 220, y = 400)
        ptfee_entry = tk.Entry(root, textvariable = ptfee_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        ptfee_entry.place(x = 520, y = 400)

        lcfee_label = tk.Label(root, text = "Left Course Fees", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        lcfee_label.place(x = 220, y = 500)
        lcfee_entry = tk.Entry(root, textvariable = lcfee_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        lcfee_entry.place(x = 520, y = 500)

        ltfee_label = tk.Label(root, text = "Left Tuition Fees", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        ltfee_label.place(x = 220, y = 600)
        ltfee_entry = tk.Entry(root, textvariable = ltfee_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        ltfee_entry.place(x = 520, y = 600)

        adminpaymentbtnsubmit = tk.Button(root, text = "Save", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = savepayment)
        adminpaymentbtnsubmit.place(x=470, y=650)
        


#-----------------------------------------------------------------------Payment2//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Save Marks And Rank 2------------------------------------------------------------------------------------------------------------------------


    def savemarks():
        tm = tm_var.get()
        mo = mo_var.get()
        rank = rank_var.get()
        remark = remark_var.get()

        if tm == "" or mo == "" or rank == "" or remark == "":
            messagebox.showerror("Failure", "Enter Desired Details!")
            return

        conn = connect()
        cursor = conn.cursor()
        sql = """
            UPDATE project_admin_dashboard
            SET Total_Marks=%s, Marks_Obtained=%s, Rank=%s, Remark = %s
            WHERE Admin_Username=%s AND Admin_Password=%s"""
        values = (tm, mo, rank, remark, current_admin_username, current_admin_password)
        cursor.execute(sql, values)
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Details Submitted successfully!")
        else:
            messagebox.showerror("Error", "Could not find your record to update.")

        tm_var.set("")
        mo_var.set("")
        rank_var.set("")
        remark_var.set("")
        cursor.close()
        conn.close()


#-----------------------------------------------------------------------Save Marks And Rank2//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Mark And Rank 2------------------------------------------------------------------------------------------------------------------------


    def markrank2():

        clear_admininfo()
        clear_attendence2()
        clear_payments2()
        clear_marks2()
        global adminnote22, tm_label, tm_entry, mo_label, mo_entry, rank_label, rank_entry, adminmarkbtnsubmit, remark_entry, remark_label

        adminnote22 = tk.Label(root, text = "Marks And Rank", font = ("arial", 15, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 5, padx = 5, pady = 15)
        adminnote22.place(x = 430, y =0)

        tm_label = tk.Label(root, text = "Total Marks", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        tm_label.place(x = 220, y = 100)
        tm_entry = tk.Entry(root, textvariable = tm_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        tm_entry.place(x = 520, y = 100)

        mo_label = tk.Label(root, text = "Marks Obtained", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        mo_label.place(x = 220, y = 200)
        mo_entry = tk.Entry(root, textvariable = mo_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        mo_entry.place(x = 520, y = 200)

        rank_label = tk.Label(root, text = "Rank", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        rank_label.place(x = 220, y = 300)
        rank_entry = tk.Entry(root, textvariable = rank_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        rank_entry.place(x = 520, y = 300)

        remark_label = tk.Label(root, text = "Remarks", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        remark_label.place(x = 220, y = 400)
        remark_entry = tk.Entry(root, textvariable = remark_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        remark_entry.place(x = 520, y = 400)

        adminmarkbtnsubmit = tk.Button(root, text = "Save", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = savemarks)
        adminmarkbtnsubmit.place(x=470, y=550)

#-----------------------------------------------------------------------Mark And Rank 2//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Admin Info------------------------------------------------------------------------------------------------------------------------


    def admininfo():
        global adminnote4, adminnote5, adminnote6, adminnote7, adminnote8, adminnote9, adminnote10, adminnote11, adminnote12, adminnote13, adminnote14, adminnote15
        clear_admininfo()
        clear_attendence2()
        clear_info()
        clear_marks2()
        clear_password()
        clear_payments2()
        clear_update()
        clear_payment1()
        clear_attendence1()
        clear_mark1()

        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_admin_dashboard WHERE Admin_Username=%s AND Admin_Password=%s"
        result = (current_admin_username, current_admin_password)

        cursor.execute(sql, result)
        result = cursor.fetchone()

        if result: 
            
            adminnote4 = tk.Label(root, text = "Teacher's Dashboard", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            adminnote4.place(x = 280, y = 0)
            adminnote5 = tk.Label(root, text = f"ADMIN NAME:  {result[0]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote5.place(x = 180, y = 100)
            adminnote6 = tk.Label(root, text = f"ADMIN USERNAME:   {result[1]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote6.place(x = 180, y = 150)
            adminnote7 = tk.Label(root, text = f"ADMIN PASSWORD:   {result[2]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote7.place(x = 180, y = 200)
            adminnote8 = tk.Label(root, text = f"STUDENT USERNAME:   {result[15]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote8.place(x = 180, y = 250)
            adminnote9 = tk.Label(root, text = f"STUDENT PASSWORD:   {result[16]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote9.place(x = 180, y = 300)
            adminnote10 = tk.Label(root, text = f"PAID COURSE  FEES:  {result[5]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote10.place(x = 180, y = 350)
            adminnote11 = tk.Label(root, text = f"PAID TUITION FEES:  {result[6]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote11.place(x = 180, y = 400)
            adminnote12 = tk.Label(root, text = f"MARKS OBTAINED:  {result[9]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote12.place(x = 180, y = 450)
            adminnote13 = tk.Label(root, text = f"RANK:  {result[10]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote13.place(x = 180, y = 500)
            adminnote14 = tk.Label(root, text = f"ATTENDANCE:  {result[14]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote14.place(x = 180, y = 550)
            adminnote15 = tk.Label(root, text = f"REMARKS:  {result[11]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote15.place(x = 180, y = 600)
            

            cursor.close()
            conn.close()
#-----------------------------------------------------------------------Admin Info//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Submit In Admin Log In------------------------------------------------------------------------------------------------------------------------


    def submitinadminlogin():
        

        global adminnote4, adminnote5, adminnote6, adminnote7, adminnote8, adminnote9, adminnote10, adminnote11, adminnote12, adminnote13, adminnote14, adminnote15
        global current_admin_username, current_admin_password
        global infobtn1, paybtn1, attbtn1, mrkbtn1, lgoutbtn1

        adminusername = adminusername_var.get()
        adminpassword = adminpassword_var.get()
        adminstusername = adminstusername_var.get()
        adminstpassword = adminstpassword_var.get()


        conn = connect()
        cursor = conn.cursor()

        sql = "SELECT *  FROM project_admin_dashboard WHERE Admin_Username=%s and Admin_Password=%s and Username = %s and Password = %s"
        result = (adminusername, adminpassword, adminstusername, adminstpassword)

        cursor.execute(sql, result)
        result = cursor.fetchone()
        if adminusername == "" or adminpassword == "" or adminstusername == "" or adminstpassword == "":
            messagebox.showerror("Empty Fields", "Please Fill The Required Details")
            return
        
        if result: 
            
            for widget in (adminnote17, adminusername_label, adminusername_entry, adminpassword_label, adminpassword_entry, adminbtnsubmit, adminstpassword_label, adminstpassword_entry, adminstusername_label,adminstusername_entry):
                widget.destroy()
            if adminbtnback.winfo_exists():
                adminbtnback.destroy()
            messagebox.showinfo("Success", "Login Successfully!")

            current_admin_username = adminusername
            current_admin_password = adminpassword

            adminnote4 = tk.Label(root, text = "Teacher's Dashboard", font = ("arial", 30, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 7, padx = 6, pady = 15)
            adminnote4.place(x = 280, y = 0)
            adminnote5 = tk.Label(root, text = f"ADMIN NAME:  {result[0]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote5.place(x = 180, y = 100)
            adminnote6 = tk.Label(root, text = f"ADMIN USERNAME:   {result[1]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote6.place(x = 180, y = 150)
            adminnote7 = tk.Label(root, text = f"ADMIN PASSWORD:   {result[2]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote7.place(x = 180, y = 200)
            adminnote8 = tk.Label(root, text = f"STUDENT USERNAME:   {result[15]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote8.place(x = 180, y = 250)
            adminnote9 = tk.Label(root, text = f"STUDENT PASSWORD:   {result[16]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote9.place(x = 180, y = 300)
            adminnote10 = tk.Label(root, text = f"PAID COURSE  FEES:  {result[5]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote10.place(x = 180, y = 350)
            adminnote11 = tk.Label(root, text = f"PAID TUITION FEES:  {result[6]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote11.place(x = 180, y = 400)
            adminnote12 = tk.Label(root, text = f"MARKS OBTAINED:  {result[9]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote12.place(x = 180, y = 450)
            adminnote13 = tk.Label(root, text = f"RANK:  {result[10]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote13.place(x = 180, y = 500)
            adminnote14 = tk.Label(root, text = f"ATTENDANCE:  {result[14]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote14.place(x = 180, y = 550)
            adminnote15 = tk.Label(root, text = f"REMARKS:  {result[11]}", font = ("Arial", 14, "bold"),fg = "black", padx = 5, pady = 10)
            adminnote15.place(x = 180, y = 600)

            infobtn1 = tk.Button(root, text = "Info", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = admininfo)
            infobtn1.place(x = 1, y = 150)
            paybtn1 = tk.Button(root, text = "Payments", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = payment2)
            paybtn1.place(x = 1, y = 250)
            attbtn1 = tk.Button(root, text = "Attendence", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = attendence2)
            attbtn1.place(x = 1, y = 350)
            mrkbtn1 = tk.Button(root, text = "Marks/Rank", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = markrank2)
            mrkbtn1.place(x = 1, y = 450)
            lgoutbtn1 = tk.Button(root, text = "Log-Out", font = ("arial", 17, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 4, width=10,height=2, command = continue_profile)
            lgoutbtn1.place(x = 1, y = 550)
            adminusername_var.set("")
            adminpassword_var.set("")
            adminstusername_var.set("")
            adminstpassword_var.set("")
            

            adminbtnsubmit.destroy()
            cursor.close()
            conn.close()

        else:
            messagebox.showerror("Incorrect","Incorrect! Username or Password")
            username_var.set("")
            password_var.set("")



#-----------------------------------------------------------------------Submit In Admin Log In//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Admin Log In------------------------------------------------------------------------------------------------------------------------


    def adminlogin():
        widgets = [note, note1, note2, btnlogin, btnsignin, btnadminlogin, btnadminsignup]

        if 'loginagainbtn' in globals() and loginagainbtn.winfo_exists():
            widgets.append(loginagainbtn)

        for widget in widgets:
            if widget.winfo_exists():
                widget.destroy()
        
        global adminnote17, adminusername_label, adminusername_entry, adminpassword_label, adminpassword_entry, adminbtnsubmit, adminbtnback, adminstusername_label, adminstusername_entry, adminstpassword_label, adminstpassword_entry

        adminnote17 = tk.Label(root, text = "LOGIN", font = ("arial", 15, "bold"), relief = "solid", bg = "darkgreen", fg = "white",  borderwidth = 5, padx = 5, pady = 15)
        adminnote17.place(x = 470, y =0)

        adminusername_label = tk.Label(root, text = "Admin Username", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        adminusername_label.place(x = 170, y = 150)
        adminusername_entry = tk.Entry(root, textvariable = adminusername_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        adminusername_entry.place(x = 450, y = 150)

        adminpassword_label = tk.Label(root, text = "Admin Password", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        adminpassword_label.place(x = 170, y = 250)
        adminpassword_entry = tk.Entry(root, textvariable = adminpassword_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, show = "*")
        adminpassword_entry.place(x = 450, y = 250)

        adminstusername_label = tk.Label(root, text = "Student Username", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        adminstusername_label.place(x = 170, y = 350)
        adminstusername_entry = tk.Entry(root, textvariable = adminstusername_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5)
        adminstusername_entry.place(x = 450, y = 350)

        adminstpassword_label = tk.Label(root, text = "Student Password", font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, bg = "darkgreen", fg = "white")
        adminstpassword_label.place(x = 170, y = 450)
        adminstpassword_entry = tk.Entry(root, textvariable = adminstpassword_var, font = ("arial", 20, "bold"), relief = "solid", borderwidth = 5, show = "*")
        adminstpassword_entry.place(x = 450, y = 450)

        adminbtnsubmit = tk.Button(root, text = "Submit", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = submitinadminlogin)
        adminbtnsubmit.place(x=470, y=550)
        adminbtnback = tk.Button(root, text = "Back", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = continue_profile)
        adminbtnback.place(x=710, y=560)


#-----------------------------------------------------------------------Admin Log In//------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------Admin Sign Up------------------------------------------------------------------------------------------------------------------------


    def adminsignup():

        global adminnote3, adminname_label, adminname_entry, adminpassword_label, adminpassword_entry, adminusername_label, adminusername_entry, adminstpassword_entry, adminstpassword_label, adminstusername_label, adminstusername_entry, adminbackbtn, adminsubmitbtn

        for widget in [note, note1, note2, btnlogin, btnsignin, btnadminlogin, btnadminsignup]:
            widget.destroy()

        adminnote3 = tk.Label(root, text="SIGN UP", font=("arial", 15, "bold"), relief="solid",
                          bg="darkgreen", fg="white", borderwidth=5, padx=5, pady=15)
        adminnote3.place(x=470, y=0)

        adminname_label = tk.Label(root, text="Admin Full Name", font=("arial", 15, "bold"), relief="solid",
                               borderwidth=5, bg="darkgreen", fg="white")
        adminname_label.place(x=120, y=100)
        adminname_entry = tk.Entry(root, textvariable=adminname_var, font=("arial", 15, "bold"),
                               relief="solid", borderwidth=5)
        adminname_entry.place(x=320, y=100)

        adminusername_label = tk.Label(root, text="Admin Username", font=("arial", 15, "bold"), relief="solid",
                                   borderwidth=5, bg="darkgreen", fg="white")
        adminusername_label.place(x=120, y=170)
        adminusername_entry = tk.Entry(root, textvariable=adminusername_var, font=("arial", 15, "bold"),
                                   relief="solid", borderwidth=5)
        adminusername_entry.place(x=320, y=170)

        adminpassword_label = tk.Label(root, text="Admin Password", font=("arial", 15, "bold"), relief="solid",
                                   borderwidth=5, bg="darkgreen", fg="white")
        adminpassword_label.place(x=120, y=240)
        adminpassword_entry = tk.Entry(root, textvariable=adminpassword_var, font=("arial", 15, "bold"),
                                   relief="solid", borderwidth=5, show="*")
        adminpassword_entry.place(x=320, y=240)

        adminstusername_label = tk.Label(root, text="Student Username", font=("arial", 15, "bold"),
                                          relief="solid", borderwidth=5, bg="darkgreen", fg="white")
        adminstusername_label.place(x=120, y=310)
        adminstusername_entry = tk.Entry(root, textvariable=adminstusername_var, font=("arial", 15, "bold"),
                                          relief="solid", borderwidth=5)
        adminstusername_entry.place(x=320, y=310)

        adminstpassword_label = tk.Label(root, text="Student Password", font=("arial", 15, "bold"), relief="solid",
                                 borderwidth=5, bg="darkgreen", fg="white")
        adminstpassword_label.place(x=120, y=380)
        adminstpassword_entry = tk.Entry(root, textvariable=adminstpassword_var, font=("arial", 15, "bold"),
                                 relief="solid", borderwidth=5, show="*")
        adminstpassword_entry.place(x=320, y=380)

        adminsubmitbtn = tk.Button(root, text="SUBMIT", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = submitinadminsignup)
        adminsubmitbtn.place(x=470, y=600)
        adminbackbtn = tk.Button(root, text = "Back", font=("arial", 15, "bold"), relief="sunken", bg="darkgreen",
                               fg="white", borderwidth=4, padx=2, pady=5, command = continue_profile)
        adminbackbtn.place(x=710, y=600)

#-----------------------------------------------------------------------Admin Sign Up//------------------------------------------------------------------------------------------------------------------------

    note = tk.Label(root, text="WELCOME", font=("arial", 30, "bold"), relief="solid",
                     bg="green", fg="white", borderwidth=10, padx=8, pady=20)
    note.place(x=320, y=0)
    note1 = tk.Label(root, text="STUDENT DASHBOARD", font=("arial", 20, "bold"), relief="solid",
                      bg="green", fg="white", borderwidth=7, padx=8, pady=20)
    note1.place(x=270, y=120)
    note2 = tk.Label(root, text="INTERNATIONAL SCHOOL", font=("arial", 20, "bold"), relief="solid",
                      bg="green", fg="white", borderwidth=7, padx=8, pady=20)
    note2.place(x=240, y=220)
    btnlogin = tk.Button(root, text = "LOG IN", font = ("arial", 15, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 8, padx = 5, pady = 15, command = login)
    btnlogin.place(x = 50, y = 550)
    btnsignin = tk.Button(root, text = "SIGN UP", font = ("arial", 15, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 8, padx = 5, pady = 15, command = signup)
    btnsignin.place(x = 710, y = 550)
    btnadminsignup = tk.Button(root, text = "ADMIN SIGN UP", font = ("arial", 15, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 8, padx = 5, pady = 15, command = adminsignup)
    btnadminsignup.place(x = 220, y = 550)
    btnadminlogin = tk.Button(root, text = "ADMIN LOG IN", font = ("arial", 15, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 8, padx = 5, pady = 15, command = adminlogin)
    btnadminlogin.place(x = 480, y = 550)



#-----------------------------------------------------------------------continue_profile//------------------------------------------------------------------------------------------------------------------------


continuebtn = tk.Button(root, text = "Continue", font = ("arial", 25, "bold"), relief = "groove", bg = "darkgreen", fg = "white", borderwidth = 8, padx = 5, pady = 15, command = continue_profile)
continuebtn.place(x = 710, y = 550)
root.mainloop()
