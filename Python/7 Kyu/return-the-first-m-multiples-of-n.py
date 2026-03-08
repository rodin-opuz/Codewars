def multiples(m: int, n: int | float) -> list[int] | list[float]:
    mult = []
    for i in range(1, m + 1):
        mult.append(n * i)
    return mult
