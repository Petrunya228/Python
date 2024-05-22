import re


def my_t9(digits):
    keypad = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    with open('/usr/share/dict/words', 'r') as file:
        words = set(word.strip().lower() for word in file)

    pattern = '^' + ''.join(keypad[digit][0] for digit in digits) + '$'

    matching_words = [word for word in words if re.match(pattern, word)]

    return matching_words


# Пример использования
result = my_t9('22736368')
print(result)