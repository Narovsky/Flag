def flag():
    try:
        N = int(input('Введите N: '))
        if N % 2 != 0:
            print('ArgumentError')
            return flag()
    except ValueError as e:
        print(e)
        return flag()

    w = 3 * N
    rh = int(N / 2)
    n2 = int(1.5 * N)

    lines = []

    lines.append("#" * (w + 2))  # первая строка
    lines.extend(["#" + (" " * w) + "#" for i in range(rh)])  # строки до круга
    lines.extend(["#" + (" " * (n2 - i - 1)) + "*" + ("o" * i * 2) + "*" + (" " * (n2 - i - 1)) + "#" for i in range(rh)])  # круг

    print("\n".join(lines))
    lines.reverse()
    print("\n".join(lines))


flag()
