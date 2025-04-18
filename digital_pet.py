class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate. Hunger decreased, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept. Energy restored!")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played. Energy used, happiness increased, and hunger grew!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"• Hunger: {self.hunger}/10")
        print(f"• Energy: {self.energy}/10")
        print(f"• Happiness: {self.happiness}/10")

    # Bonus methods
    def train(self, trick):
        self.tricks.append(trick)
        print(f"\n{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"\n{self.name} doesn't know any tricks yet.")
            return
        print(f"\n{self.name} knows these tricks:")
        for i, trick in enumerate(self.tricks, 1):
            print(f"{i}. {trick.capitalize()}")