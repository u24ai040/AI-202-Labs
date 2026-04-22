class KB:
    def __init__(self):
        self.symbols = []
        self.premise_conclusions = {}
        self.facts = []

    def add_rule(self, premise, conclusion):
        if conclusion not in self.premise_conclusions:
            self.premise_conclusions[conclusion] = []
        self.premise_conclusions[conclusion].append(premise)
        for p in premise:
            if p not in self.symbols:
                self.symbols.append(p)
        if conclusion not in self.symbols:
            self.symbols.append(conclusion)

    def add_fact(self, fact):
        if fact not in self.facts:
            self.facts.append(fact)
        if fact not in self.symbols:
            self.symbols.append(fact)


def backward_chaining(kb, query, visited):
    
    if query in kb.facts:
        return True
    
    if query in visited:
        return False
    
    visited.append(query)
    
    if query not in kb.premise_conclusions:
        return False
    
    rules = kb.premise_conclusions[query]
    
    for premise in rules:
        all_true = True
        
        for symbol in premise:
            if not backward_chaining(kb, symbol, visited):
                all_true = False
                break
        
        if all_true:
            return True
    
    return False


kba = KB()
kba.add_rule(['P'], 'Q')  # P → Q
kba.add_rule(['R'], 'Q')  # R → Q
kba.add_rule(['A'], 'P')  # A → P
kba.add_rule(['B'], 'R')   # B → R

kba.add_fact('A')
kba.add_fact('B')

qa = 'Q'

result_a = backward_chaining(kba, qa, [])

print("Problem (a):")
if result_a:
    print("Q is entailed (True)")
else:
    print("Q is not entailed (False)")


kbb = KB()
kbb.add_rule(['A'], 'B')  # A → B

kbb.add_rule(['B', 'C'], 'D')    # B ∧ C → D
kbb.add_rule(['E'], 'C')   # E → C

kbb.add_fact('A')
kbb.add_fact('E')

qb = 'D'

result_b = backward_chaining(kbb, qb, [])

print("\nProblem (b):")
if result_b:
    print("D is entailed (True)")
else:
    print("D is not entailed (False)")