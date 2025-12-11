# coffee.py (UPDATED - TASK 2: Method Overriding and Reuse)

from typing import Optional
from intensity import Intensity
from syrup_type import SyrupType

# --- Base Class (Level 1) ---
class Coffee:
    """The base class. Adds: coffeeIntensity."""
    def __init__(self, name: str, intensity: Intensity):
        self.name: str = name
        self.coffee_intensity: Intensity = intensity
        self._const_name: str = "Coffee" # Added for better hierarchy tracing in output

    def print_coffee_details(self):
        """Prints the base details."""
        print(f"--- {self.name} Details ---")
        # Task 2 Improvement: Showing the base name
        print(f"Type: {self.__class__.__name__} (Base: {self._const_name})") 
        print(f"Intensity: {self.coffee_intensity.value}")

# --- Sub-Classes (Level 2) ---
class WaterBasedCoffee(Coffee):
    """Inherits Coffee. Adds: mlOfWater. Correctly uses super()."""
    def __init__(self, name: str, intensity: Intensity, ml_of_water: int):
        super().__init__(name, intensity)
        self.ml_of_water: int = ml_of_water 
    
    def print_coffee_details(self):
        # Task 2: Reuse parent's printing logic
        super().print_coffee_details()
        print(f"Water: {self.ml_of_water} ml")

class MilkBasedCoffee(Coffee):
    """Inherits Coffee. Adds: mlOfMilk. Correctly uses super()."""
    def __init__(self, name: str, intensity: Intensity, ml_of_milk: int):
        super().__init__(name, intensity)
        self.ml_of_milk: int = ml_of_milk
    
    def print_coffee_details(self):
        # Task 2: Reuse parent's printing logic
        super().print_coffee_details()
        print(f"Milk: {self.ml_of_milk} ml")

# --- Sub-Classes (Level 3) ---
class SpiceCoffee(MilkBasedCoffee):
    """Inherits MilkBasedCoffee. Adds: mgOfSpice. Correctly uses super()."""
    def __init__(self, name: str, intensity: Intensity, ml_of_milk: int, mg_of_spice: int):
        super().__init__(name, intensity, ml_of_milk)
        self.mg_of_spice: int = mg_of_spice
    
    def print_coffee_details(self):
        # Task 2: Reuse parent's printing logic (which includes the Milk detail)
        super().print_coffee_details()
        print(f"Spice: {self.mg_of_spice} mg")

class SyrupCoffee(MilkBasedCoffee):
    """Inherits MilkBasedCoffee. Adds: SyrupType. Correctly uses super()."""
    def __init__(self, name: str, intensity: Intensity, ml_of_milk: int, syrup_type: SyrupType):
        super().__init__(name, intensity, ml_of_milk)
        self.syrup_type: SyrupType = syrup_type

    def print_coffee_details(self):
        # Task 2: Reuse parent's printing logic (which includes the Milk detail)
        super().print_coffee_details()
        print(f"Syrup Flavor: {self.syrup_type.value}")
