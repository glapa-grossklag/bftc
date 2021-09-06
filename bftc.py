#!/usr/bin/env python3
from sys import stdin, stdout

_prelude = """
#include <stdio.h>

int main(void) {
    char array[65536] = {0};
    char *ptr = array;
"""

_postlude = "}"

_translation = {
    ">": "++ptr;",
    "<": "--ptr;",
    "+": "++*ptr;",
    "-": "--*ptr;",
    ".": "putchar(*ptr);",
    ",": "*ptr = getchar();",
    "[": "while (*ptr) {",
    "]": "}",
}


def translate(src: str, standalone: bool = True) -> str:
    """
    Translate Brainfuck source code to C source code.
    """
    result = [_translation.get(c, "") for c in src]
    result = "".join(result)

    if standalone:
        return _prelude + result + _postlude
    else:
        return result


def main():
    src = stdin.read()
    translation = translate(src)
    stdout.write(translation)


if __name__ == "__main__":
    main()
