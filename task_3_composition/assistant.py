# assistant.py
try:
    from task_1_interaction.display import Display
except ImportError:
    print("WARNING: Could not import 'Display' from task_1_interaction. Make sure your Python path is set correctly.")

class Assistant:
    """
    The Assistant class demonstrates composition by holding a list of Display objects.
    Its job is to help compare and manage the assigned monitors.
    """

    def __init__(self, name: str):
        """
        Constructor for the Assistant. Initializes its name and an empty list
        to store the Display objects.
        """
        self._assistant_name = name
        # Composition: The Assistant HAS-A List of Displays.
        self._assigned_displays = []

    # --- Methods for Managing Displays ---

    def assign_display(self, d: Display):
        """
        Implementation Detail: Adds a Display object to the assigned_displays list.
        This is how the Assistant gets monitors to work with.
        """
        self._assigned_displays.append(d)
        print(f"[{self._assistant_name}]: Assigned display '{d.model}' to the list.")

    def buy_display(self, d: Display) -> Display:
        """
        Implementation Detail: Removes a specified Display object from the list,
        returning the reference to that display (simulating a purchase/removal).
        """
        try:
            self._assigned_displays.remove(d)
            print(f"[{self._assistant_name}]: Successfully removed '{d.model}' (Simulating Purchase).")
            return d
        except ValueError:
            # Handle the case where the display is not in the list.
            print(f"[{self._assistant_name}]: Error: Display '{d.model}' was not found in the assigned list.")
            return None

    # --- Analysis Method ---

    def assist(self):
        """
        Implementation Detail: Iterates through the assigned Displays list,
        comparing each Display object sequentially to give advice.
        """
        num_displays = len(self._assigned_displays)
        print(f"\n[{self._assistant_name}]: Starting sequential comparison for {num_displays} assigned displays...")

        if num_displays < 2:
            print(f"[{self._assistant_name}]: Need at least two monitors to compare!")
            return

        # Start with the first display and compare it to every subsequent display.
        for i in range(num_displays):
            current_display = self._assigned_displays[i]
            
            # Compare the current display with all monitors that come after it in the list.
            for j in range(i + 1, num_displays):
                next_display = self._assigned_displays[j]
                
                print(f"\n--- Comparing Monitor {i+1} ({current_display.model}) with Monitor {j+1} ({next_display.model}) ---")
                
                # We reuse the compareWithMonitor method from the Display class (Code Reuse)
                current_display.compare_with_monitor(next_display)
                
        print(f"\n[{self._assistant_name}]: Comparison cycle complete. I hope this assisted your choice!")

    # Optional Getter for the list (not strictly required by UML, but helpful)
    def get_assigned_displays(self):
        return self._assigned_displays

