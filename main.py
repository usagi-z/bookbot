
from stats import count_words, get_book_text

def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()
