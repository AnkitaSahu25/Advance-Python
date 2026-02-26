###Check if two strings are anagrams using set and logic.
s1 = "listen"
s2 = "silent"

if set(s1) == set(s2) and len(s1) == len(s2):
    print("Anagram")
else:
    print("Not anagram")
