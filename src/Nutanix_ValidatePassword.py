def validatePassword(pwd):
    charCount = 5
    spclCharCount = 1
    numCount = 1
    smallCharCount = 1
    blockCharCount = 1

    for i in range(len(pwd)):
        ch = pwd[i]
        if ch.isalpha():
            charCount -= 1
            if ch.isupper():
                blockCharCount -= 1
            else:
                smallCharCount -= 1
        elif ch.isnumeric():
            numCount -= 1
        else:
            spclCharCount -= 1
        if i>=2:
            if pwd[i]==pwd[i-1] and pwd[i]==pwd[i-2]:
                return False

    return charCount <= 0 and spclCharCount <= 0 and numCount <= 0 and smallCharCount <= 0 and blockCharCount <= 0


print(validatePassword("##11AsHg"))
