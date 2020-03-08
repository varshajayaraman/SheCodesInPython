class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        global refDict
        refDict = {}
        for w in wordList:
            for i in range(len(beginWord)):
                if w[:i] + "*" + w[i + 1:] in refDict:
                    refDict[w[:i] + "*" + w[i + 1:]].append(w)
                else:
                    refDict[w[:i] + "*" + w[i + 1:]] = [w]

        refSet = set([beginWord])
        wordSet = set(wordList)
        currLev = 0
        minLev = math.inf
        q = [(beginWord, 1)]
        while len(q) > 0:

            currItem = q.pop(0)
            currWord = currItem[0]
            currLev = currItem[1]
            for i in range(len(currWord)):
                if currWord[:i] + "*" + currWord[i + 1:] in refDict:
                    for word in refDict[currWord[:i] + "*" + currWord[i + 1:]]:
                        if word not in refSet:
                            refSet.add(word)
                            if word == endWord:
                                return currLev + 1
                            q.append((word, currLev + 1))
                            continue
        return 0
