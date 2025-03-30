def get_word_count(text: str):
    return len(text.split())


def get_character_counts(text: str):
    characters: dict[str, int] = {}

    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1

    return characters
