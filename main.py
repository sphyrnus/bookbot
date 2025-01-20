from collections import Counter


def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        filtered_contents = "".join(
            filter(lambda char: char.isalpha() and char != "\n", contents)
        )
    counter = Counter(filtered_contents.lower())
    print("--- Begin report of books/frankenstein.txt ---")
    for key, value in sorted(counter.items(), key=lambda num: num[1], reverse=True):
        print(f"The '{key}' character was found {value} times")
    print("--- End report---")


main()
