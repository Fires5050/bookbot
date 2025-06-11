from stats import get_word_count
from stats import get_char_count
def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents
def main():
        num_words = get_word_count(get_book_text("books/frankenstein.txt"))
        num_chars = get_char_count(get_book_text("books/frankenstein.txt"))
        print (f"{num_words} words found in the document")
        for character in num_chars:
                number = num_chars[character]
                print (f"'{character}': {number}")
main()