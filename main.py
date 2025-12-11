# main.py (TASK 1 CHECK)
from intensity import Intensity
from syrup_type import SyrupType
from coffee import Coffee, WaterBasedCoffee, MilkBasedCoffee, SpiceCoffee, SyrupCoffee 

def run_task_1():
    """Instantiates different coffee objects to demonstrate the class hierarchy."""
    print("--- Laboratory 5, Task 1: Hierarchy and Field Check ---")
    
    basic_coffee = Coffee(name="Black Coffee", intensity=Intensity.LIGHT)
    basic_coffee.print_coffee_details()
    print("-" * 30)

    americano = WaterBasedCoffee(name="Americano", intensity=Intensity.NORMAL, ml_of_water=150)
    americano.print_coffee_details()
    print("-" * 30)

    cappuccino = MilkBasedCoffee(name="Cappuccino", intensity=Intensity.STRONG, ml_of_milk=80)
    cappuccino.print_coffee_details()
    print("-" * 30)
    
    pumpkin_spice_latte = SpiceCoffee(name="Pumpkin Spice Latte", intensity=Intensity.STRONG, ml_of_milk=100, mg_of_spice=50)
    pumpkin_spice_latte.print_coffee_details()
    print("-" * 30)
    
    vanilla_cappuccino = SyrupCoffee(name="Vanilla Cappuccino", intensity=Intensity.NORMAL, ml_of_milk=90, syrup_type=SyrupType.VANILLA)
    vanilla_cappuccino.print_coffee_details()
    print("-" * 30)
    
if __name__ == "__main__":
    run_task_1()
