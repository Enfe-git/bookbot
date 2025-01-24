def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_contents(book_path)
    book_lenght = len(file_contents.split())
    character_count = count_characters(file_contents)
    print_report(sort_dictionary(character_count), book_lenght, book_path)

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    characters = []
    for key in dict:
        characters.append({"character": key,  "num" : dict[key]})
    characters.sort(reverse=True, key=sort_on)
    return characters
    

def count_characters(file_contents):
    character_count = {}
    for char in file_contents.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def get_book_contents(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def print_report(character_count, book_length, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_length} words found in the document")
    for dict in character_count:
        if dict["character"].isalpha():
            print(f"The '{dict["character"]}' character was found {dict["num"]} times")
    print("--- End report ---")



main()