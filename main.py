"""One-liner groan-off entry: load the dad joke and print it."""

import pathlib

ENTRY_FILE = "entry.txt"


def load_joke(path=ENTRY_FILE):
    here = pathlib.Path(__file__).resolve().parent
    return (here / path).read_text(encoding="utf-8").strip()


def deliver():
    joke = load_joke()
    print(joke)


if __name__ == "__main__":
    deliver()
