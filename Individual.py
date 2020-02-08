import random


class Individual:
    def __init__(self):
        self.fitness = 0
        self.weight = 0
        self.solution = [0, 0, 0, 0, 0]

    def create(self, blocks):
        self.solution.clear()

        for block in blocks:
            quantity = random.randint(0, 15)

            self.solution.append(quantity)

        self.correct_fitness_weight(blocks)

    def birth(self, individual_1, individual_2, blocks, capacity):
        i = 0
        for block in blocks:
            gene_transfer = random.randint(0, 1)

            if gene_transfer == 0:
                self.solution[i] = individual_1.solution[i]
            else:
                self.solution[i] = individual_2.solution[i]

            i += 1

        self.correct_fitness_weight(blocks)

        while self.weight > capacity:
            attribute = random.randint(0, len(blocks) - 1)

            while self.solution[attribute] == 0:
                attribute = random.randint(0, len(blocks) - 1)

            self.change_attribute(blocks, capacity, attribute, -1, once=True)

    def correct_fitness_weight(self, blocks):
        self.fitness = 0
        self.weight = 0

        i = 0
        for attribute in self.solution:
            self.fitness += blocks[i][0] * attribute
            self.weight += blocks[i][1] * attribute

            i += 1

    def change_attribute(self, blocks, capacity, attribute, number, **kwargs):
        once = kwargs["once"]

        self.solution[attribute] += number
        self.correct_fitness_weight(blocks)

        if self.weight > capacity:
            if not once:
                self.change_attribute(blocks, capacity, attribute, -1, once=False)
        elif self.solution[attribute] < 0:
            if not once:
                self.change_attribute(blocks, capacity, attribute, 1, once=False)
