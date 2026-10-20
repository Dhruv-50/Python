python
```
# 27.4 Word Frequency Counter
import re

text = """
Python is easy to learn. Python is useful for coding.
Learning Python improves coding skills and coding knowledge.
"""

# Extract words and convert them to lowercase
words = re.findall(r'\b\w+\b', text.lower())

# Count each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Arrange words by frequency
frequency_list = sorted(
    word_count.items(),
    key=lambda item: item[1],
    reverse=True
)

print(f"{'Word':<15} | {'Count':<10}")
print("-" * 28)

for word, count in frequency_list:
    print(f"{word:<15} | {count:<10}")
```