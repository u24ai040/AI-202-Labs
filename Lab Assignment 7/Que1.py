import random
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

results = []
for j in range(50):
  curr=generate_board(N)
  h=heuri(curr)
  final,final_h,steps=steepest_ascent(curr)
  status = "Solved" if final_h == 0 else "Fail"
    
  results.append((h, final_h, steps, status))

print("Run  Initial_h  Final_h  Steps  Status")
for i, r in enumerate(results, 1):
    print(f"{i}\t   {r[0]}      {r[1]}     {r[2]}\t   {r[3]}")
sum=0
for r in results:
  if r[3] == "Solved":
    sum+=1

solved=sum
fail = len(results) - solved

print("\nNo of Solved:", solved)
print("No of Failed:", fail)

for i, r in enumerate(results, 1):
    if r[1] > 0:
        print(f"\nLocal minimum Failed to get Global Maxima in run {i} having final_h: {r[1]}")
        print("This proves hill climbing got stuck at a non-goal state with no better neighbor.")
        break

 






