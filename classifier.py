# classifier.py
from alien_species import AlienSpecies

class Classifier:
    """
    Applies classification rules to assign an AlienSpecies to a universe.
    """
    # Define simple rules: If any of these features are present, assign the universe.
    CLASSIFICATION_RULES = {
        "solar power": "Kryptonian Universe",
        "icy breath": "Arcturian Universe",
        "three legs": "Zorpian Universe",
        # Add more complex rules here later if needed!
    }

    def classify_species(self, alien: AlienSpecies):
        """
        Iterates through the alien's features and applies the classification rules.
        """
        for feature in alien.features:
            if feature in self.CLASSIFICATION_RULES:
                # Assign the universe and stop checking
                alien.classified_universe = self.CLASSIFICATION_RULES[feature]
                return f"Classified {alien.name} as {alien.classified_universe}"
        
        # If no rule matches, set a default
        alien.classified_universe = "Unknown Universe"
        return f"Could not classify {alien.name}, assigned to {alien.classified_universe}"
