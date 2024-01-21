from tkinter import Button, Label
import random
import settings
class Cell:
    all_cells = []
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_btn_obj = None
        Cell.all_cells.append(self)
    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=3,
        )
        btn.bind("<Button-1>", self.left_click_action)
        btn.bind("<Button-3>", self.right_click_action)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.mines_count == 0:
                self.show_cell()
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()
    
    def get_cell_by_axes(self, x, y):
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell 
            
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axes(self.x-1, self.y-1),
            self.get_cell_by_axes(self.x-1, self.y),
            self.get_cell_by_axes(self.x-1, self.y+1),
            self.get_cell_by_axes(self.x, self.y-1),
            self.get_cell_by_axes(self.x+1, self.y-1),
            self.get_cell_by_axes(self.x+1, self.y),
            self.get_cell_by_axes(self.x+1, self.y+1),
            self.get_cell_by_axes(self.x, self.y+1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def mines_count(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1
        return count

    def show_cell(self):
        self.cell_btn_obj.configure(bg="green", text=self.mines_count)

    def show_mine(self):
        self.cell_btn_obj.configure(bg="red")

    def right_click_action(self, event):
        print("Right click")
    

    @staticmethod
    def random_mines():
        mine_cells = random.sample(Cell.all_cells, settings.MINES_COUNT)
        for cell in mine_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y}, {self.is_mine})"
     