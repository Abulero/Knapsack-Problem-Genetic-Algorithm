# Author:
# André Gomes Cecchi
#
# Objective:
# Easily understand the fundamentals of a genetic algorithm and how useful it can be

from Population import Population


if __name__ == "__main__":
    pop = Population(size=10, knapsack_capacity=15, blocks=((1, 1), (2, 1), (2, 2), (4, 12), (10, 4)))
    pop.show()
    pop.evolve(generations=50, mutation=True)
    pop.show()