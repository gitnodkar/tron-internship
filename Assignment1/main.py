import tkinter as ui
import time

window = ui.Tk()
digital_clock_lbl = ui.Label(window, text="00:00:00", font="Calibri 72")
digital_clock_lbl.pack()

def update_clock():
    time_text = time.strftime("%H:%M:%S")
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)

update_clock()
window.mainloop()
