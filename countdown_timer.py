# here I have created a countdown Time using Python standard libraries such as Tkinter and time module. 
#The basic functionality of this application is to run the timer for a given period of time.
from tkinter import *

import time

win = Tk()

win.geometry('700x350')

win.resizable(False, False)

win.config(bg='black')

sec = StringVar()
Entry(win, textvariable=sec, width=2,
   font='Verdana').place(x=380, y=120)
sec.set('00')

mins = StringVar()
Entry(win, textvariable=mins, width=2, font='Verdana').place(x=346, y=120)
mins.set('00')

hrs = StringVar()
Entry(win, textvariable=hrs, width=2, font='Verdana').place(x=310, y=120)
hrs.set('00')

def countdowntimer():
   times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
   while times > -1:
      minute, second = (times // 60, times % 60)
      hour = 0
      if minute > 60:
         hour, minute = (minute // 60, minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)

      win.update()
      time.sleep(1)
      if (times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times -= 1


Label(win, font=('Verdana bold', 22), text='Set the Timer', bg='skyblue4', fg="white").place(x=260, y=70)

Button(win, text='START', bd='2', bg='IndianRed1', font=('Verdana bold', 10), command=countdowntimer).place(x=335, y=180)

win.mainloop()
