class Pet:
    def __init__(self,name): 
        self.name = name
        self.hunger = 60
        self.cleanliness = 60
        self.mood = 60
        self.health = 100
    
    def feed(self): 
        self.hunger = min(100, self.hunger + 20)
    
    def play(self):
        self.mood = min(100, self.mood + 15)
        self.hunger = max(0, self.hunger - 10)

    def clean(self): 
        self.cleanliness = 100

    def sleep(self):
        self.health = min(100, self.health + 10)
        self.hunger = max(0, self.hunger -15)

    def decay(self):
        self.hunger = max(0, self.hunger - 5)
        self.mood = max(0, self.mood - 3)
        self.cleanliness = max(0, self.cleanliness - 4)

        if self.hunger == 0: 
            self.health = max(0, self.health - 10)
        if self.mood == 0: 
            self.health = max(0, self.health - 30)
        if self.cleanliness == 0: 
            self.health = max(0, self.health - 50)
    
    def status(self): 
        print(f'_______{self.name} state_______')
        print(f'hunger:       {self.hunger} |100')
        print(f'mood:         {self.mood} |100')
        print(f'cleanliness:  {self.cleanliness} |100')
        print(f'health:      {self.health} |100')
    
    def isAlive(self): 
        return self.health > 0
