def lottery(s):
    num = ""
    for i in s:
        if i not in num and i in "1234567890":
            num += i
    if num == "": return "One more run!"
    else: return num
