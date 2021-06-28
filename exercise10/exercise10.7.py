def is_anagram(word1, word2):
    """Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams."""
    chars1 = list(word1)
    chars1.remove(" ")

    chars2 = list(word1)
    chars2.remove(" ")
    return sorted(chars1) == sorted(chars2)


print(is_anagram("ЛАЖНИ СТИД КУПАЧА", "НУДИСТИЧКА ПЛАЖА"))
