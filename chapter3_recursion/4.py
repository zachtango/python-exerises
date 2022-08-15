# Chapter 3 Exercise 4 Reverse String

def reverse_string(text: str):
    if not text:
        return ''

    return text[-1] + reverse_string(text[:-1])

tests = ['A', 'ABC', 'abcdefghi']

for t in tests:
    print(reverse_string(t))