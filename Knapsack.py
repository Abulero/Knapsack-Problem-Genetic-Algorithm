from Population import Population


if __name__ == "__main__":
    pop = Population(size=250)
    pop.Show()
    pop.Evolve(generations=1000, crossover=False)
    pop.Show()