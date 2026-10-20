python
```
# 21.6 String Reverse & Palindrome

def reverse_text(text):
    return text[::-1]

def check_palindrome(text):
    new_text = text.lower().replace(" ", "")
    return new_text == reverse_text(new_text)

words = ["madam
```