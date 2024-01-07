from tkinter import *
import settings
import cal

root = Tk()

root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.title("Python Game")

top_frame = Frame(
    root,
    bg="green",
    height=cal.height_cal(25),
    width=cal.width_cal(100)
)
top_frame.place(x=0, y=0)

side_frame = Frame(
    root,
    bg="red",
    height=cal.height_cal(75),
    width=cal.width_cal(15)
)
side_frame.place(x=0, y=cal.height_cal(25))


center_frame = Frame(
    root,
    bg="blue",
    height=cal.height_cal(75),
    width=cal.width_cal(85)
)
center_frame.place(x=cal.width_cal(15), y=cal.height_cal(25))

btn1 = Button(
    center_frame,
    bg="white",
    text="Click Me",
    font="arial 20 bold",
)

btn1.place(x=cal.width_cal(0), y=cal.height_cal(0))
root.mainloop()
