class VacuumProblem:

    def initial(self):
        return ('B','D','D')   
    def goal(self, state):
        return state in [('A','C','C'),('B','C','C')]

    def actions(self, state):
        pos,A,B=state

        Action_Sequence=['Remove']
        if pos == 'A':
            Action_Sequence.append('Right')
        else:
            Action_Sequence.append('Left')

        return Action_Sequence

    def result(self,state,action):
        pos,A,B=state

        if action=='Remove':

            if pos=='A':
                if A=='D':
                    return [
                        ('A','C',B),      
                        ('A','C','C')     
                    ]
                else:
                    return [
                        state,             
                        ('A','D',B)       
                    ]

            if pos=='B':
                if B=='D':
                    return [
                        ('B',A,'C'),
                        ('B','C','C')
                    ]
                else:
                    return [
                        state,
                        ('B',A,'D')
                    ]

        elif action=='Left':
            return [('A',A,B)]

        elif action=='Right':
            return [('B',A,B)]

    def cost(self,state,action):
        return 1  

def is_cycle(state,path):
    return state in path


def and_or_search(problem):
    return or_search(problem,problem.initial(),[])


def or_search(problem,state,path):
    if problem.goal(state):
        return []

    if is_cycle(state,path):
        return "failure"

    for action in problem.actions(state):
        plan=and_search(problem,problem.result(state, action),path+[state])

        if plan!="failure":
            return [action, plan]

    return "failure"


def and_search(problem,states,path):
    plans={}

    for s in states:
        plan=or_search(problem,s,path)

        if plan=="failure":
            return "failure"

        plans[s]=plan

    return plans

problem=VacuumProblem()
plan=and_or_search(problem)
print("\nConditional Plan:\n")
print(plan)