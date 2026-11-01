def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        cleaned_name = "Stranger"
    else:
        cleaned_name = cleaned_name.capitalize()

    return f"Hello, {cleaned_name}! Welcome to Python!"


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    user_name = input("Enter your name: ")
    print(greet_user(user_name))