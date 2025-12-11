# main.py (UPDATED - TASK 3 CHECK)

from intensity import Intensity
from syrup_type import SyrupType
from coffee import Coffee, WaterBasedCoffee, MilkBasedCoffee, SpiceCoffee, SyrupCoffee 

def run_task_3_demonstration():
    """Demonstrates the class-specific make methods and recipe reuse."""
    
    print("\n" + "="*50)
    print("--- Laboratory 5, Task 3: Recipe Logic and Reuse Check ---")
    print("="*50)

    # 1. Americano (Base + Water)
    americano = WaterBasedCoffee(
        name="Americano",
        intensity=Intensity.NORMAL,
        ml_of_water=150
    )
    print("\n[Recipe: Americano]")
    americano.make_americano()
    
    # 2. Pumpkin Spice Latte (Base + Milk + Spice)
    pumpkin_spice_latte = SpiceCoffee(
        name="Pumpkin Spice Latte",
        intensity=Intensity.STRONG,
        ml_of_milk=100,
        mg_of_spice=50
    )
    print("\n[Recipe: Pumpkin Spice Latte]")
    # This calls make_cappuccino(), which in turn calls make()
    pumpkin_spice_latte.make_pumpkin_spice_latte() 
    
    # 3. Vanilla Cappuccino (Base + Milk + Syrup)
    vanilla_cappuccino = SyrupCoffee(
        name="Vanilla Syrup Cappuccino",
        intensity=Intensity.NORMAL,
        ml_of_milk=90,
        syrup_type=SyrupType.VANILLA
    )
    print("\n[Recipe: Vanilla Syrup Cappuccino]")
    vanilla_cappuccino.make_syrup_cappuccino()
    
    print("\n" + "="*50)

if __name__ == "__main__":
    # We run only the Task 3 demonstration for clean output
    run_task_3_demonstration()
