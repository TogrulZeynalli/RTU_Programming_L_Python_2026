def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""
    char_count = len(text)
    word_count = len(text.split())
    has_python = "python" in text.lower()

    return char_count, word_count, has_python


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    user_text = input("Enter a sentence: ")
    chars, words, has_py = analyze_sentence(user_text)

    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {has_py}")