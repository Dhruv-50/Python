python
```
# 26.8 List Comprehension Lab

# (a) Squares of 1-12
square_list = [n**2 for n in range(1, 13)]

# (b) Even numbers 1-30
even_list = [n for n in range(1, 31) if n % 2 == 0]

# (c) Words longer than 5 characters
text = "Computer science helps students develop useful skills"
word_list = [w for w in text.split() if len(w) > 5]

# (d) Cubes of odd numbers 1-9
cube_list = [n**3 for n in range(1, 10) if n % 2 != 0]

print(f"(a) Squares (1-12)   : {square_list}")
print(f"(b) Evens (1-30)     : {even_list}")
print(f"(c) Words > 5 chars  : {word_list}")
print(f"(d) Odd Cubes (1-9)  : {cube_list}")
```