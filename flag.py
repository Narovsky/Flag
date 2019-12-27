def flag():
    try:
        N = int(input('Введите N: '))
        if N % 2 != 0:
            print('ArgumentError')
            return flag()
    except ValueError as e:
        print(e)
        return flag()

    width = 3 * N
    radius_height = int(N / 2)
    N2 = int(1.5 * N)

    lines = []

    lines.append("#" * (width + 2))  
    lines.extend(["#" + (" " * width) + "#" for i in range(radius_height)])  
    lines.extend(["#" + (" " * (N2 - i - 1)) + "*" + ("o" * i * 2) + "*" + 
                  (" " * (N2 - i - 1)) + "#" for i in range(radius_height)])  

    str = "\n".join(lines)
    lines.reverse()
    return str + "\n".join(lines)


flag()
