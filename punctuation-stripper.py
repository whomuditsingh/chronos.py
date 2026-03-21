import string
import os

def clean_text_file(input_filename, output_filename):

    # 1. Check if the input file actually exists
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' was not found.")
        return

# 2. Create the translation table (The "Filter")
# This maps every punctuation character to None (deleting it)
    table = str.maketrans('', '', string.punctuation)

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            raw_content = file.read()
            
# 3. Apply the filter
            clean_content = raw_content.translate(table)
            
# Optional: Clean up extra whitespace/newlines
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(clean_content)
            
        print(f"Success! Cleaned text saved to: {output_filename}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
# Example: If you have a file named 'notes.txt'
    clean_text_file('input.txt', 'cleaned_output.txt')