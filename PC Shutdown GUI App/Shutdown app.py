from tkinter import *
import os


# Defining functions to shutdown/restart

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")



# Making GUI


screen = Tk()

screen.title("Shutdown App")
screen.geometry("500x500")
screen.config(bg="grey")


restart_button = Button(screen, text="Restart", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="hand2", command=restart)
restart_button.place(x=150, y=60, height=50, width=200)

restart_time_button = Button(screen, text="Restart Time", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="hand2", command=restart_time)
restart_time_button.place(x=150, y=170, height=50, width=200)

logout_button = Button(screen, text="Log Out", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="hand2", command=logout)
logout_button.place(x=150, y=270, height=50, width=200)

shutdown_button = Button(screen, text="Shutdown", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="hand2", command=shutdown)
shutdown_button.place(x=150, y=370, height=50, width=200)


screen.mainloop()