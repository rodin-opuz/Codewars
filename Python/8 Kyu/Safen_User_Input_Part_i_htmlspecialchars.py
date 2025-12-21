def html_special_chars(formData):
    characters = {"<": "&lt;", ">": "&gt;", '"': "&quot;", "&": "&amp;"}
    new = ""
    for i in formData:
        if i in characters: new += characters[i]
        else: new += i
    return new
