from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    ampm = time.strftime("%p")

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    hour_label.config(text=hr)
    minute_label.config(text=min)
    second_label.config(text=sec)
    AMPM_label.config(text=ampm)


    date_label.config(text=date)
    month_label.config(text=month)
    year_label.config(text=year)
    day_label.config(text=day)


    # Auto changing time
    hour_label.after(200, date_time)



clock = Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg="yellow")


hour_label = Label(clock, text="00", font=("Times New Roman", 60, "bold"), bg="Red", fg="white")
hour_label.place(x=120, y=50, height=110, width=100)

text_hour_label = Label(clock, text="Hour", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_hour_label.place(x=120, y=190, height=40, width=100)


minute_label = Label(clock, text="00", font=("Times New Roman", 60, "bold"), bg="Red", fg="white")
minute_label.place(x=340, y=50, height=110, width=100)

text_minute_label = Label(clock, text="Minute", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_minute_label.place(x=340, y=190, height=40, width=100)

second_label = Label(clock, text="00", font=("Times New Roman", 60, "bold"), bg="Red", fg="white")
second_label.place(x=560, y=50, height=110, width=100)

text_second_label = Label(clock, text="Second", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_second_label.place(x=560, y=190, height=40, width=100)


AMPM_label = Label(clock, text="00", font=("Times New Roman", 50, "bold"), bg="Red", fg="white")
AMPM_label.place(x=780, y=50, height=110, width=100)

text_AMPM_label = Label(clock, text="AM/PM", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_AMPM_label.place(x=780, y=190, height=40, width=100)











date_label = Label(clock, text="00", font=("Times New Roman", 60, "bold"), bg="Red", fg="white")
date_label.place(x=120, y=270, height=110, width=100)

text_date_label = Label(clock, text="Date", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_date_label.place(x=120, y=410, height=40, width=100)


month_label = Label(clock, text="00", font=("Times New Roman", 60, "bold"), bg="Red", fg="white")
month_label.place(x=340, y=270, height=110, width=100)

text_month_label = Label(clock, text="Month", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_month_label.place(x=340, y=410, height=40, width=100)


year_label = Label(clock, text="00", font=("Times New Roman", 60, "bold"), bg="Red", fg="white")
year_label.place(x=560, y=270, height=110, width=100)

text_year_label = Label(clock, text="Year", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_year_label.place(x=560, y=410, height=40, width=100)


day_label = Label(clock, text="00", font=("Times New Roman", 45, "bold"), bg="Red", fg="white")
day_label.place(x=780, y=270, height=110, width=100)

text_day_label = Label(clock, text="Day", font=("Times New Roman", 20, "bold"), bg="Red", fg="white")
text_day_label.place(x=780, y=410, height=40, width=100)



date_time()

clock.mainloop()