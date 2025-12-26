from stats import get_num_words, get_num_characters, sorted_list_of_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    text = get_book_text(file_path)
    num_words = get_num_words(text)
    sorted_dict = sorted_list_of_dict(get_num_characters(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for d in sorted_dict:
        #print(not d["char"].isalpha())
        if not d["char"].isalpha():
            continue
        else:
            print(f"{d["char"]}: {d["num"]}")
    print("============= END =============")
def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()
