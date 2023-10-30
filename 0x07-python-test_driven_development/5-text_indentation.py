#!/usr/bin/python3
"""function that prints texts
"""


def text_indentation(text):
    """
    function that prints text with new line every ".", "?", ":" appears
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    for char in chars:
        text = text.replace(char, char + "\n\n")
    new_lines = [lines.strip(" ") for lines in text.split("\n")]
    final = "\n".join(new_lines)
    print(final, end="")
