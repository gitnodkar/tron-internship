import tkinter as ui
import time
import math

window = ui.Tk()
window.geometry("400x400")

def update_clock():
    hours, minutes, seconds = map(int, time.strftime("%I %M %S").split())

    update_hand(seconds_hand, seconds_hand_len, seconds * 6)
    update_hand(minutes_hand, minutes_hand_len, minutes * 6)
    update_hand(hours_hand, hours_hand_len, hours * 30 + 0.5 * minutes + 0.008 * seconds)

    window.after(1000, update_clock)

def update_hand(hand, length, angle_degrees):
    x = length * math.sin(math.radians(angle_degrees)) + center_x
    y = -1 * length * math.cos(math.radians(angle_degrees)) + center_y
    canvas.coords(hand, center_x, center_y, x, y)

canvas = ui.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill='both')

# create background
bg = ui.PhotoImage(file='dial_400.png')
canvas.create_image(200, 200, image=bg)

# create clock hands
center_x, center_y = 200, 200
seconds_hand_len, minutes_hand_len, hours_hand_len = 95, 80, 60

seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='blue')
minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='white')
hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='white')

update_clock()

window.mainloop()