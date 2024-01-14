def main():
    path_to_file = "/Users/andychen/workspace/bookbot/books/frankenstein.txt"
    file_contents = open_file(path_to_file)
    word_count = get_count(file_contents)
    sorted_list = get_letters(file_contents)
    generate_report(word_count, sorted_list, path_to_file)


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

    new_list = sorted(letter_count_dict.items(), key=lambda x: x[1], reverse=True)
    return new_list


def generate_report(word_count, sorted_list, path_to_file):
    report_title = path_to_file.split("/")[-1]
    print(f"--- Begin report of document {report_title} ---")
    print(f"{word_count} words found in the document")
    print()
    for word, count in sorted_list:
        if word.isalpha():
            print(f"The '{word}' character was found {count} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
