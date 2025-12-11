# main.py

import sys
from file_reader import FileReader
from text_data import TextData

def main():
    """
    The main method, responsible for reading command-line arguments
    and printing the TextData object's information.
    """
    
    # Task requirement: get the file to be parsed from the args (sys.argv)
    
    # sys.argv[0] is always the script name itself, so we need at least one more argument.
    if len(sys.argv) < 2:
        print("Error: Please provide the path to the text file(s) as a command-line argument.")
        # We can suggest the user how to run the script.
        print("Usage: python main.py <path/to/your/file.txt>")
        return

    # For Task 2, we only process the first file path provided in args.
    file_path = sys.argv[1]
    
    # 1. Read the file using our reusable FileReader
    print(f"Attempting to read file at: {file_path}")
    raw_text = FileReader.read_file_into_string(file_path)

    if raw_text is None:
        # File reading failed (e.g., FileNotFoundError was handled internally)
        return

    # 2. Create the TextData object, which immediately parses and calculates everything
    file_name_only = file_path.split('/')[-1] # Simple way to get just the file name
    text_data_object = TextData(file_name_only, raw_text)

    # 3. Print the object of textData info in the main() method
    print("\n=============================================")
    print(f"   Analysis Results for: {text_data_object.get_filename()}")
    print("=============================================")
    print(f"Total Letters:        {text_data_object.get_number_of_letters()}")
    print(f"    Vowels Count:     {text_data_object.get_number_of_vowels()}")
    print(f"    Consonants Count: {text_data_object.get_number_of_consonants()}")
    print(f"Sentence Count:       {text_data_object.get_number_of_sentences()}")
    print(f"Longest Word:         '{text_data_object.get_longest_word()}'")
    print("=============================================")


if __name__ == "__main__":
    main()
