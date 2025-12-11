# main.py (FINAL CODE - TASK 4: BARISTA LAYER)

from intensity import Intensity
from syrup_type import SyrupType
from barista import Barista # <--- ONLY Barista is the primary import!

# NOTE: For the objects to be created and passed, we must temporarily import the types. 
# The spirit of the rule is that MAIN DOES NOT USE their methods directly.
from coffee import WaterBasedCoffee, SpiceCoffee, SyrupCoffee 


def run_task_4_demonstration():
    """
    Demonstrates the Barista layer fulfilling the order, completing the layered architecture.
    """
    
    # 1. Create the Barista instance
    barista = Barista("The TUM Coffee Master")

    # 2. Define the order list (main.py creates the objects but does NOTHING with them)
    order = [
        WaterBasedCoffee(
            name="Americano",
            intensity=Intensity.NORMAL,
            ml_of_water=150
        ),
        SpiceCoffee(
            name="Pumpkin Spice Latte",
            intensity=Intensity.STRONG,
            ml_of_milk=100,
            mg_of_spice=50
        ),
        SyrupCoffee(
            name="Vanilla Syrup Cappuccino",
            intensity=Intensity.NORMAL,
            ml_of_milk=90,
            syrup_type=SyrupType.VANILLA
        )
    ]
    
    # 3. Pass the entire responsibility to the Barista layer (The only call from main.py)
    barista.fulfill_order(order)
    
if __name__ == "__main__":
    run_task_4_demonstration()
