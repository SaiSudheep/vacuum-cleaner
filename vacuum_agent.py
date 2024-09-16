import sys

class Agent:
    def __init__(self):
        self.state = 0
        self.actionList = [0]

    def chooseAction(self):
        return self.actionList[0]
    
    def senseEnvironment(self, currentEnvironment):
        pass

    def getState(self):
        return 0

class Environment:
    def __init__(self, state):
        self.state = 0

    def getCurrentEnvironment(self):
        return self.state

    def applyAgentAction(self, agentAction):
        pass

    def getState(self):
        return 0

# Vacuum cleaner agent
class VacuumBot(Agent):
    def __init__(self):
        self.room = "A"
        self.state = "Clean"

    def chooseAction(self):
        if (self.state == "Dirty"):
            return "Suck"
        elif (self.state == "Clean" and self.room == "A"):
            return "Move Right"
        else:
            return "Move Left"

    def senseEnvironment(self, room, state):
        self.room = room
        self.state = state

    def getState(self):
        if (self.state == "Dirty"):
            return "Cleaning Room " + self.room
        elif (self.state == "Clean" and self.room == "A"):
            return "Moving to B"
        else:
            return "Moving to A"

# State of the two rooms involved
class VacuumEnvironment(Environment):
    def __init__(self, botRoom, stateA, stateB):
        self.botRoom = botRoom
        self.stateA = stateA
        self.stateB = stateB

    def getCurrentEnvironment(self):
        if (self.botRoom == "A"):
            return self.botRoom, self.stateA
        else:
            return self.botRoom, self.stateB

    def applyAgentAction(self, agentAction):
        if (agentAction == "Suck"):
            if (self.botRoom == "A"):
                self.stateA = "Clean"
            else:
                self.stateB = "Clean"
        elif (agentAction == "Move Right"):
            self.botRoom = "B"
        else:
            self.botRoom = "A"

    def getState(self):
        return "Room A: " + self.stateA + ", Room B: " + self.stateB

# We simulate the agent-environment interaction for several iterations
if __name__ == "__main__":
    # Pass arguments while executing - initial agent room, state of room A, state of room B, and total iterations
    #
    # Example: py vacuum_agent.py A Dirty Clean
    #                                                                                               Sai Sudheep Namachivayam
    #                                                                                               017857346
    botRoom = sys.argv[1]
    stateA = sys.argv[2]
    stateB = sys.argv[3]
    iterations = sys.argv[4]

    vacBot = VacuumBot()
    vacEnv = VacuumEnvironment(botRoom, stateA, stateB)
    
    print()
    print()
    print("Initial Agent Room: " + botRoom)
    print()
    print("Initial Environment:")
    print("Room A: " + stateA + ", Room B: " + stateB)
    print()
    print()

    for i in range(int(iterations)):
        botRoom, roomState = vacEnv.getCurrentEnvironment()
        vacBot.senseEnvironment(botRoom, roomState)
        vacEnv.applyAgentAction(vacBot.chooseAction())
        print(f"Iteration: {i + 1}")
        print(f"vacBot: {vacBot.getState()}")
        print(f"vacEnv: {vacEnv.getState()}")
        print()

    print()