def get_word_count(book_as_string):
        number_of_words = 0
        word_list = book_as_string.split()
        for word in word_list:
                number_of_words +=1
        return number_of_words
def get_char_count(book_as_string):
        char_count = set()
        unique_char = {}
        lowercase_book = book_as_string.lower()
        for char in lowercase_book:
               char_count.add(char)
        for i in char_count:
                unique_char[i] = lowercase_book.count(i)
        return unique_char