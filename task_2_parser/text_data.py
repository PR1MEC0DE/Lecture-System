# text_data.py

import re

class TextData:
    """
    A class to represent and analyze a text file's data.
    All calculations are done when the object is created (in __init__).
    """

    # We only care about standard English letters (a-z, A-Z).
    VOWELS = "aeiouAEIOU"
    CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    def __init__(self, file_name: str, text: str):
        """
        Constructor that receives the file name and the raw text,
        then calculates all the required metrics instantly.
        """
        self._file_name = file_name
        self._text = text
        
        # Calculate all metrics and store them as internal properties
        self._calculate_metrics()

    def _calculate_metrics(self):
        """
        Internal method to perform all the intensive text parsing calculations.
        """
        
        # 1. Total Letters (only alphabetical characters)
        # Using a regex to find all letters is the cleanest way.
        all_letters = re.findall(r'[a-zA-Z]', self._text)
        self._number_of_letters = len(all_letters)

        # 2. Vowels and Consonants
        # We iterate over the found letters to count vowels and consonants.
        self._number_of_vowels = 0
        self._number_of_consonants = 0
        
        for char in all_letters:
            if char in self.VOWELS:
                self._number_of_vowels += 1
            elif char in self.CONSONANTS:
                # Although we used regex to filter, this is an extra check
                self._number_of_consonants += 1

        # 3. Sentences
        # A simple approach: count periods, exclamation marks, and question marks.
        # This might not be perfect for all texts, but it's a good estimate for the task.
        sentence_markers = ['.', '!', '?']
        self._number_of_sentences = sum(self._text.count(marker) for marker in sentence_markers)
        
        # 4. Longest Word
        # First, split the text into words. We'll use a regex to separate by
        # non-word characters and then filter out empty strings.
        words = re.findall(r'\b\w+\b', self._text)
        
        # Now find the longest word among the extracted list.
        if words:
            # max() with the key=len function automatically finds the word with the max length.
            self._longest_word = max(words, key=len)
        else:
            self._longest_word = ""

    # --- Getter Methods (as specified in the task UML) ---

    def get_filename(self) -> str:
        """Returns the name of the file being processed."""
        return self._file_name

    def get_text(self) -> str:
        """Returns the original, raw text content."""
        return self._text

    def get_number_of_vowels(self) -> int:
        """Returns the total count of vowels found in the text."""
        return self._number_of_vowels

    def get_number_of_consonants(self) -> int:
        """Returns the total count of consonants found in the text."""
        return self._number_of_consonants

    def get_number_of_letters(self) -> int:
        """Returns the total count of alphabetical letters."""
        return self._number_of_letters

    def get_number_of_sentences(self) -> int:
        """Returns the estimated number of sentences based on terminal punctuation."""
        return self._number_of_sentences

    def get_longest_word(self) -> str:
        """Returns the longest word found in the text."""
        return self._longest_word
