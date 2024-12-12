def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # Split the text into words once
        words = file_contents.split()
        
        # Print header
        print("--- Begin report of books/frankenstien.txt ---")

        # Count and print the word count
        count_words(words)
        
        # Count and print the character count
        count_characters(words)

        # Sort and print only the alphabetic character counts
        sort_on(char_count)

        # Print footer
        print("--- End report ---")

def count_words(words):
    word_count = len(words)
    print(f"{word_count} words found in document")

char_count = {}

def count_characters(words):
    for word in words:
        lword = word.lower()
        for char in lword:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(char_count):
    counts = [{"letter":key, "number":value} for key, value in char_count.items()]
    letter_counts = []
    for count in counts:
        if count["letter"].isalpha():
            letter_counts.append(count)

    sorted_letter_counts = sorted(letter_counts, key=lambda x: x["number"], reverse=True)
    for sorted_letter_count in sorted_letter_counts:
        let = sorted_letter_count["letter"]
        num = sorted_letter_count["number"]
        print(f"The '{let}' character was found {num} times")
    return(sorted_letter_counts)


main()

