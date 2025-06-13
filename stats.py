# Returns the number of words in the input string
def get_word_count(book_as_string):
        number_of_words = 0
        word_list = book_as_string.split()  # Split the string into words
        for word in word_list:
                number_of_words +=1         # Count each word
        return number_of_words

# Returns a dictionary with the count of each unique character (lowercased) in the input string
def get_char_count(book_as_string):
        char_count = set()
        unique_char = {}
        lowercase_book = book_as_string.lower()  # Convert to lowercase for case-insensitive counting
        for char in lowercase_book:
               char_count.add(char)              # Collect unique characters
        for i in char_count:
                unique_char[i] = lowercase_book.count(i)  # Count occurrences of each unique character
        return unique_char

# Converts a dictionary of character counts to a sorted list of dicts, descending by count
def sort_dict(dict):
        list_dict = []
        for item in dict:
              list_dict.append({"Character": item, "Number": dict[item]})  # Build list of dicts
        list_dict.sort(reverse=True, key=sort_on)  # Sort by count descending
        return list_dict

# Helper function for sorting by the "Number" key
def sort_on(dict):
        return dict["Number"]