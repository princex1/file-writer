from tkinter import *

root = Tk()
root.title("fill write")
root.geometry("500x500")

title = Label(text="fill write", font="had 15 bold").grid(pady=10, row=0, column=2)


def print1():
    user = user_val.get()
    pass_w = password_val.get()
    phone = phone_val.get()
    with open("1.txt", 'w') as fill:
        fill.write(f"user name = {user}, password = {pass_w}, phone = {phone}")
    # ans = int(user_val.get()) + int(phone_val.get())
    # Label(text=ans).grid(row=4, column=1).te
    print(user_val.get() + phone_val.get())


user_lab = Label(text="user name:").grid(row=1, column=1)
password_lab = Label(text="password:").grid(row=2, column=1)
phone_lab = Label(text="phone:").grid(row=3, column=1)

user_val = StringVar()
password_val = StringVar()
phone_val = StringVar()

user_enter = Entry(textvariable=user_val).grid(row=1, column=2)
password_enter = Entry(textvariable=password_val).grid(row=2, column=2)
phone_enter = Entry(textvariable=phone_val).grid(row=3, column=2)

print2 = Button(text="write", command=print1).grid(row=4, column=2, pady=13)


root.mainloop()
