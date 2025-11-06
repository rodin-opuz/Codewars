def validate_word(word):
    letters = []
    word = word.lower()
    counts = []
    for i in word:
        if i not in letters:
            letters.append(i)
            counts.append(word.count(i))
    return len(set(counts)) == 1
