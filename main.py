import sys
from stats import char_count, count_words, get_book_text, sorted_char_counts

def char_count_report(counts: list):
    for item in counts:
        ch, num = item["char"], item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {filepath}...")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    char_count_report(sorted_char_counts(char_count(text)))
    print('============= END ===============')

main()
