def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = []
        deck = sorted(deck)
        for i in deck[::-1]:
            #res =[i]+res[-1:]+res[:-1]
            if len(res)>0:
                last = res.pop()
                res.insert(0,last)
            res.insert(0,i)
        return res