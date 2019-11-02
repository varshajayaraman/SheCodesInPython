def intersection(num1, num2):
    num = set();
    for x in num2:
        if x in num1:
            num.add(x)
    list(num)

    print(num)