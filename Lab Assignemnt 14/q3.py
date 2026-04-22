class KB:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(clause)


def negation(literal):
    if literal.startswith('NOT '):
        return literal[4:]
    else:
        return 'NOT ' + literal


def resolve(ci, cj):
    resolvents = []
    
    for di in ci:
        for dj in cj:
            if di == negation(dj):
                n_clauses = []
                
                for x in ci:
                    if x != di and x not in n_clauses:
                        n_clauses.append(x)
                
                for x in cj:
                    if x != dj and x not in n_clauses:
                        n_clauses.append(x)
                
                resolvents.append(n_clauses)
    
    return resolvents


def pl_resolution(kb, query):
    
    clauses = []
    for c in kb.clauses:
        clauses.append(c.copy())
    
    clauses.append([negation(query)])
    
    while True:
        new = []
        
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                
                resolvents = resolve(clauses[i], clauses[j])
                
                for r in resolvents:
                    if len(r) == 0:
                        return True
                    
                    if r not in clauses and r not in new:
                        new.append(r)
        
        a = True
        for c in new:
            if c not in clauses:
                a = False
        
        if a:
            return False
        
        for c in new:
            clauses.append(c)


# Problem (a)

kba = KB()
kba.add_clause(['P', 'Q'])
kba.add_clause(['NOT P', 'R'])
kba.add_clause(['NOT Q', 'S'])
kba.add_clause(['NOT R', 'S'])

result_a = pl_resolution(kba, 'S')

print("Problem (a):")
if result_a:
    print("S is entailed (True)")
else:
    print("S is not entailed (False)")


# Problem (b)

kbb = KB()
kbb.add_clause(['NOT P', 'Q'])
kbb.add_clause(['NOT Q', 'R'])
kbb.add_clause(['NOT S', 'NOT R'])
kbb.add_clause(['P'])

result_b = pl_resolution(kbb, 'S')

print("\nProblem (b):")
if result_b:
    print("S is entailed (True)")
else:
    print("S is not entailed (False)")