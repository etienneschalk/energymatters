

class Controller:
    def __init__(self, map):
        self.map = map 

        self.selected_cell = None 



    # def position_cursor(self, pos):
    #     if (pos[0] < 0 or pos[0] >= self.map.width * 2 or pos[1] < 0 or pos[1] > self.map.height):
    #         return
    #     self.cursor_coord = pos

    # def select_cell(self, pos):
    #     if (pos[0] < 0 or pos[0] >= self.map.width or pos[1] < 0 or pos[1] > self.map.height):
    #         return
    #     self.selected_cell_coord = (pos[0], pos[1])
    #     # self.selected_cell = self.map.array[pos[0]][pos[1]]

    # def rotate_cell(self, pos):
    #     if (pos[0] < 0 or pos[0] >= self.map.width or pos[1] < 0 or pos[1] > self.map.height):
    #         return
    #     self.map.rotate_anti_clockwise(pos[0], pos[1])
    #     # self.selected_cell.rotate_anti_clockwise()

    # # replace the selected cell by a new one
    # def change_cell(self, type):
    #     self.map.change_block(
    #         self.selected_cell_coord[0], self.selected_cell_coord[1], type)

    # # </To be moved in a controller>
