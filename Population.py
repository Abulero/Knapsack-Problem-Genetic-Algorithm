from Individual import Individual
import random


class Population:
    def __init__(self, **kwargs):
        self.size = kwargs["size"]
        self.population = []
        self.blocks = ((1, 1), (2, 1), (2, 2), (4, 12), (10, 4))
        self.capacity = 15
        self.mutation_chance = 10

        self.Generate()

    def Generate(self):
        for pop in range(self.size):
            individual = Individual()

            while individual.weight == 0 or individual.weight >= 15:
                individual.Create(self.blocks)

            self.population.append(individual)

    def Show(self):
        print('Current population:\nStrongest: {}'.format(self.Strongest()))

        for individual in self.population:
            spaces_1 = ''
            spaces_2 = ''

            if individual.fitness < 10:
                spaces_1 = '  '
            elif individual.fitness >= 10 and individual.fitness < 100:
                spaces_1 = ' '

            if individual.weight < 10:
                spaces_2 = '  '
            elif individual.weight >= 10 and individual.weight < 100:
                spaces_2 = ' '

            solution = ''
            i = 0
            for block in self.blocks:
                solution += '{} x {}$/{}kg, '.format(individual.solution[i], block[0], block[1])

                i += 1

            solution = solution[:-2]

            print('Fitness: {}{} | Weight: {}{} | Solution: {}'.format(individual.fitness, spaces_1, individual.weight, spaces_2, solution))

        print()

    def Evolve(self, **kwargs):
        generations = kwargs["generations"]
        crossover_flag = kwargs["crossover"]
        mutation_flag = kwargs["mutation"]

        for generation in range(generations):
            self.Procriation()

            if mutation_flag:
                self.Mutation()

            if crossover_flag:
                self.Crossover()

            self.Survival_Of_The_Fittest()

    def Procriation(self):
        for individual in range(int(self.size/2)):
            ind_1 = random.randint(0, self.size-1)
            ind_2 = random.randint(0, self.size-1)

            while ind_2 == ind_1:
                ind_2 = random.randint(0, self.size-1)

            newborn = Individual()
            newborn.Birth(self.population[ind_1], self.population[ind_2], self.blocks, self.capacity)

            self.population.append(newborn)

    def Mutation(self):
        for individual in self.population:
            dice_roll = random.randint(1, 100)

            if dice_roll >= 0 and dice_roll < self.mutation_chance:
                attribute = random.randint(0, len(self.blocks)-1)
                change = random.randint(0, 1)

                if change == 0:
                    individual.ChangeAttribute(self.blocks, self.capacity, attribute, 1)
                else:
                    individual.ChangeAttribute(self.blocks, self.capacity, attribute, -1)

    def Crossover(self):
        pass

    def Survival_Of_The_Fittest(self):
        while len(self.population) > self.size:
            self.population.pop(self.Weakest())

    def Weakest(self):
        i = 0
        weakest = 0
        fitness = self.population[0].fitness

        for individual in self.population:
            if individual.fitness < fitness:
                weakest = i

            i += 1

        return weakest

    def Strongest(self):
        fitness = self.population[0].fitness
        strongest = fitness

        for individual in self.population:
            if individual.fitness > fitness:
                strongest = individual.fitness

        return strongest

