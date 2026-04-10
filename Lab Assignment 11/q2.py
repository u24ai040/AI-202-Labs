variables=['S','E','N','D','M','O','R','Y']
assigned=[False]*10
ans=[]
all_solutions=[]

def solve(i):
  if i==len(variables):
    if valid():
      all_solutions.append(ans.copy())
  
  for digit in range(10):
    if assigned[digit]==True:
      continue

    if (variables[i]=='S' or variables[i]=='M') and digit==0:
      continue

    ans.append(digit)
    assigned[digit]=True

    if solve(i+1):
      return True
    
    assigned[digit]=False
    ans.pop()

  return False


def valid():
  n1=ans[0]*1000+ans[1]*100+ans[2]*10+ans[3]

  n2=ans[4]*1000+ans[5]*100+ans[6]*10+ans[1]

  n3=ans[4]*10000+ans[5]*1000+ans[2]*100+ans[1]*10+ans[7]
  return n1+n2==n3

  
variables=['S','E','N','D','M','O','R','Y']

assigned=[False]*10
ans=[]

all_solutions=[]


def solve(i):
    if i==len(variables):
        if valid():
            all_solutions.append(ans.copy())
        return

    for digit in range(10):

        if assigned[digit]:
            continue

        if (variables[i]=='S' or variables[i]=='M') and digit==0:
            continue

        ans.append(digit)
        assigned[digit]=True

        solve(i+1)

        assigned[digit]=False
        ans.pop()


def valid():
    n1=ans[0]*1000+ans[1]*100+ans[2]*10+ans[3]

    n2=ans[4]*1000+ans[5]*100+ans[6]*10+ans[1]

    n3=ans[4]*10000+ans[5]*1000+ans[2]*100+ans[1]*10+ans[7]

    return n1+n2==n3


solve(0)


if len(all_solutions)>0:

    print("Total Solutions:",len(all_solutions))
    print()

    for idx,sol in enumerate(all_solutions):

        print("Solution",idx+1)

        for i in range(len(variables)):
            print(variables[i],"=",sol[i])

        print()

else:
    print("No Such solution is possible")


