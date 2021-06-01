class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = [str(len(s)) for s in strs]
        res = [".".join(res)]
        res = res + ["#"] + strs
        return "".join(res)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        li = s.split('#')
        # print(li)
        lengths = li.pop(0).split('.')
        if len(li) == 1:
            str_arr = li[0]
        else:
            # print(li[1:])
            str_arr = "#".join(li)
        res = []
        start = 0
        for l in lengths:
            res.append(str_arr[start:start + int(l)])
            start += int(l)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))