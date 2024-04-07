#!/usr/bin/python3
"""5 text indentation module.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.
    Args:
        text: The text string.
    Returns:
        Nothing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for separator in ".:?":
        text = (separator + "\n\n").join(
            [ln.strip(" ") for ln in text.split(separator)])

    print(text, end="")
