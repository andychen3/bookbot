def main():
    path_to_file = "/Users/andychen/workspace/bookbot/books/frankenstein.txt"
    file_contents = open_file(path_to_file)
    print(f"There are {get_count(file_contents)} words in this document..")


def get_count(file):
    return len(file.split())


def open_file(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
