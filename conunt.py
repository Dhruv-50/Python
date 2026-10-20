python
```
# 13.5 Vowel Counter & Character Frequency

def vowel_count(sentence):
    letters = "aeiouAEIOU"
    count = 0

    for letter in sentence:
        if letter in letters:
            count += 1

    return count

def frequency_count(sentence):
    result = {}

    for letter in sentence:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    return result

text = "banana"

print("Word:", text)
print("Number of Vowels:", vowel_count(text))
print("Letter Frequency:", frequency_count(text))
```