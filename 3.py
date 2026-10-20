python
```
import string

text_data = (
    "Mumbai is a popular city known for its business and culture.\n"
    "Many people visit Mumbai to explore its famous tourist attractions.\n"
    "The city of Mumbai is also known for its busy lifestyle."
)

with open("city_text2.txt", "w") as file:
    file.write(text_data)

search_word = input("Enter a word to find its frequency: ").strip()

with open("city_text2.txt", "r") as file:
    text_lines = file.readlines()

line_count = len(text_lines)
character_count = sum(len(line) for line in text_lines)

complete_text = "".join(text_lines)
word_list = complete_text.translate(
    str.maketrans("", "", string.punctuation)
).lower().split()

word_total = len(word_list)
frequency = word_list.count(search_word.lower())

print(f"\nNumber of Lines: {line_count}")
print(f"Number of Words: {word_total}")
print(f"Number of Characters: {character_count}")
print(f"Frequency of '{search_word}': {frequency}")
```