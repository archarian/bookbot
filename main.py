def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # Split the text into words once
        words = file_contents.split()
        
        # Count and print the word count
        count_words(words)
        
        # Count and print the character count
        count_characters(words)

def count_words(words):
    word_count = len(words)
    print(f"Word count: {word_count}")

def count_characters(words):
    char_count = {}
    for word in words:
        lword = word.lower()
        for char in lword:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    print("Character count:", char_count)
    return char_count

main()

