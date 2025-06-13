import sys

# Check for correct number of command-line arguments
if (len(sys.argv)) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

# Import analysis functions from stats.py
from stats import get_word_count
from stats import get_char_count
from stats import sort_dict

# Reads the entire contents of the book file and returns as a string
def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents

def main():
        # Get the total word count
        num_words = get_word_count(get_book_text(sys.argv[1]))
        # Get a dictionary of character counts
        num_chars = get_char_count(get_book_text(sys.argv[1]))
        # Sort the character counts in descending order
        ordered_list = sort_dict(num_chars)
        # Print output header and results
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {sys.argv[1]}")
        print ("----------- Word Count ----------")
        print (f"Found {num_words} total words")
        print ("--------- Character Count -------")
        # Print only alphabetic characters and their counts
        for item in ordered_list:
                if item["Character"].isalpha():
                        print (f"{item["Character"]}: {item["Number"]}")
        print ("============= END ===============")

main()