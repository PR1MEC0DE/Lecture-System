# coffee.py ( TASK 3: Recipe Logic)

from typing import Optional
from intensity import Intensity
from syrup_type import SyrupType

# --- Base Class (Level 1) ---
class Coffee:
    """The base class. Adds: coffeeIntensity."""
    def __init__(self, name: str, intensity: Intensity):
        self.name: str = name
        self.coffee_intensity: Intensity = intensity
        self._const_name: str = "Coffee"

    def print_coffee_details(self):
        """Prints the base details (Task 2)."""
        print(f"--- {self.name} Details ---")
        print(f"Type: {self.__class__.__name__} (Base: {self._const_name})") 
        print(f"Intensity: {self.coffee_intensity.value}")

    # TASK 3: Base make method
    def make(self) -> 'Coffee':
        """The base recipe step for all coffees."""
        print(f" * Starting with base espresso for {self.name}")
        return self

# --- Sub-Classes (Level 2) ---
class WaterBasedCoffee(Coffee):
    """Inherits Coffee. Adds: mlOfWater."""
    def __init__(self, name: str, intensity: Intensity, ml_of_water: int):
        super().__init__(name, intensity)
        self.ml_of_water: int = ml_of_water 
    
    def print_coffee_details(self):
        super().print_coffee_details()
        print(f"Water: {self.ml_of_water} ml")

    # TASK 3: Class-specific make method
    def make_americano(self) -> 'WaterBasedCoffee': 
        # Reuse parent recipe step
        self.make() 
        print(f" * Adding {self.ml_of_water} mls of water")
        return self

class MilkBasedCoffee(Coffee):
    """Inherits Coffee. Adds: mlOfMilk."""
    def __init__(self, name: str, intensity: Intensity, ml_of_milk: int):
        super().__init__(name, intensity)
        self.ml_of_milk: int = ml_of_milk
    
    def print_coffee_details(self):
        super().print_coffee_details()
        print(f"Milk: {self.ml_of_milk} ml")

    # TASK 3: Class-specific make method (used as a base for Spice/Syrup)
    def make_cappuccino(self) -> 'MilkBasedCoffee': 
        # Reuse parent recipe step
        self.make() 
        print(f" * Steaming {self.ml_of_milk} mls of milk")
        return self

# --- Sub-Classes (Level 3) ---
class SpiceCoffee(MilkBasedCoffee):
    """Inherits MilkBasedCoffee. Adds: mgOfSpice."""
    def __init__(self, name: str, intensity: Intensity, ml_of_milk: int, mg_of_spice: int):
        super().__init__(name, intensity, ml_of_milk)
        self.mg_of_spice: int = mg_of_spice
    
    def print_coffee_details(self):
        super().print_coffee_details()
        print(f"Spice: {self.mg_of_spice} mg")

    # TASK 3: Class-specific make method
    def make_pumpkin_spice_latte(self) -> 'SpiceCoffee':
        # Reuse MilkBasedCoffee recipe step
        self.make_cappuccino() 
        print(f" * Adding {self.mg_of_spice} mgs of spice for flavoring")
        return self

class SyrupCoffee(MilkBasedCoffee):
    """Inherits MilkBasedCoffee. Adds: SyrupType."""
    def __init__(self, name: str, intensity: Intensity, ml_of_milk: int, syrup_type: SyrupType):
        super().__init__(name, intensity, ml_of_milk)
        self.syrup_type: SyrupType = syrup_type

    def print_coffee_details(self):
        super().print_coffee_details()
        print(f"Syrup Flavor: {self.syrup_type.value}")

    # TASK 3: Class-specific make method
    def make_syrup_cappuccino(self) -> 'SyrupCoffee':
        # Reuse MilkBasedCoffee recipe step
        self.make_cappuccino()
        print(f" * Adding {self.syrup_type.value} syrup for extra flavor")
        return self
