import random
import math
N=8
def generate_board(N):
  board=[]
  for i in range(N):
    board.append(random.randint(0,7))
  
  return board

def heuri(board):
  h=0
  for i in range(N):
    for j in range(i+1,N):
      if board[i]==board[j]:
        h+=1
      if abs(board[i]-board[j])==abs(i-j):
        h+=1
  return h
        
def find_best_neighbour(curr):
  b2=curr[:]
  h=heuri(curr)

  for i in range(N):
    i_row=b2[i]
    for j in range(N):
      if i_row==j:
        continue
      b2[i]=j
      h_new=heuri(b2)
      if h_new<h:
        h=h_new
        curr=b2[:]
    b2[i]=i_row
  
  return curr,h


def steepest_ascent(board):
    steps = 0
    curr = board[:]
    curr_h = heuri(curr)
    
    while True:
        neigh,nh=find_best_neighbour(curr)
        if nh >=curr_h:
            return curr,curr_h,steps
        curr=neigh
        curr_h=nh
        steps+=1
def first_choice(board):
  curr=board[:]
  curr_h=heuri(curr)
  steps=0

  while True:

    found=False

    for i in range(100):

      col=random.randint(0,7)
      row=random.randint(0,7)

      if row==curr[col]:
        continue

      new=curr[:]
      new[col]=row

      h_new=heuri(new)

      if h_new<curr_h:
        curr=new
        curr_h=h_new
        steps+=1
        found=True
        break

    if found==False:
      return curr,curr_h,steps
   
def random_restart():

  total_steps=0

  for i in range(50):
    board=generate_board(N)
    final,h,steps=steepest_ascent(board)
    total_steps+=steps

    if h==0:
      return final,h,total_steps

  return final,h,total_steps

def schedule(t):
  return 0.99**t # Here we used Exponential Cooling


def simulated_annealing(board):

  current=board[:]
  current_h=heuri(current)

  steps=0
  t=1

  while True:

    T=schedule(t)

    if T<0.001 or current_h==0:
      return current,current_h,steps


    # random neighbour
    col=random.randint(0,7)
    row=random.randint(0,7)

    next_state=current[:]
    next_state[col]=row

    next_h=heuri(next_state)

    delta=current_h-next_h


    if delta>0:
      current=next_state
      current_h=next_h

    else:
      prob=math.exp(delta/T)

      if random.random()<prob:
        current=next_state
        current_h=next_h


    steps+=1
    t+=1
def simulation(name):

  results=[]

  for j in range(50):

    curr=generate_board(N)
    h=heuri(curr)


    if name=="First Choice":
      final,final_h,steps=first_choice(curr)

    elif name=="Random Restart":
      final,final_h,steps=random_restart()

    elif name=="Simulated Annealing":
      final,final_h,steps=simulated_annealing(curr)


    status="Solved" if final_h==0 else "Fail"

    results.append((h,final_h,steps,status))


  print("\n======",name,"======")
  print("Run  Initial_h  Final_h  Steps  Status")

  for i,r in enumerate(results,1):
    print(f"{i}\t   {r[0]}      {r[1]}     {r[2]}\t   {r[3]}")


  solved=0
  for r in results:
    if r[3]=="Solved":
      solved+=1

  print("\nSolved:",solved)
  print("Failed:",50-solved)


simulation("First Choice")

simulation("Random Restart")

simulation("Simulated Annealing")
