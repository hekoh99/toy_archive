from tkinter import *

window = Tk()
window.title("test") # window name
window.geometry("410x410") # size of window
window.resizable(0, 0)

label = Label(window, text="test label", anchor=NW, bg="light green", fg="black")
label.pack()

window.mainloop()
