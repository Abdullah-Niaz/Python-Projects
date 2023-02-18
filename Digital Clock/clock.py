from tkinter import *
import datetime


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_zone.config(text=am)

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200, date_time)


clock = Tk()
clock.title(" Digital Clock ")
clock.geometry("1000x500")
clock.config(bg="yellow")

lab_hr = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_hr.place(x=40, y=40, height=110, width=100)
lab_hr_txt = Label(clock, text="Hr", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_hr_txt.place(x=40, y=170, height=60, width=100)


lab_min = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_min.place(x=220, y=40, height=110, width=100)

lab_min_txt = Label(clock, text="Min", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_min_txt.place(x=220, y=170, height=60, width=100)


lab_sec = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_sec.place(x=380, y=40, height=110, width=100)
lab_sec_txt = Label(clock, text="Sec", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_sec_txt.place(x=380, y=170, height=60, width=100)


lab_zone = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_zone.place(x=550, y=40, height=110, width=120)
lab_zone_txt = Label(clock, text="Am/Pm", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_zone_txt.place(x=550, y=170, height=60, width=120)


lab_date = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_date.place(x=40, y=300, height=110, width=100)
lab_date_txt = Label(clock, text="Date", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_date_txt.place(x=40, y=420, height=60, width=100)


lab_month = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_month.place(x=220, y=300, height=110, width=100)
lab_min_txt = Label(clock, text="Month", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_min_txt.place(x=220, y=420, height=60, width=100)


lab_year = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_year.place(x=380, y=300, height=110, width=100)
lab_year_txt = Label(clock, text="Year", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_year_txt.place(x=380, y=420, height=60, width=100)


lab_day = Label(clock, text="00", font=(
    'sans serif', 60, 'bold'), bg="green", fg="black")

lab_day.place(x=550, y=300, height=110, width=120)
lab_day_txt = Label(clock, text="Day", font=(
    'sans serif', 20, 'bold'), bg="green", fg="black")

lab_day_txt.place(x=550, y=420, height=60, width=120)


date_time()
clock.mainloop()
