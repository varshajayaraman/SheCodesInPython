class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = -1
        self.tweets = dict()
        self.following = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if self.tweets.get(userId) is None:
            self.tweets[userId] = []
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        if self.tweets.get(userId) is not None:
            heap.extend(self.tweets[userId][-10:])
        # print(self.tweets[userId][-10:])
        if self.following.get(userId) is not None:
            for f in self.following[userId]:
                if self.tweets.get(f) is not None:
                    heap.extend(self.tweets[f][-10:])

        heap = sorted(heap, key=lambda a: a[0])
        # print(heap)
        res = heap[:10]
        # print(res)
        res = [x[1] for x in res]
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.following.get(followerId) is None:
            self.following[followerId] = set([])
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.following.get(followerId) is not None:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)