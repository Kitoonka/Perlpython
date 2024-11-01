def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    # Check if the normalized word is the same forwards and backwards
    return normalized_word == normalized_word[::-1]

# Example usage
print(is_palindrome("radar"))
print(is_palindrome("level"))
print(is_palindrome("python"))

