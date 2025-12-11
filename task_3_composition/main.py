# main.py

# We need the Display class from Task 1
try:
    from task_1_interaction.display import Display
except ImportError:
    print("FATAL ERROR: Ensure 'task_1_interaction' module and 'display.py' are accessible.")
    # For testing, you might need to temporarily copy Display into this folder,
    # but the final solution should correctly import from task_1_interaction.

from assistant import Assistant

def run_task_3():
    """
    Main function to demonstrate class composition (Assistant holding Displays)
    and list iteration.
    """
    print("--- Task 3: Class Composition Demonstration ---")
    
    # 1. Instantiate 3 Display objects (reusing the class from Task 1)
    # Using different specs for variety
    d1 = Display(2560, 1440, 109.0, "Acer Predator")
    d2 = Display(3840, 2160, 140.0, "Dell UltraSharp")
    d3 = Display(1920, 1080, 92.0, "Budget FHD")
    
    print("Created 3 monitor objects (d1, d2, d3).")

    # 2. Instantiate the Assistant class
    my_assistant = Assistant("MonitorAdvisor-A.I.")
    print(f"Created Assistant: {my_assistant._assistant_name}")
    
    print("\n--- Assigning Displays to the Assistant ---")
    
    # 3. Use assignDisplay to add the monitors to the Assistant's list
    my_assistant.assign_display(d1)
    my_assistant.assign_display(d2)
    my_assistant.assign_display(d3)
    
    # 4. Use assist() to perform the sequential comparison (List Iteration)
    print("\n--- Requesting Assistance (Sequential Comparison) ---")
    my_assistant.assist()
    
    # 5. Use buyDisplay() to remove a monitor
    print("\n--- Simulating a Purchase ---")
    # Let's say we decide to buy the sharpest one (d2)
    purchased_monitor = my_assistant.buy_display(d2)
    
    if purchased_monitor:
        print(f"Main Program: Successfully acquired '{purchased_monitor.model}'.")
        print(f"Monitors remaining for {my_assistant._assistant_name}: {len(my_assistant.get_assigned_displays())}")
        
        # Check if the remaining monitors still need comparison
        my_assistant.assist()


if __name__ == "__main__":
    run_task_3()
