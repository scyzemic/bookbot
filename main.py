
def get_book_text(file_path: str):
    return open(file_path).read()

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(book_text)

main()
