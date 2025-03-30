from stats import get_word_count, get_character_counts


def get_book_text(file_path: str):
    return open(file_path).read()


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book_text)
    characters = get_character_counts(book_text)
    print(f"{word_count} words found in the document")
    print(characters)


main()
