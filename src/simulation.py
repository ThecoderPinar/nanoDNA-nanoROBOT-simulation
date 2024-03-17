class Simulation:
    def __init__(self):
        self.total_moves = 0
        self.position = [0, 0, 0]

    def move(self, displacement):
        self.position = [self.position[i] + displacement[i] for i in range(3)]
        self.total_moves += 1

    def run(self):
        pass
