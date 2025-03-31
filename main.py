from stats import get_word_count, get_character_counts, format_character_counts


def get_book_text(file_path: str):
    return open(file_path).read()


def main():
    book_text = get_book_text("./books/frankenstein.txt")
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
