class Human:
    def __init__(self, x_position=0, y_position=0):	
        self.y_position = y_position
        self.x_position = x_position

class Feared(Human):
    def __init__(self, x_position=0, y_position=0, fear_percent=0): 
        self.y_position = y_position
        self.x_position = x_position
        self.fear_percent=fear_percent

    def __init__(self, human=Human(), fear_percent=0):
        print("adaasda")
        self.y_position = human.y_position
        self.x_position = human.x_position
        self.fear_percent=0

a=Human(2,3)
b=Feared()
print(b.y_position)

