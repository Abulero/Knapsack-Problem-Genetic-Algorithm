from Individual import Individual
import random


class Population:
    def __init__(self, **kwargs):
        self.size = kwargs["size"]
        self.population = []
        self.blocks = ((1, 1), (2, 1), (2, 2), (4, 12), (10, 4))
        self.capacity = 15

        self.Generate()

    def Generate(self):
        for pop in range(self.size):
            individual = Individual()

            while individual.weight == 0 or individual.weight >= 15:
                individual.Create(self.blocks)

            self.population.append(individual)

    def Show(self):
        print('Current population:\n')

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

    def Evolve(self, **kwargs):
        generations = kwargs["generations"]
        crossover_flag = kwargs["crossover"]

        for generation in range(generations):
            self.Procriation()
            self.SurvivalOfTheFittest()

    def Procriation(self):
        for individual in self.size/2:
            ind_1 = random.randint(self.size)
            ind_2 = random.randint(self.size)

            while ind_2 == ind_1:
                ind_2 = random.randint(self.size)

            newborn = Individual.Birth(self.population[ind_1], self.population[ind_2])
            self.population.append(newborn)

    def Survival_Of_The_Fittest(self):
        pass

