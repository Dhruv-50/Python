python
```
# 12.4 Anagram Checker
def check_anagram(text1, text2):
    a = text1.lower().replace(" ", "")
    b = text2.lower().replace(" ", "")
    return sorted(a) == sorted(b)

pairs = [
    ("listen", "silent"),
    ("earth", "heart"),
    ("below", "elbow"),
    ("cat", "dog"),
    ("study", "dusty"),
    ("inch", "chin")
]

for first, second in pairs:
    result = "Anagrams" if check_anagram(first, second) else "Not Anagrams"
    print(f"'{first:<9}' and '{second:<9}' -> {result}")
```