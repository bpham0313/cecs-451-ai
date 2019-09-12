import random
import numpy as np
from random import shuffle


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = n * (n-1) // 2

    def set_queens(self):
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def get_map(self):
        return self.map

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ", self.fit)

# ===================================== Hill Climb =========================================================
    def find_q(self):
        m = self.map
        ans = []
        for i in range(0, self.n_queen):
            for j in range(0, self.n_queen):
                if m[i][j] == 1:
                    ans.append([i, j])
        return ans

    def get_h(self, queen_positions):  # Get attacking pairs as heuristic function
        pos = queen_positions
        conf = [0]*self.n_queen
        for j in range(len(pos[0])):
            for i in range(len(pos)):
                temp = pos[i][j]
                for k in range(self.n_queen):
                    if temp == pos[k][j]:
                        conf[i] += 1
        conf[:] = [x - 2 for x in conf]
        for count, i in enumerate(pos,0):
            for j in pos:
                if abs(j[0]-i[0]) == abs(j[1]-i[1]):
                    conf[count] += 1
        conf[:] = [x - 1 for x in conf]
        cost = int(sum(conf)/2)
        return cost

    def move_queen(self, queen_position, pos):
        p = queen_position
        temp = self.map[p[0]][(p[1]+pos) % 5]
        self.map[p[0]][(p[1] + pos) % 5] = self.map[p[0]][p[1]]
        self.map[p[0]][p[1]] = temp

# ===================================== Genetic Algorithm =========================================================
    def init_pop(self):
        population = []
        for i in range(4):
            gene = list(range(5))
            shuffle(gene)
            population.append(gene)
        return population

    def set_queens_from_list(self, queenlist):
        for i, q_pos in enumerate(queenlist):
            self.map[i][q_pos] = 1

    def fitness(self):  # Non-attacking pairs
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit -= 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit -= 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit -= 1
        return self.fit


if __name__ == '__main__':
    test = Board(5)
    test.set_queens()
    test.fitness()
    test.show()
    pop = test.init_pop()
    print(np.matrix(pop))
    test1 = Board(5)
    test1.set_queens_from_list(pop[1])
    test1.show()



