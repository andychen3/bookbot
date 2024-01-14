def main():
    path_to_file = "/Users/andychen/workspace/bookbot/books/frankenstein.txt"
    file_contents = open_file(path_to_file)
    print(f"There are {get_count(file_contents)} words in this document..")
    get_letters(file_contents)


def get_count(file):
    return len(file.split())


def open_file(path):
    with open(path) as f:
        return f.read()


def get_letters(file):
    letter_count_dict = {}

    for char in file:
        lowercase_letter = char.lower()
        if lowercase_letter not in letter_count_dict:
            letter_count_dict[lowercase_letter] = 1
        else:
            letter_count_dict[lowercase_letter] += 1

    for key, val in letter_count_dict.items():
        print(f"{key}: {val}")


if __name__ == "__main__":
    main()
