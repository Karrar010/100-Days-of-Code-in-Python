
class animal():
    def __init__(self):
        self.is_animal = "It is an animal"
    def is_halal(self):
        print("Yes")
class fish(animal):
    def __init__(self):
        super().__init__()
    def action(self):
        print("Breaths Under Water")

nemo = fish()
nemo.is_halal()
print(nemo.is_animal)
nemo.action()