Here is the complete corrected code with changed number, variables, and words:

python
```
# 22.4 String Reverse & Palindrome

def reverse_text(text):
    return text[::-1]

def check_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == reverse_text(clean_text)

words = ["noon", "rotor", "Amit", "Surat"]

for item in words:
    reverse_word = reverse_text(item)
    answer = "Yes" if check_palindrome(item) else "No"
    print(f"Word: '{item}' | Reverse: '{reverse_word}' | Palindrome: {answer}")
```