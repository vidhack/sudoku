
from collections import defaultdict
import itertools


class Sudoku:

    def __init__(self):
        self.row_string = '123456789'
        self.col_string = 'ABCDEFGHI'
        choice = set(range(1, 10))
        [setattr(self, each_col + each_row, choice)
         for each_row in self.row_string for each_col in self.col_string]
        self._init_row()
        self._init_col()
        self._init_grid()

    def _init_row(self):
        self.row = defaultdict(dict)
        for each_row in self.row_string:
            for each_col in self.col_string:
                self.row[each_row][each_col +
                                   each_row] = getattr(self, each_col + each_row)

    def _init_col(self):
        self.col = defaultdict(dict)
        for each_col in self.col_string:
            for each_row in self.row_string:
                self.col[each_col][each_col +
                                   each_row] = getattr(self, each_col + each_row)

    def _init_grid(self):
        self.grid = defaultdict(set)
        split_string = lambda x, n: [x[i:i + n] for i in range(0, len(x), n)]
        col_group = split_string(self.col_string, 3)
        row_group = split_string(self.row_string, 3)
        for each_grid in range(1, 10):
            row_group_no = (each_grid - 1) / 3
            col_group_no = (each_grid - 1) % 3
            grid_col = col_group[col_group_no]
            grid_row = row_group[row_group_no]
            grid_cell = set(["".join(each_cell)
                             for each_cell in itertools.product(grid_col, grid_row)])
            self.grid[each_grid] = grid_cell

    def draw_sudoku(self):
        for each_col in self.col_string:
            print each_col,
        print '\n'
        for each_row in self.row:
            for each_col in self.col:
                cell_options =  getattr(self, each_col + each_row)
                print "".join([str(each) for each in cell_options]),
            print '\n'


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.draw_sudoku()
