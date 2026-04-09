import random

cities = ['A','B','C','D','E','F','G','H']
dist = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

SIZE = 20
GENERATIONS = 200
MUTATION_RATE = 0.1


def cost(route):
    total = 0
    for i in range(len(route)-1):
        a=cities.index(route[i])
        b =cities.index(route[i+1])
        total+=dist[a][b]

    total+=dist[cities.index(route[-1])][cities.index(route[0])]
    return total


def random_route():
    r=cities[:]
    random.shuffle(r)
    return r


def mutate(route):
    if random.random() < MUTATION_RATE:
        i,j = random.sample(range(len(route)),2)
        route[i],route[j] = route[j],route[i]


def one_point_crossover(p1,p2):

    point=random.randint(1,len(p1)-2)
    child=p1[:point]
    for c in p2:
        if c not in child:
            child.append(c)

    return child


def two_point_crossover(p1,p2):
    a,b=sorted(random.sample(range(len(p1)),2))
    child=[None]*len(p1)
    child[a:b]=p1[a:b]
    pos=0

    for c in p2:
        if c not in child:
            while child[pos]!=None:
                pos += 1
            child[pos]=c

    return child


def genetic_algorithm(crossover_type):
    population=[random_route() for _ in range(SIZE)]
    for gen in range(GENERATIONS):
        population.sort(key=cost)
        new_pop=population[:5]

        while len(new_pop) < SIZE:
            p1,p2=random.sample(population[:10],2)
            if crossover_type==1:
                child=one_point_crossover(p1,p2)
            else:
                child=two_point_crossover(p1,p2)
            mutate(child)

            new_pop.append(child)

        population=new_pop

    population.sort(key=cost)

    return population[0], cost(population[0])


print("One Point Crossover")
best,c = genetic_algorithm(1)
print(best,"Cost =",c)

print("\nTwo Point Crossover")
best,c = genetic_algorithm(2)
print(best,"Cost =",c)