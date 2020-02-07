from Population import Population


if __name__ == "__main__":
    pop = Population(size=100)
    pop.Show()
    pop.Evolve(generations=250, mutation=True, crossover=False)
    pop.Show()