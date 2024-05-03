import tkinter as tk
import tkinter.font as font
import datetime


app_windows = tk.Tk()
app_windows.iconbitmap("clock.ico")
app_windows.title("Digital Clock")
app_windows.geometry("300x200")
app_windows.resizable(1,1)
app_windows.config(bg="black")

text_font = font.Font(family="Helvetica", size=50, weight="bold")
background = "#000000"
foreground = "#ffffff"
border_width = 25
border_shadow = "black"



label = tk.Label(app_windows, font=text_font, bg=background, fg=foreground)
label.grid(row=0, column=1, padx=10, pady=30)

def digital_clock():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    label.config(text=time)
    label.after(200, digital_clock)

digital_clock()





app_windows.mainloop()