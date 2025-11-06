def make_backronym(acronym):
    phrase = []
    for i in acronym.upper():
        phrase.append(dictionary[i])
    return " ".join(phrase)
