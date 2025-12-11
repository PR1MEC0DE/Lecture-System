# To import the Display class, ensure display.py is accessible (e.g., in the same directory or package)
from display import Display 

def run_task_1():
    """
    Instantiates 3 Display objects and compares them using the class methods.
    """
    
    # Instantiate 3 display objects of type Display.
    print("--- Task 1: Objects & Object Interaction ---")
    print("--- Instantiating Display Objects ---")
    
    # Monitor 1: High Resolution/High PPI (The Sharp One)
    monitor_4k = Display(
        width=3840, 
        height=2160, 
        ppi=163.0, 
        model="UltraSharp 4K"
    )
    print(f"Created: {monitor_4k.model}")

    # Monitor 2: Standard Resolution/Standard PPI (The Big One)
    monitor_wide = Display(
        width=3440, # Changed resolution for a different comparison point
        height=1440, 
        ppi=109.0, 
        model="WideScreen QHD"
    )
    print(f"Created: {monitor_wide.model}")

    # Monitor 3: Lower Resolution/Standard PPI (A Common One)
    monitor_fhd = Display(
        width=1920, 
        height=1080, 
        ppi=93.0, 
        model="Compact FHD"
    )
    print(f"Created: {monitor_fhd.model}")

    # --- Compare the objects (The printed result is descriptive and verbose) ---

    print("\n======================================")
    print("           OBJECT INTERACTION           ")
    print("======================================")

    # 1. Use compareWithMonitor for both size and sharpness
    monitor_4k.compare_with_monitor(monitor_wide)
    
    print("\n--------------------------------------")
    
    # 2. Use compareSize
    monitor_wide.compare_size(monitor_fhd)
    
    print("\n--------------------------------------")

    # 3. Use compareSharpness
    monitor_fhd.compare_sharpness(monitor_4k)
    
if __name__ == "__main__":
    run_task_1()
