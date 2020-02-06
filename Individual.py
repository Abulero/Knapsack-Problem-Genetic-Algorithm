import random


class Individual:
    def __init__(self):
        self.fitness = 0
        self.weight = 0
        self.solution = [0, 0, 0, 0, 0]

    def Create(self, blocks):
        self.solution.clear()
        self.fitness = 0
        self.weight = 0

        for block in blocks:
            quantity = random.randint(0, 15)

            self.solution.append(quantity)
            self.fitness += block[0] * quantity
            self.weight += block[1] * quantity

    @staticmethod
    def Birth(individual_1, individual_2, blocks):
        newborn = Individual()

        i = 0
        for block in blocks:
            gene_transfer = random.randint(0, 1)

            if gene_transfer == 0:
                newborn.solution[i] = individual_1.solution[i]
            else:
                newborn.solution[i] = individual_2.solution[i]

            newborn.fitness += block[0] * newborn.solution[i]
            newborn.weight += block[1] * newborn.solution[i]

            i += 1

        return newborn
