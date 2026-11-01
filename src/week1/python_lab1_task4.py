def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    return len("".join(text.split()))


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    numbers = []
    for word in text.split():
        cleaned = word.rstrip(".,!?:;")
        # Handle optional leading negative sign
        if cleaned.startswith("-") and len(cleaned) > 1:
            digits_part = cleaned[1:]
        else:
            digits_part = cleaned

        if digits_part.isdigit():
            numbers.append(int(cleaned))

    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)

    num_sum = sum(nums)
    num_avg = float(num_sum / len(nums)) if nums else 0.0

    return {
        "characters": chars,
        "words": words,
        "numbers": nums,
        "sum": num_sum,
        "average": num_avg,
    }


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    user_input = input("Enter text: ")
    res = analyze_text(user_input)

    print(f"Characters (no spaces): {res['characters']}")
    print(f"Words: {res['words']}")
    print(f"Numbers: {res['numbers']}")
    print(f"Sum: {res['sum']}")
    print(f"Average: {res['average']:.2f}")