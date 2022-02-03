def cityKorToEng(a, b, city):

    for i in range(0, len(a)):
        if a[i] == city:
            print(b[i])
            return b[i]
