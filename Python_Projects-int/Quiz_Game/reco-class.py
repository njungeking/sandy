# A brief recap of classes.

class FootBallPlayers:
    print("Welcome to a player profile!")

    def __init__(self, name, jersey):
        self.name = name
        self.no = jersey
        self.goals = 67


ballers = FootBallPlayers("Ronaldo", 7)
print(ballers.name)
print(ballers.no)
print(ballers.goals)

