
python
```
# 25.6 List Comprehension Lab

# (a) Squares of 1-15
square_values = [x**2 for x in range(1, 16)]

# (b) Even numbers 1-40
even_values = [x for x in range(1, 41) if x % 2 == 0]

# (c) Words longer than 3 characters
sentence = "Python makes learning programming fun and interesting"
long_words = [word for word in sentence.split() if len(word) > 3]

# (d) Cubes of odd numbers 1-11
odd_cubes = [x**3 for x in range(1, 12) if x % 2 != 0]

print(f"(a) Squares (1-15)    : {square_values}")
print(f"(b) Evens (1-40)      : {even_values}")
print(f"(c) Words > 3 chars   : {long_words}")
print(f"(d) Odd Cubes (1-11)  : {odd_cubes}")
```