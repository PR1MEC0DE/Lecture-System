# barista.py

from typing import List, Union
# The Barista layer IS allowed to access and import the core classes.
from coffee import Coffee, WaterBasedCoffee, MilkBasedCoffee, SpiceCoffee, SyrupCoffee 
from intensity import Intensity
from syrup_type import SyrupType

# Define a type hint for any specific coffee object we'll handle
CoffeeProduct = Union[WaterBasedCoffee, MilkBasedCoffee, SpiceCoffee, SyrupCoffee]

class Barista:
    """
    The Barista class acts as the control layer, enforcing module-level encapsulation.
    It handles creation, printing details (Task 2), and making coffee (Task 3).
    """

    def __init__(self, name: str = "TUM Barista-Bot"):
        self.name = name

    def fulfill_order(self, order_list: List[CoffeeProduct]):
        """
        Accepts a list of coffee objects and processes them one by one.
        This method fully demonstrates the logic of Tasks 2 and 3.
        """
        print(f"\n--- {self.name} is fulfilling the order (Total: {len(order_list)}) ---")
        
        for i, coffee in enumerate(order_list):
            print(f"\n[{i+1}/{len(order_list)}] New Order: {coffee.name}")
            
            # 1. Print Details (Calling Task 2 logic)
            print("-" * 25)
            coffee.print_coffee_details()
            print("-" * 25)

            # 2. Make the coffee (Calling Task 3 logic)
            self._make_specific_coffee(coffee)

    def _make_specific_coffee(self, coffee: CoffeeProduct):
        """
        Internal method to correctly call the class-specific make method based on the object type.
        """
        print("\n[Recipe Steps]")
        if isinstance(coffee, SpiceCoffee):
            coffee.make_pumpkin_spice_latte()
        elif isinstance(coffee, SyrupCoffee):
            coffee.make_syrup_cappuccino()
        elif isinstance(coffee, WaterBasedCoffee):
            coffee.make_americano()
        elif isinstance(coffee, MilkBasedCoffee):
            coffee.make_cappuccino()
        else:
            coffee.make()
