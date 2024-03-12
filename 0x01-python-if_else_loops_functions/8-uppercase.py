#!/usr/bin/python3


def uppercase(s):
    result = ""

    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(uppercase_char)
        else:
            # Add non-lowercase characters to the result
            result += "{}".format(char)

    # Print the concatenated result with a newline
    print(result)
