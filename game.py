from pet import Pet
import random

class Game:
    def __init__(self):
        name = input("Please enter a name for your pet: ")
        self.pet = Pet(name)
        self.day = 1

    def show_menu(self):
        print(f"=== Day {self.day} ===")
        print("Choose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Clean")
        print("4. Sleep")
        print("5. Show status")
        print("6. Quit")

    def step(self, choice):
        if choice == "1":
            self.pet.feed()
            print("You fed your pet.")
        elif choice == "2":
            self.pet.play()
            print("You played with your pet.")
        elif choice == "3":
            self.pet.clean()
            print("You cleaned your pet.")
        elif choice == "4":
            self.pet.sleep()
            print("Your pet took a nap.")
        elif choice == "5":
            self.pet.status()
            return True  # Showing status does not advance time
        elif choice == "6":
            print("Thanks for playing! Goodbye.")
            return False
        else:
            print("Invalid input. Please choose a valid option.")
            return True

        self.pet.decay()
        self.random_event()
        if not self.pet.isAlive():
            print(f"Sadly, {self.pet.name}'s health has dropped to zero. Game over! You lasted {self.day} days.")
            return False

        self.day += 1
        return True

    def run(self):
        print("Welcome to the Virtual Pet Game!")
        running = True
        while running:
            self.show_menu()
            choice = input("Enter your choice (1-6): ")
            running = self.step(choice)
    def random_event(self):
        chance = random.random()

        if chance < 0.05:
            print("🌟 Random Event: Your pet found a tasty snack!")
            self.pet.hunger = min(100, self.pet.hunger + 10)
            self.pet.mood = min(100, self.pet.mood + 5)
        elif chance < 0.10:
            print("💊 Random Event: Your pet is feeling a bit unwell. Health decreases.")
            self.pet.health = max(0, self.pet.health - 15)
        elif chance < 0.15:
            print("👋 Random Event: A neighbor's pet came over! Mood increases.")
            self.pet.mood = min(100, self.pet.mood + 15)
        elif chance < 0.20:
            print("🧹 Random Event: Your pet played too hard and made a mess. Cleanliness decreases.")
            self.pet.cleanliness = max(0, self.pet.cleanliness - 20)

if __name__ == "__main__":
    Game().run()
