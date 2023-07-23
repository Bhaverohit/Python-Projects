# pip install speedtest-cli==2.1.3

from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / 1024 / 1024)) + " Mbps"
    up = str(round(sp.upload() / 1024 / 1024)) + " Mbps"

    label_down.config(text=down)
    label_up.config(text=up)


sp = Tk()

sp.title("Internet Speed Check Application")
sp.geometry("500x650")
sp.config(bg="Blue")

label = Label(sp, text="Internet Speed Check", font=("Times New Roman", 30, "bold"))
label.place(x=60, y=30, height=50, width=380)

label = Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"))
label.place(x=60, y=130, height=50, width=380)

label_down = Label(sp, text="00", font=("Times New Roman", 30, "bold"))
label_down.place(x=60, y=200, height=50, width=380)

label = Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"))
label.place(x=60, y=290, height=50, width=380)

label_up = Label(sp, text="00", font=("Times New Roman", 30, "bold"))
label_up.place(x=60, y=360, height=50, width=380)


button = Button(
    sp,
    text="Check Speed",
    font=("Times New Roman", 30, "bold"),
    relief=RAISED,
    bg="Black",
    fg="White",
    command=speedcheck,
)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
