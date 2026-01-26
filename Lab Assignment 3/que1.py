# Implement a Simple Reflex Agent for a vacuum cleaner that can navigate a three-room
# environment (A, B, and C) and maintain cleanliness. Identify the “rationality” of its
# actions. How will you define the performance cost? Define the complete Rule Table and
# store it either in a dictionary/vector/matrix based on the language you implement the
# vacuum cleaner. Show the simulation output with percept, action, and location. Do you
# need priorities in the rules?


import random 
#Rule Table
ruletable = {
  ('A','DIRTY') : 'CLEAN',
  ('A','CLEAN') :  'MOVE RIGHT',
  ('B','DIRTY') : 'CLEAN',
  ('B','CLEAN'): random.choice(['MOVE RIGHT','MOVE LEFT']),
  ('B','DIRTY') : 'CLEAN',
  ('C','CLEAN') : 'MOVE LEFT',
  ('C','DIRTY') : 'CLEAN',
}


class Vacuum_cleaner :
  def __init__(self):
    self.cost=0

  def percept(self,loc,state):
    return (loc,state)

  
  def action(self,percept,ruletable):
      if percept[0] =='B' and percept[1] == 'CLEAN':
          return random.choice(['MOVE LEFT', 'MOVE RIGHT'])
      else:
          return ruletable.get(percept)
  
class Env : 
  def __init__(self):
    self.location= 'A'
    self.status = { 'A':'DIRTY' , 'B' : 'DIRTY','C': 'DIRTY'}

  def move(self,action):
      if action == 'MOVE RIGHT':
          if self.location == 'A':
            self.location = 'B'
          elif self.location == 'B':
            self.location = 'C'

      if action == 'MOVE LEFT':
          if self.location == 'C':
            self.location = 'B'
          elif self.location == 'B':
            self.location = 'A'
  
  def clean(self):
    self.status[self.location]='CLEAN'

def simulate(agent, rooms,step):
  print("\nStep \t Location \t Percept \t\t Action")

 
  while True:

    if all(state == 'CLEAN' for state in rooms.status.values()):
        print("\nAll rooms are CLEAN. Simulation stopped.")
        break

    percept = agent.percept(rooms.location, rooms.status[rooms.location])
    action  = agent.action(percept, ruletable)

    print(f"{agent.cost}\t    {rooms.location}\t\t{percept}\t\t{action}")

    if action == 'CLEAN':
        rooms.clean()
    else:
        rooms.move(action)

    agent.cost += 1
    step += 1


def main():
  agent = Vacuum_cleaner()
  rooms = Env()
  step=1
  while True:
    simulate(agent, rooms,step)
    print("Cost of Agent :", agent.cost)

    #Ask for user input
    choice = input("\nDo you want to make any room dirty? (yes/no): ").lower()

    if choice == 'no':
        print("Simulation ended.")
        break
    elif choice != 'yes':
        print("Invalid choice. Please enter 'yes' or 'no'.")
        continue

    room = input("Which room to make DIRTY? (A/B/C): ").upper()

    if room in rooms.status:
        rooms.status[room] = 'DIRTY'
        print(f"Room {room} is now DIRTY.")
    else:
        print("Invalid room.")

main()