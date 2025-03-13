import re

def validate_email(email):
    """Validates an email address using regex."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def find_phone_numbers(text):
    """Finds phone numbers in a text using regex."""
    pattern = r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    return re.findall(pattern, text)

def replace_words(text, old_word, new_word):
    """Replaces all occurrences of a word with another word using regex."""
    pattern = r"\b" + re.escape(old_word) + r"\b"  # Use re.escape for special chars
    return re.sub(pattern, new_word, text)

def extract_dates(text):
    """Extracts dates in YYYY-MM-DD format using regex."""
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    return re.findall(pattern, text)

def extract_urls(text):
    """Extracts URLs from a text using regex."""
    pattern = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?"
    return re.findall(pattern, text)

def example_match_search():
    """Demonstrates re.match() and re.search()."""
    string = "The quick brown fox"

    # re.match()
    match_at_start = re.match(r"The", string)
    match_not_at_start = re.match(r"quick", string)

    print("\n--- re.match() vs. re.search() ---")
    print(f"match_at_start: {match_at_start}")
    print(f"match_not_at_start: {match_not_at_start}")

    # re.search()
    search_at_start = re.search(r"The", string)
    search_anywhere = re.search(r"quick", string)

    print(f"search_at_start: {search_at_start}")
    print(f"search_anywhere: {search_anywhere}")

def main():
    # Email validation
    email = "test.user@example.com"
    print(f"'{email}' is valid email: {validate_email(email)}")
    email = "invalid_email"
    print(f"'{email}' is valid email: {validate_email(email)}")

    # Phone number extraction
    text = "My phone number is 123-456-7890 or (123) 456-7890. Also +1 123 456 7890"
    phone_numbers = find_phone_numbers(text)
    print(f"Phone numbers found: {phone_numbers}")

    # Word replacement
    text = "The quick brown fox jumps over the lazy dog."
    new_text = replace_words(text, "fox", "cat")
    print(f"Replaced text: {new_text}")

    # Date extraction
    text = "Dates: 2023-10-26, 2024-01-01, invalid-date"
    dates = extract_dates(text)
    print(f"Dates found: {dates}")

    # URL extraction
    text = "Visit https://www.example.com or http://example.org/path"
    urls = extract_urls(text)
    print(f"URLs found: {urls}")

    # Match vs Search example
    example_match_search()

if __name__ == "__main__":
    main()