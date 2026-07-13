import heapq

class Twitter:
    #users and tweets uniquely identified by their ids 

    #dict: {userid: [list of all their tweets]}
    #dict: {userId: [SET of followees]}
    TWEET_COUNTER = 0

    def __init__(self):
        self.user_tweets = {}
        self.user_follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.TWEET_COUNTER += 1
        self.user_tweets[userId].append((self.TWEET_COUNTER, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.user_follows.get(userId, set())
        followees.add(userId)  # include self in case not added yet

        heap = []
        # Initialize heap with the most recent tweet from each followee
        for person in followees:
            tweets = self.user_tweets.get(person, [])
            if tweets:
                ts, tweetId = tweets[-1]  # most recent tweet is at end
                idx = len(tweets) - 1
                heapq.heappush(heap, (-ts, tweetId, person, idx))

        result = []
        while heap and len(result) < 10:
            neg_ts, tweetId, person, idx = heapq.heappop(heap)
            result.append(tweetId)
            # Push the next tweet from this user (if exists)
            if idx > 0:
                next_ts, next_id = self.user_tweets[person][idx - 1]
                heapq.heappush(heap, (-next_ts, next_id, person, idx - 1))

        return result
                    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
        
