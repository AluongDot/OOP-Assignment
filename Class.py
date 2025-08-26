# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.model} charged to {self.battery}%")

# Subclass (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        if self.battery > 20:
            self.battery -= 20
            print(f"Playing {game} on {self.model} with {self.gpu} GPU 🎮. Battery: {self.battery}%")
        else:
            print(f"Battery too low to play {game} 😢")

# Test
phone1 = Smartphone("Samsung", "Galaxy S25", "256GB", 80)
phone1.call("+123456789")
phone1.charge(15)

gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", "512GB", 90, "Adreno 740")
gaming_phone.play_game("PUBG Mobile")
gaming_phone.charge(5)
