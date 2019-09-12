from board import Board
import copy
import numpy as np

class Hill_Climb:
    def __init__(self):
        self.no_steps = 0

    def solve_board(self, board):
        best_board = Board(len(board.get_map()))
        q_list = [board.find_q()[k][1] for k in range(len(board.get_map()))]
        best_board.set_queens_from_list(q_list)
        iterations = 0
        while best_board.get_h(best_board.find_q()) != 0 and iterations < 3125:
            q_pos = best_board.find_q()
            for i in range(len(q_pos)):
                queen = best_board.find_q()[i]
                comp = []
                for j in range(1, 5):
                    temp_board = copy.deepcopy(best_board)
                    temp_board.move_queen(queen, j)
                    comp.append(temp_board.get_h(temp_board.find_q()))
                best_board.move_queen(queen, comp.index(min(comp)) + 1)
                self.no_steps += 1
                if best_board.get_h(best_board.find_q()) == 0:
                    break
            iterations += 1
        print("Number of Steps: ", self.no_steps)
        print("Number of attacking pairs:", best_board.get_h(best_board.find_q()))
        return best_board


if __name__ == '__main__':
    brd = Board(5)
    brd.set_queens()
    f = brd.fitness()
    brd.show()
    print("Number of attacking pairs:", brd.get_h(brd.find_q()))
    print("==================================================================")
    HillClimb = Hill_Climb()
    solved_board = HillClimb.solve_board(brd)
    solved_board.fitness()
    solved_board.show()
