class Main:
    def __init__(self):
        robot1 = Robot("Felipe", "Red", 70)
        robot1.name = "Pendejo"
        robot1.introduceSelf()


class Robot:
    name: str
    color = str
    weight = int

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        self.introduceSelf()
        pass

    def introduceSelf(self):
        print(f"My name is {self.name}, I'm {self.color} and {self.weight} Kg")

if __name__ == "__main__":
    Main()