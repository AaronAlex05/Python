def string(s: str):
    """
    Analyzes a string and returns counts for vowels, consonants, digits, 
    special characters, and words.
    """
    vowels_set = set("aeiouAEIOU")
    vowels = 0
    consonants = 0
    digits = 0
    special_chars = 0
    
    # Clean the string for word count
    words = len(s.split())
    
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1
        elif not char.isspace():
            special_chars += 1
            
    return {
        "vowels": vowels,
        "consonants": consonants,
        "digits": digits,
        "special_chars": special_chars,
        "words": words
    }

def main():
    print("--- String Program ---")
    user_input = input("Enter a string: ")
    
    results = string(user_input)
    
    print(f"\n'{user_input}'")
    print(f"{'Vowels:':<20} {results['vowels']}")
    print(f"{'Consonants:':<20} {results['consonants']}")
    print(f"{'Digits:':<20} {results['digits']}")
    print(f"{'Special Chars:':<20} {results['special_chars']}")
    print(f"{'Word Count:':<20} {results['words']}")

if __name__ == "__main__":
    main()
