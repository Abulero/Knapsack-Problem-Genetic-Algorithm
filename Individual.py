import random


class Individual:
    def __init__(self):
        self.fitness = 0
        self.weight = 0
        self.solution = []

    def Create(self, blocks):
        self.solution.clear()
        self.fitness = 0
        self.weight = 0

        for block in blocks:
            quantity = random.randint(0, 16)

            self.solution.append(quantity)
            self.fitness += block[0] * quantity
            self.weight += block[1] * quantity

    @staticmethod
    def Birth(individual_1, individual_2):
        newborn = Individual()

        i = 0
        for number in individual_1.solution:
            gene_transfer = random.randint(0, 2)

            if gene_transfer == 0:
                newborn.solution[i] = individual_1.solution[i]
            else:
                newborn.solution[i] = individual_2.solution[i]

            i += 1

        return newborn
