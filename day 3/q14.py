import sys

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
  
    vowel_count = sum(1 for char in s if char in vowels)
    return vowel_count

def count_consonants(s: str) -> int:
  
    vowels = "aeiouAEIOU"

    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return consonant_count

def calculate_vowel_consonant_ratio(s: str) -> float | str:
   
    num_vowels = count_vowels(s)
    num_consonants = count_consonants(s)

    if num_consonants == 0:
        if num_vowels == 0:
            return 
        else:
           
            return 
    
    ratio = num_vowels / num_consonants
    return ratio

def main():
    print("Enter a string to calculate its vowel-to-consonant ratio:")
   
    user_input = sys.stdin.readline().strip() 
    
    if not user_input:
        print("No input received. Exiting.")
        return

    vowel_count = count_vowels(user_input)
    consonant_count = count_consonants(user_input)
    ratio_result = calculate_vowel_consonant_ratio(user_input)

    print(f"\nString analyzed: '{user_input}'")
    print(f"Total vowels found: {vowel_count}")
    print(f"Total consonants found: {consonant_count}")

    if isinstance(ratio_result, float):
        print(f"Ratio of vowels to consonants (V:C): {ratio_result:.4f}")
    else:
        print(f"Ratio calculation result: {ratio_result}")

if __name__ == "__main__":
    main()

1