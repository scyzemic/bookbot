def get_word_count(text: str):
    return len(text.split())


def get_character_counts(text: str):
    characters: dict[str, int] = {}

    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1

    return characters


def format_character_counts(characters: dict[str, int]):
    sorted_chars: list[dict[str, str | int]] = []

    for char, count in characters.items():
        char_dict = {"char": char, "count": count}
        sorted_chars.append(char_dict)

    sorted_chars.sort(key=lambda x: x["count"], reverse=True)

    return sorted_chars
