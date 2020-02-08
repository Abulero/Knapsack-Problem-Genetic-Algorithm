# Knapsack-Problem-Genetic-Algorithm
Solving the knapsack problem using a genetic algorithm made in python3, allowing for the code to be used as a simple genetic algorithm playground.

# Knapsack Problem
See:
https://en.wikipedia.org/wiki/Knapsack_problem

# Genetic algorithm fundamentals
Throughout the code and the explanation below, you will find the following terms: individual, population, generation and fitness.

Population is a group of individuals, and generations are the iterations of populations over time. Fitness, on the other hand, is a way to quantify how fit an individual is in its environment.

For the purpose of this algorithm, fitness will be the added weight of the blocks inside the knapsack, as it represents how good the solution is.

As for the individuals, each will be a solution to the problem.

# How does the playground work?
You can tinker with the following parameters:

Population size
Number of generations
Mutation (yes or no)
Crossover (yes or no)

It is interesting to use the flags to show how important mutation and crossover are for the population to reach maximum fitness quickly or even at all.

# Population size and number of generations
Population size and the number of generations with both (each in their own way) increase the number of gene exchanges, mutations and overall computational time required for the simulation to end. It is imperative for these numbers to be high enough for the population to reach optimal fitness.

# Mutation
Mutation is one of the most importante aspects of the genetic algorithm, and of genetics as a whole. It's the concept of genes randomly changing after a new individual receives genes froms its parents, making it slightly different.

# Why is mutation important?
Without it, the population may lean towards a local peak of fitness, instead of the global one (see image below).

![Fitness Mountain](/images/mountain_peaks.jpg)

Imagine the fitness of an individual is represented by the height of a mountain, as the one above. New generations, thanks to natural selection, tend to reach a peak and not leave it, as either sides of it mean a decrease in fitness. Therefore, it is possible for evolution to drive a species towards a local peak, leaving it oblivious to the higher summit right next to it.
Mutation allows some individuals to escape the local peak and allow for evolution to find new ones, until it reaches the global apex.

# Crossover
[COMING SOON]
