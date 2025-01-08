def main():
    file_contents = read_frankenstein()
    num_file_words = count_words(file_contents)
    char_report = get_sorted_char_report(file_contents)
    print(f"{num_file_words} words found in the document")
    for char in char_report:
        print(f"character '{char["char"]}' appears {char["count"]} times")

# return number of words in text
def count_words(text):
    return len(text.split())

def key_count(dict):
    return dict["count"]

def get_sorted_char_report(text):
    char_counts = get_char_dict(text)
    report = []
    for char in char_counts:
        if char.isalpha():
            report.append({"char": char, "count": char_counts[char]})
    report.sort(reverse=True, key=key_count)
    return report

# return dict of number of each character in text
def get_char_dict(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if not char in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    return char_counts

# return string of frakenstein book text
def read_frankenstein():
    with open("books/frankenstein.txt") as f:
        return f.read()

main()