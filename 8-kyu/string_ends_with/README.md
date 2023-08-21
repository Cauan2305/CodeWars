## Exercise: "String ends with?"

### Objective:

The goal of the exercise is to check if a string (text) ends with a specified substring (ending).

### Input:

- A string `text` which is the main text.
- A string `ending` which is the substring we want to check if it's at the end of `text`.

### Output:

- Returns `True` if `text` ends with `ending`.
- Returns `False` otherwise.

### Examples:

- `solution('abc', 'bc')` - The string "abc" ends with "bc", so the function returns `True`.
- `solution('abc', 'd')` - The string "abc" doesn't end with "d", so the function returns `False`.

## Solution:

The proposed solution uses string slicing to check if the end of `text` matches `ending`.

### Explanation of the solution:

1. `text[-len(ending):]`: This part of the code grabs the last characters of `text` that have the same length as `ending`.
   - For example, if `text = 'abc'` and `ending = 'bc'`, then `text[-len(ending):]` will be `'bc'`.

2. `ending in text[-len(ending):]`: This expression checks if `ending` is contained in the last characters of `text`. If it is, it means `text` ends with `ending`.

3. `return True if ... else False`: This is a conditional construct that returns `True` if the previous condition is true and `False` otherwise.

### Simplification:

The solution could be simplified to:

```python
def solution(text:str, ending:str):
    return True if ending in text[-len(ending):] else False 
```

```python
def solution(text:str, ending:str):
    return text.endswith(ending)
```


The built-in `endswith()` function in Python does exactly what the exercise asks for, checking if a string ends with a certain substring.