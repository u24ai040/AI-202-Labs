# Design a Simple Reflex Agent for an Indian Railways Level Crossing. The agent must
# ensure maximum safety for road traffic while minimizing delays for the train, using
# multi-source sensory input without historical tracking.
# The environment consists of a double-track railway line intersecting a busy state
# highway. The percepts include the following:
# ● Track Sensors (Inbound/Outbound): Sensors placed 2km away that detect if a
# train is currently passing over them. It is either detected or not detected.
# ● Obstacle Sensors (Yellow Box): A grid of sensors on the road between the gates
# to detect “stuck” vehicles (e.g., an auto-rickshaw or buffalo).
# ● Manual Emergency Input: A physical lever for the station master. It is either
# Neutral or Active.
# Actuators:
# ● Gate Arm: Lower/Raise
# ● Hooter/Siren: On/Off
# ● Signal to Train: Green (Safe to proceed)/Red (Emergency Stop)

# Design the rules set. Show the simulation output with percept, action, and location. Do you need
# priorities in the rules?

ruletable = {
    # Manual Emergency – highest priority
    ('DETECTED','DETECTED','CLEAR','ACTIVE') : 'EMERGENCY_STOP',
    ('DETECTED','NOT_DETECTED','CLEAR','ACTIVE') : 'EMERGENCY_STOP',
    ('NOT_DETECTED','DETECTED','CLEAR','ACTIVE') : 'EMERGENCY_STOP',
    ('NOT_DETECTED','NOT_DETECTED','CLEAR','ACTIVE') : 'EMERGENCY_STOP',
    ('DETECTED','DETECTED','STUCK','ACTIVE') : 'EMERGENCY_STOP',
    ('DETECTED','NOT_DETECTED','STUCK','ACTIVE') : 'EMERGENCY_STOP',
    ('NOT_DETECTED','DETECTED','STUCK','ACTIVE') : 'EMERGENCY_STOP',
    ('NOT_DETECTED','NOT_DETECTED','STUCK','ACTIVE') : 'EMERGENCY_STOP',

    #when train is coming there is an obstacle
    ('DETECTED','NOT_DETECTED','STUCK','NEUTRAL') : 'EMERGENCY_STOP',
    ('NOT_DETECTED','DETECTED','STUCK','NEUTRAL') : 'TRAIN_GONE',

    # Train is comming and no obstacle
    ('DETECTED','NOT_DETECTED','CLEAR','NEUTRAL') : 'TRAIN_INCOMING',

    # Train passed safely
    ('NOT_DETECTED','DETECTED','CLEAR','NEUTRAL') : 'TRAIN_GONE',

    # No train, obstacle clears naturally
    ('NOT_DETECTED','NOT_DETECTED','STUCK','NEUTRAL') : 'NONE',
    ('NOT_DETECTED','NOT_DETECTED','CLEAR','NEUTRAL') : 'NONE'
}

class Agent:
    def __init__(self):
        self.cost = 0

    def percept(self,inbound,outbound,obstacle,manual):
        return (inbound,outbound,obstacle,manual)

    def action(self,percept):
        return ruletable.get(percept)

class Env:
    def __init__(self):
        self.Gate_Arm = 'RAISE'
        self.Siren = 'OFF'
        self.Signal = 'RED'
        self.just_cleared = False
        self.inbound = 'DETECTED'
        self.outbound = 'NOT_DETECTED'
        self.obstacle = 'STUCK'
        self.manual = 'NEUTRAL'

    def take_user_input(self,done=True):
        while True:
            print("\n Give the Inputs or Percepts:")
            train=input("Is train coming? (in / out / no): ").lower()
            if train=='in':
                self.inbound='DETECTED'
                self.outbound='NOT_DETECTED'
            elif train=='out':
                self.inbound='NOT_DETECTED'
                self.outbound='DETECTED'
            elif train!='no':
                print("Invalid Input.try again")
                continue
                
            else:
                self.inbound='NOT_DETECTED'
                self.outbound='NOT_DETECTED'

            obs = input("Is any vehicle stuck? (yes/no): ").lower()
            if obs=='yes':
                self.obstacle='STUCK'
            elif obs!='no':
                print("Invalid Input .try again")
                continue
            else:
                self.obstacle='CLEAR'

            emer = input("Manual emergency active? (yes/no): ").lower()
            if emer =='yes':
                self.manual='ACTIVE' 
            elif emer!='no':
                print("Invalid Input .try again")
                continue   
            else:
                self.manual='NEUTRAL'
            break

    def train_incoming(self):
        self.Gate_Arm = 'LOWER'
        self.Siren = 'ON'
        self.Signal = 'GREEN'

        # As Train passes inbound sensor , then we update the percepts
        self.inbound = 'NOT_DETECTED'
        self.outbound = 'DETECTED'

    def train_gone(self):
        self.Gate_Arm = 'RAISE'
        self.Siren = 'OFF'
        self.Signal = 'RED'
        
        # As Train gone, then we update the percepts
        self.outbound = 'NOT_DETECTED'
        self.obstacle = 'CLEAR'
        self.just_cleared = True 

    def emergency(self):
        self.Gate_Arm = 'RAISE'
        self.Siren = 'OFF'
        self.Signal = 'RED'

        # Emergency handling clears obstacle
        self.obstacle = 'CLEAR'
        self.outbound = 'NOT_DETECTED'

    def do_nothing(self):
        self.obstacle = 'CLEAR'
        self.just_cleared = False

    def execute(self, action):
        if action == 'TRAIN_INCOMING':
            self.train_incoming()
        elif action == 'TRAIN_GONE':
            self.train_gone()
        elif action == 'EMERGENCY_STOP':
            self.emergency()
        elif action == 'NONE':
            self.do_nothing()


def simulate():
    agent = Agent()
    env = Env()
    print("\nStep | Percept (IN, OUT, OBS, MAN) \t\t Action \t\t Gate \t Siren \t Signal")

    for step in range(1, 50) :
        # Ask user only if no train detected
        if env.inbound == 'NOT_DETECTED' and env.outbound == 'NOT_DETECTED' and env.obstacle == 'CLEAR' and not env.just_cleared:
            print("Do You want to give Inputs ? (yes/no) :")
            choice=input().lower()
            if choice == 'no':
                print("Simulation ended")
                print("Total Cost of Agent:", agent.cost)
                return
                
                
            elif choice!='yes':
                print("Invalid Input.")
                continue
            env.take_user_input()
        

        percept = agent.percept(env.inbound, env.outbound, env.obstacle, env.manual)
        action = agent.action(percept)

        if(action != 'NONE'):
            agent.cost+=1

        env.execute(action)



        if env.manual == 'ACTIVE':
            percept = agent.percept(env.inbound, env.outbound, env.obstacle, env.manual)
            action = agent.action(percept)
            env.execute(action)

            print(step, " | ", percept, "\t" , action, "\t",env.Gate_Arm, "\t", env.Siren, "\t", env.Signal)

            print("\nEmergency Manual is Now Active")
            choice = input("Do you want to switch it to neutral (yes / no)").lower()

            if choice == 'yes':
                env.manual = 'NEUTRAL'
                print("Emergency Manual is Now Neutral\n")
            else:
                print("Total Cost of Agent:", agent.cost)
                return

            continue


        print(step, " | ", percept, "\t", action, "\t", env.Gate_Arm, "\t", env.Siren, "\t", env.Signal)

    print("\nTotal Cost of Agent:", agent.cost)

simulate()
