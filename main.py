
def get_book_text(file_path: str):
    return open(file_path).read()

def get_word_count(text: str):
    return len(text.split())

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

main()
