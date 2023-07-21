from tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("Live Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "black"
foreground= "green"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def live_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, live_clock)

live_clock()
app_window.mainloop()

