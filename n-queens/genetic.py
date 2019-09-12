from board import Board
import numpy as np
import random
import copy


class Genetic:
    def __init__(self):
        self.no_steps = 0

    def selection(self, population):
        pop_fit = [0 for j in range(len(population))]
        for i, gene in enumerate(population):
            temp_board = Board(5)
            temp_board.set_queens_from_list(gene)
            temp_board_fit = temp_board.fitness()
            pop_fit[i] = temp_board_fit
        try:
            pop_fit = [x / sum(pop_fit) for x in pop_fit]
        except:
            print(" Please run the program again. The population can't be evolved further!")
        random_gene = list(np.random.choice(np.arange(len(pop_fit)), 4, p=pop_fit))
        next_pop = [population[g] for g in random_gene]
        return next_pop

    def crossover(self, population):
        crossover_pos = random.randint(0, len(population[0])-1)
        next_pop=[]
        for i in range(0, len(population[0])-1, 2):
            parents = copy.deepcopy(population[i:i+2])
            temp = parents[0][crossover_pos:]
            parents[0][crossover_pos:] = parents[1][crossover_pos:]
            parents[1][crossover_pos:] = temp
            next_pop.append(parents[0])
            next_pop.append(parents[1])
        return next_pop

    def mutation(self, population, mutation_rate):
        next_pop = []
        for gene in population:
            mutate = bool(np.random.choice([True, False], 1, p=[mutation_rate, 1-mutation_rate]))
            if mutate:
                mutate_pos = random.randint(0, len(population[0]) - 1)
                gene[mutate_pos] = random.randint(0, len(population[0])-1)
                next_pop.append(gene)
            else:
                next_pop.append(gene)
        return next_pop

    def best_fitness(self, population):
        pop_fit = [0 for j in range(len(population))]
        for i, gene in enumerate(population):
            temp_board = Board(5)
            temp_board.set_queens_from_list(gene)
            temp_board_fit = temp_board.fitness()
            pop_fit[i] = temp_board_fit
        return min(pop_fit)

    def solve_board(self, board):
        pop = board.init_pop()
        while self.best_fitness(pop) < 10:
            pop = self.selection(pop)
            pop = self.crossover(pop)
            pop = self.mutation(pop, 0.5)
        pop_fit = [0 for k in range(len(pop))]

        for i, gene in enumerate(pop):
            temp_board = Board(5)
            temp_board.set_queens_from_list(gene)
            temp_board_fit = temp_board.fitness()
            pop_fit[i] = temp_board_fit

        solved_board = Board(5)
        solved_board.set_queens_from_list(pop[pop_fit.index(10)])
        # Find number of steps
        init_q = [board.find_q()[k][1] for k in range(len(pop[0]))]
        ans_q = [solved_board.find_q()[m][1] for m in range(len(pop[0]))]
        for i in range(len(init_q)):
            if init_q[i] != ans_q[i]:
                self.no_steps += 1
        print("Number of steps: ", self.no_steps)
        return solved_board


if __name__ == '__main__':
    brd = Board(5)
    brd.set_queens()
    brd.fitness()
    brd.show()
    print("======================================================")
    GA = Genetic()
    ans = GA.solve_board(brd)
    ans.fitness()
    ans.show()



