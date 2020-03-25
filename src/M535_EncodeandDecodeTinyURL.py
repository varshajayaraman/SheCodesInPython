class Codec:

    def __init__(self):
        self.count = 1
        self.buf = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.hmap = {}
        self.r = Random()

    def getKey(self):
        c = 5
        key = ""
        while c > 0:
            key += self.buf[self.r.randint(0, 61)]
            c -= 1
        return key

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.getKey()
        while key in self.hmap:
            key = self.getKey()
        self.hmap[key] = longUrl
        self.count += 1
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        keyL = shortUrl.split("http://tinyurl.com/")
        # print(shortUrl, keyL)
        return self.hmap[keyL[1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))