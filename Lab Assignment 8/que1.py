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

def generate_random_state(existing):
    state = cities[1:]         
    random.shuffle(state)
    state = ['A'] + state      
    
    if state in existing:
        return generate_random_state(existing)
    return state

def cost(state):
    total = 0
    for i in range(len(state)-1):
        from_city=cities.index(state[i])
        to_city=cities.index(state[i+1])
        total += dist[from_city][to_city]

    total += dist[cities.index(state[-1])][cities.index(state[0])]
    return total

def generate_neighbours(state):
    neighbours = []
    for i in range(1, len(state)):
        for j in range(i+1, len(state)):
            new_state=state[:]
            new_state[i],new_state[j]=new_state[j],new_state[i]
            neighbours.append(new_state)
    return neighbours

for k in [3,5,10]:
    beam = []
    for i in range(k):
        beam.append(generate_random_state(beam))

    for iteration in range(100):

        frontier = []

        for state in beam:
            frontier.extend(generate_neighbours(state))

        frontier=[list(x) for x in set(tuple(x) for x in frontier)]

        frontier.sort(key=cost)

        beam=frontier[:k]

    print("\nBeam width =", k)
    print("Iteration", iteration)

    for s in beam:
        print(s, "Cost =", cost(s))