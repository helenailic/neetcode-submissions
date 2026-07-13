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
        followees = set(followees)
        followees.add(userId)  # ensure self-follow
        mostRecentTweets = []
        for person in followees:
            for timestamp, tweetId in self.user_tweets.get(person, []):
                mostRecentTweets.append((timestamp, tweetId))
        mostRecentTweets.sort(reverse=True)
        return [t[1] for t in mostRecentTweets[:10]]
                    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
        
