def swap_case(s):
    swapped_str = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                swapped_str+=char.lower()
            elif char.islower():
                swapped_str+=char.upper()
        else:
            swapped_str+=char
    return swapped_str