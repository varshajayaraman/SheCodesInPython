def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    currWord = ""
    resDict = {}

    for i in range(len(paragraph)):
        if paragraph[i].isalpha():
            currWord += paragraph[i]
        else:
            if len(currWord) > 0:
                currWord = currWord.lower()
                if currWord in resDict.keys():
                    resDict[currWord] += 1
                else:
                    resDict[currWord] = 1
            currWord = ""
    if len(currWord) > 0:
        currWord = currWord.lower()
        if currWord in resDict.keys():
            resDict[currWord] += 1
        else:
            resDict[currWord] = 1
    for word in banned:
        if word in resDict.keys():
            resDict.pop(word)

    freq = -math.inf
    freqword = ""
    for k in resDict.keys():
        if resDict[k] > freq:
            freq = resDict[k]
            freqword = k
    return freqword