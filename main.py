from stats import get_word_count, get_character_counts, format_character_counts
import sys


def get_book_text(file_path: str):
    return open(file_path).read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    characters = get_character_counts(book_text)
    sorted_characters = format_character_counts(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character in sorted_characters:
        if str(character["char"]).isalpha():
            print(f"{character['char']}: {character['count']}")

    print("============= END ===============")


main()
