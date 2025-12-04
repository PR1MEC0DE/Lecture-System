class AlienSpecies:
    """
    Represents an individual alien species in the classification system.
    """
    def __init__(self, id, name, features):
        # Attributes mapped directly from the input JSON
        self.id = id
        self.name = name
        self.features = features  # Expected to be a list of strings

        # Attribute to store the classification result (to be used in Day 4)
        self.classified_universe = None

    def __str__(self):
        """
        Provides a human-readable string representation of the object for testing.
        """
        universe_status = self.classified_universe if self.classified_universe else "Unclassified"
        return (
            f"--- Alien Species: {self.name} (ID: {self.id}) ---\n"
            f"  Features: {', '.join(self.features)}\n"
            f"  Classification: {universe_status}\n"
        )
