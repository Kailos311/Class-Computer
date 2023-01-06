class Computer:
    def __init__(self, name, cpu, ram, hard):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.hard = hard
    def run(self):
        print("This " + self.name + " computer is running")