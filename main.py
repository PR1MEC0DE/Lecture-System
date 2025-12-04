# main.py (Final update for Day 4)
from data_importer import DataImporter
from classifier import Classifier

if __name__ == '__main__':
    importer = DataImporter()
    all_aliens = importer.load_to_classes() # This loads the objects

    classifier = Classifier()

    print("\n--- Running Classification (Day 4) ---")
    for alien in all_aliens:
        # Pass the alien object to the classifier
        result_message = classifier.classify_species(alien)
        print(f"  {result_message}")

    print("\n--- Final Classified Objects ---")
    for alien in all_aliens:
        # The classified_universe attribute has now been updated
        print(alien)
