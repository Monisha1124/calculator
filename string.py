def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def count_consonants(s):
    return sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")

def count_uppercase(s):
    return sum(1 for ch in s if ch.isupper())

if __name__ == "__main__":
    s = "Programming"
    print("Vowels:", count_vowels(s))