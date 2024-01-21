from tkinter import *
import settings
import cal
from cell import Cell
root = Tk()

root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.title("Python Game")

top_frame = Frame(
    root,
    bg="black",
    height=cal.height_cal(25),
    width=cal.width_cal(100)
)
top_frame.place(x=0, y=0)

side_frame = Frame(
    root,
    bg="black",
    height=cal.height_cal(75),
    width=cal.width_cal(15)
)
side_frame.place(x=0, y=cal.height_cal(25))

center_frame = Frame(
    root,
    bg="black",
    height=cal.height_cal(75),
    width=cal.width_cal(85)
)
center_frame.place(x=cal.width_cal(15), y=cal.height_cal(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(y,x)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(column=x, row=y)

# Cell.create_cell_count_label(side_frame)
# Cell.cell_count_label_object.place(x=0, y=0)
Cell.random_mines()
# print(Cell.all_cells)
root.mainloop()
