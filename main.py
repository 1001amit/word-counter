import argparse

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of words in a text file.")
    parser.add_argument("file_path", nargs="?", help="The path to the text file.")
    args = parser.parse_args()

    if args.file_path:
        file_path = args.file_path
    else:
        file_path = input("Enter the file path: ")
    
    num_words = count_words(file_path)
    
    if num_words is not None:
        print(f"Number of words: {num_words}")
