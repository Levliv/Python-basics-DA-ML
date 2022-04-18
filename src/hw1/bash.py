from typing import List
import os


def head(filename: str, lines: int = 5):
    if lines < 0:
        raise RuntimeError("Number of lines must be positive")
    with open(filename) as file:
        for line_number, line in enumerate(file, start=1):
            if line_number > lines:
                break
            print(line, end="")


def tail(filename: str, lines: int = 5):
    lines -= 1
    if lines < 0:
        raise RuntimeError("Number of lines must be positive")
    with open(filename) as file:
        data = list(file)[-lines:]
        print("".join(data))


def nl(filename: str):
    current_line = 1
    with open(filename) as file:
        for line in file:
            if line.strip():
                print(f"{current_line}: {line}", end="")
                current_line += 1
            else:
                print(line, end="")


def wc(filename: str):
    total_lines, total_words, total_symbols = 0, 0, 0
    with open(filename) as file:
        symbols = os.path.getsize(filename)
        words = 0
        for line in file:
            total_lines += 1
            words += len(line.split())
        total_words += words
        total_symbols += symbols
        total_lines += 1
    print(f"lines = {total_lines}")
    print(f"words = {total_words}")
    print(f"symbols = {total_symbols}")
