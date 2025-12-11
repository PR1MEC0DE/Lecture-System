class Display:
    """
    Represents a computer display/monitor with size and sharpness characteristics.
    Attributes: width, height (for size), ppi (pixels per inch for sharpness), and model.
    """
    
    # The __init__ method acts as the constructor.
    def __init__(self, width: int, height: int, ppi: float, model: str):
        self.width = width
        self.height = height
        self.ppi = ppi
        self.model = model

    def get_total_pixels(self) -> int:
        """Calculates the total number of pixels (used for size comparison)."""
        return self.width * self.height

    # --- Comparison Methods (Object Interaction) ---

    def compare_size(self, other_display):
        """
        Compares the size of this Display object with another Display object.
        Comparison is based on the total number of pixels.
        """
        this_size = self.get_total_pixels()
        other_size = other_display.get_total_pixels()
        
        print(f"--- Comparing Size: {self.model} vs {other_display.model} ---")
        
        if this_size > other_size:
            print(f"{self.model} is **BIGGER** than {other_display.model}. ({this_size:,} pixels > {other_size:,} pixels)")
        elif this_size < other_size:
            print(f"{self.model} is **SMALLER** than {other_display.model}. ({this_size:,} pixels < {other_size:,} pixels)")
        else:
            print(f"{self.model} is the **SAME SIZE** as {other_display.model}. ({this_size:,} pixels)")

    def compare_sharpness(self, other_display):
        """
        Compares the sharpness (PPI) of this Display object with another Display object.
        """
        print(f"--- Comparing Sharpness (PPI): {self.model} vs {other_display.model} ---")
        
        if self.ppi > other_display.ppi:
            print(f"{self.model} is **SHARPER** than {other_display.model}. ({self.ppi:.2f} PPI > {other_display.ppi:.2f} PPI)")
        elif self.ppi < other_display.ppi:
            print(f"{self.model} is **LESS SHARP** than {other_display.model}. ({self.ppi:.2f} PPI < {other_display.ppi:.2f} PPI)")
        else:
            print(f"{self.model} has the **SAME SHARPNESS** as {other_display.model}. ({self.ppi:.2f} PPI)")

    def compare_with_monitor(self, other_display):
        """
        Performs a combined comparison of both size and sharpness between the two monitors.
        The result should be descriptive and verbose.
        """
        print(f"\n*** Detailed Comparison: {self.model} vs {other_display.model} ***")

        this_size = self.get_total_pixels()
        other_size = other_display.get_total_pixels()

        # 1. Compare Size
        if this_size > other_size:
            size_result = "Bigger in size"
        elif this_size < other_size:
            size_result = "Smaller in size"
        else:
            size_result = "The same size"
        
        # 2. Compare Sharpness
        if self.ppi > other_display.ppi:
            sharpness_result = "Sharper"
        elif self.ppi < other_display.ppi:
            sharpness_result = "Less sharp"
        else:
            sharpness_result = "The same sharpness"
        
        # 3. Verbose Summary
        print(f"Conclusion for {self.model} compared to {other_display.model}:")
        print(f"* Size: {self.model} is {size_result} ({this_size/1000000:.2f}M vs {other_size/1000000:.2f}M pixels).")
        print(f"* Sharpness: {self.model} is {sharpness_result} ({self.ppi:.2f} PPI vs {other_display.ppi:.2f} PPI).")
