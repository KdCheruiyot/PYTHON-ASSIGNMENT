# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def specs(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nStorage: {self.storage}GB")

# Child class inheriting Smartphone
class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_quality):
        super().__init__(brand, model, storage)  # Inherit base attributes
        self.camera_quality = camera_quality     # Additional attribute

    # Method Overriding (Polymorphism)
    def specs(self):
        super().specs()  # Call parent specs
        print(f"Camera Quality: {self.camera_quality}MP")

    def take_picture(self):
        print(f"{self.brand} {self.model} is taking a picture with {self.camera_quality}MP camera!")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy A14", 128)
phone2 = SmartPhonePro("iPhone", "15 Pro Max", 256, 48)

# Calling methods
phone1.specs()
phone1.call("+123456789")

print("\n--- Upgraded Phone ---\n")
phone2.specs()
phone2.call("+987654321")
phone2.take_picture()
