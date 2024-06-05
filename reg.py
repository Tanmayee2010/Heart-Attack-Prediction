from tkinter import *
from tkinter import messagebox
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("New User Registration")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False, False)

def register():
    username = user.get()
    password = code.get()
    admincode = adminaccess.get()

    if admincode == "9955":
        if (username == "" or username == "UserID") or (password == "" or password == "Password"):
            messagebox.showerror("Entry error", "Type username or password!!")
        else:
            try:
                mydb = mysql.connector.connect(
                    host='localhost',
                    user='tanu',
                    password="tanu1620"
                )
                mycursor = mydb.cursor()
                mycursor.execute("CREATE DATABASE IF NOT EXISTS patientregistration")
                mycursor.execute("USE patientregistration")
                mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS login (
                        user INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                        Username VARCHAR(50),
                        Password VARCHAR(100)
                    )
                """)
                command = "INSERT INTO login (Username, Password) VALUES (%s, %s)"
                mycursor.execute(command, (username, password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Register", "New User added successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
    else:
        messagebox.showerror("Admin code!", "Input Correct Admin code to add new user!!")

# Define the login function if necessary
def login():
    pass

# Icon image
image_icon = PhotoImage(file="import your icon.png path")
root.iconphoto(False, image_icon)

# Background image
frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="import your register.png path")
Label(frame, image=backgroundimage).pack()

adminaccess = Entry(frame, width=15, fg="#000", border=0, bg="#e8ecf7", font=("Arial Bold", 20))
adminaccess.focus()
adminaccess.place(x=550, y=280)

# User entry
def user_enter(e):
    user.delete(0, "end")

def user_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "UserID")

user = Entry(frame, width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold", 20))
user.insert(0, "UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=370)

# Password entry
def password_enter(e):
    code.delete(0, "end")

def password_leave(e):
    if code.get() == "":
        code.insert(0, "Password")

code = Entry(frame, width=18, fg="#fff", bg="#375174", border=0, font=("Arial Bold", 20))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500, y=470)

button_mode = True
def hide():
    global button_mode

    if button_mode:
        eyebutton.config(image=closeeye, activebackground="white")
        code.config(show="*")
        button_mode = False
    else:
        eyebutton.config(image=openeye, activebackground="white")
        code.config(show="")
        button_mode = True

openeye = PhotoImage(file="import your openeye.png path")
closeeye = PhotoImage(file="import your close eye.png path")
eyebutton = Button(frame, image=openeye, bg="#375174", bd=0, command=hide)
eyebutton.place(x=780, y=470)



regis_button = Button(root, text="ADD NEW USER", bg="#455c88", fg="white", width=13, height=1, font=("arial", 16, "bold"), bd=0, command=register)
regis_button.place(x=530, y=650)



root.mainloop()
