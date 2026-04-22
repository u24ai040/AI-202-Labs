class KB:
    def __init__(self):
        self.symbols = []
        self.premise_conclusions = []
        self.facts = []

    def add_rule(self, premise, conclusion):
        self.premise_conclusions.append((premise, conclusion))
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


# Forward Chaining Algorithm 
def forward_chaining(KB, facts, query):
    
    count = []
    for i in range(len(KB)):
        pre = KB[i][0]
        count.append(len(pre))
    
    inferred = {}
    
    for i in range(len(KB)):
        pre = KB[i][0]
        concl = KB[i][1]
        
        for symbol in pre:
            inferred[symbol] = False
        
        inferred[concl] = False
    
    q = []
    for fact in facts:
        q.append(fact)
    
    while len(q) != 0:
        
        p = q.pop(0)  
        
        if p == query:
            return True
        
        if inferred[p] == False:
            inferred[p] = True
            
            for i in range(len(KB)):
                pre = KB[i][0]
                concl = KB[i][1]
                
                if p in pre:
                    count[i] = count[i] - 1
                    
                    if count[i] == 0:
                        q.append(concl)
    
    return False


# Problem (a)
kba = KB()
kba.add_rule(['P'], 'Q')        # P → Q
kba.add_rule(['L', 'M'], 'P')   # L ∧ M → P
kba.add_rule(['A', 'B'], 'L')   # A ∧ B → L

kba.add_fact('A')
kba.add_fact('B')
kba.add_fact('M')

result_a = forward_chaining(kba.premise_conclusions, kba.facts, 'Q')

print("Problem (a):")
if result_a:
    print("Q is entailed (True)")
else:
    print("Q is not entailed (False)")


# Problem (b)
kbb = KB()
kbb.add_rule(['A'], 'B')        # A → B
kbb.add_rule(['B'], 'C')        # B → C
kbb.add_rule(['C'], 'D')        # C → D
kbb.add_rule(['D', 'E'], 'F')   # D ∧ E → F

kbb.add_fact('A')
kbb.add_fact('E')

result_b = forward_chaining(kbb.premise_conclusions, kbb.facts, 'F')

print("\nProblem (b):")
if result_b:
    print("F is entailed (True)")
else:
    print("F is not entailed (False)")