from Population import Population


if __name__ == "__main__":
    pop = Population(size=1000)
    pop.show()
    pop.evolve(generations=250, mutation=True)
    pop.show()