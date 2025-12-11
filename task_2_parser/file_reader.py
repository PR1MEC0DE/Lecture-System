# file_reader.py

class FileReader:
    """
    Utility class designed to handle file reading operations.
    It's designed to be reusable, as the lab task suggests.
    """

    @staticmethod
    def read_file_into_string(path: str) -> str:
        """
        Reads the entire content of a file located at 'path' into one string.
        We'll handle the file path and potential errors right here.
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                # Read everything at once. Clean and simple.
                text_content = f.read()
            return text_content
        except FileNotFoundError:
            # If the file doesn't exist, we need to let the user know.
            print(f"Error: The file specified by the path '{path}' was not found.")
            return None
        except Exception as e:
            # Catch any other reading issues, like permission errors.
            print(f"An unexpected error occurred while reading the file: {e}")
            return None
