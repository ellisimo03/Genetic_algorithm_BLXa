from DemandPrediction import DemandPrediction
import random
import time
import pandas as pd

import sys

from DemandPrediction import DemandPrediction
import random
import time
import pandas as pd
import sys

random.seed(10)

populationSize = 100
NoOfGenerations = 2000
mutationIndex = 0.1
NoOfGenerationsWithoutImprovingMax = 500
NoOfGenerationsWithoutImproving = 0
population = []
fitness = []
crossoverRate = 0.9
bestSoFar = None
improving = True
initialTime = 0.0
bestTime = 0.0


training_problem = DemandPrediction("train")
test_problem  = DemandPrediction("test")

def random_parameters():
    b = DemandPrediction.bounds()  
    return [low + random.random()*(high-low) for [high, low] in b]

def initPopulation():
    global population, fitness, bestSoFar, bestError ,improving, NoOfGenerationsWithoutImproving ,initialTime, bestTime

    initialTime = time.perf_counter()
    bestTime = 0.0
    population = [random_parameters() for _ in range(populationSize)]
    fitness = [0.0] * populationSize
    bestSoFar = None
    bestError = 1e309
    improving = True
    NoOfGenerationsWithoutImproving = 0

def calculateFitness():
    global fitness, bestError, bestSoFar, bestTime, NoOfGenerationsWithoutImproving, improving

    previousBest = bestError
    improved = False

    for i in range(populationSize):
        individualChromo = population[i]
        error = training_problem.evaluate(individualChromo)
        if error < bestError:
            bestError = error
            bestSoFar = individualChromo[:]
            bestTime = time.perf_counter() - initialTime
            improved = True
        fitness[i] = 1.0 / (error + 1.0)

    if not improved:
        NoOfGenerationsWithoutImproving += 1
        if NoOfGenerationsWithoutImproving >= NoOfGenerationsWithoutImprovingMax:
            improving = False
    else:
        NoOfGenerationsWithoutImproving = 0

def normaliseFitness():
    global fitness
    total = 0.0
    for i in range(populationSize):
        total += fitness[i]

    if total == 0.0:
        return

    for i in range(populationSize):
        fitness[i] = fitness[i] / total

def selectParent():
    R = random.random()
    index = 0

    while R > 0 and index < populationSize:
        R -= fitness[index]
        index += 1

    index -= 1

    if index < 0:
        index = 0

    individualChromo = population[index][:]
    return individualChromo

def crossoverBaseline(parent1, parent2):
    child = parent1[:]
    for i in range(len(child)):
        child[i] = 0.5 * parent1[i] + 0.5 * parent2[i]
    return child

def mutate(individualChromo):
    step_size = 1.0

    for i in range(len(individualChromo)):
        rndom = random.random()
        if rndom < mutationIndex:
            individualChromo[i] += random.uniform(-step_size, step_size)
    return individualChromo

def nextGeneration():
    global population
    newPopulation = [None] * populationSize

    for i in range(populationSize):
        parent1 = selectParent()
        parent2 = selectParent()
        R = random.random()
        if R < crossoverRate:
            child = crossoverBaseline(parent1, parent2)
        else:
            child = parent1[:]
        child = mutate(child)
        newPopulation[i] = child

    population = newPopulation

def runGA():
    global improving
    initPopulation()
    generation = 0

    while generation < NoOfGenerations and improving:
        calculateFitness()
        normaliseFitness()
        nextGeneration()
        generation += 1

    calculateFitness() # to keep bestError up to date
    return generation

if __name__ == "__main__":
    gens = runGA()

    print("Generations:", gens)
    print("Best training error (MAE):", bestError)
    print("Time when best solution was found:", round(bestTime, 3))

    testError = test_problem.evaluate(bestSoFar)
    print("MAE of best test solution:", testError)
