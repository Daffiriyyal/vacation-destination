from cProfile import label
from tkinter import *
from tkinter import messagebox

def login():
    name = txt_user.get()
    password = txt_pass.get()
    sukses = False
    file = open("logindatabase.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            sukses = True
            break
    file.close()
    if(sukses):
        messagebox.showinfo("", "Anda berhasil login! Silahkan masuk")
        root.destroy()
    else:
        messagebox.showinfo("", "Username atau password anda salah, harap coba lagi!")

root = Tk()
root.geometry("1050x730+100+50")
root.title("REGISTER DAN LOGIN")
root.bg = PhotoImage(file = 'gambar3.png')
Label(root, image = root.bg).place(x = 50, y= 20)

frame_login = Frame(root, bg = "purple")
frame_login.place(x = 280, y = 200, height = 340, width = 500)

judul = Label(frame_login,
        text = "SILAHKAN LOGIN",
        font=("calibri", 30),
        fg = "#d77337", bg = "purple").place(x=130, y=30)

label_user = Label(frame_login, text = "Username",
            font = ("calibri", 15, "bold"),
            fg = "black", bg = "purple").place(x = 80, y = 100)
txt_user = Entry(frame_login,
            font = ("calibri", 15),
            bg = "lightgray").place(x=80, y=130, width=350, height=35)
        
label_password = Label(frame_login, text = "Password",
                font = ("calibri", 15, "bold"),
                fg = "black", bg = "purple").place(x = 80, y = 170)
txt_password = Entry(frame_login,
                font = ("calibri", 15),
                bg = "lightgray").place(x=80, y=200, width=350, height=35)

login_btn = Button(frame_login, command=login, text = "Login",
            fg = "#d77337", font = ("calibri", 10, "bold")).place(x = 350, y = 250)

root.mainloop()