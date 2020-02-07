import random


class Individual:
    def __init__(self):
        self.fitness = 0
        self.weight = 0
        self.solution = [0, 0, 0, 0, 0]

    def Create(self, blocks):
        self.solution.clear()

        for block in blocks:
            quantity = random.randint(0, 15)

            self.solution.append(quantity)

        self.CorrectFitnessWeight(blocks)

    def Birth(self, individual_1, individual_2, blocks, capacity):
        i = 0
        for block in blocks:
            gene_transfer = random.randint(0, 1)

            if gene_transfer == 0:
                self.solution[i] = individual_1.solution[i]
            else:
                self.solution[i] = individual_2.solution[i]

            i += 1

        self.CorrectFitnessWeight(blocks)

        while self.weight > capacity:
            attribute = random.randint(0, len(blocks) - 1)

            while self.solution[attribute] == 0:
                attribute = random.randint(0, len(blocks) - 1)

            self.ChangeAttribute(blocks, capacity, attribute, -1)

    def CorrectFitnessWeight(self, blocks):
        self.fitness = 0
        self.weight = 0

        i = 0
        for attribute in self.solution:
            self.fitness += blocks[i][0] * attribute
            self.weight += blocks[i][1] * attribute

            i += 1

    def ChangeAttribute(self, blocks, capacity, attribute, number):
        self.solution[attribute] += number

        self.CorrectFitnessWeight(blocks)

        if self.weight > capacity:
            self.ChangeAttribute(blocks, capacity, attribute, -1)
        elif self.solution[attribute] < 0:
            self.ChangeAttribute(blocks, capacity, attribute, 1)
