"""
CP1404/CP5632 Practical
Word Occurrences
"""
word_to_count = {}
words = (input("Text: ")).strip().split(" ")
words.sort()
maximum_word_length = max(len(word) for word in words)
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in word_to_count.items():
    print(f"{word:{maximum_word_length}}: {count}")
