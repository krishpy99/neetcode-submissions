class Twitter:

    def __init__(self):
        self.tweets = {}
        self.tweeted_by = {}
        self.tweeted_at = {}
        self.feed = {}
        self.following = {}
        self.followers = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append(tweetId)
        self.tweeted_at[tweetId] = self.time
        self.tweeted_by[tweetId] = userId
        self.pushToFeed(tweetId)
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        return sorted(set(self.feed[userId]), key = lambda x: self.tweeted_at[x])[-1:-11:-1] if userId in self.feed else []

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {}
        if followeeId not in self.following[followerId]:
            self.pushFolloweeToFeed(followerId, followeeId)
        self.following[followerId][followeeId] = 1
        if followeeId not in self.followers:
            self.followers[followeeId] = {}
        self.followers[followeeId][followerId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            del self.following[followerId][followeeId]
        
        if followeeId in self.followers and followerId in self.followers[followeeId]:
            del self.followers[followeeId][followerId]
        #print("hey there", self.feed[followerId])
        self.removeFolloweeFromFeed(followerId, followeeId)
    
    def pushFolloweeToFeed(self, followerId: int, followeeId: int):
        if followerId not in self.feed:
            self.feed[followerId] = []
        if followeeId in self.tweets:
            for tweetId in self.tweets[followeeId]:
                self.feed[followerId].append(tweetId)
    
    def removeFolloweeFromFeed(self, followerId: int, followeeId: int):
        if followerId not in self.feed:
            return
        
        new_list = []
        removed = {}
        for tweetId in self.feed[followerId]:
            if self.tweeted_by[tweetId] != followeeId or tweetId in removed:
                new_list.append(tweetId)
            else:
                removed[tweetId] = 1
        self.feed[followerId] = new_list

    def pushToFeed(self, tweetId: int):
        userId = self.tweeted_by[tweetId]
        if userId not in self.feed:
            self.feed[userId] = []
        self.feed[userId].append(tweetId)
        if userId in self.followers:
            for i in self.followers[userId]:
                if i not in self.feed:
                    self.feed[i] = []
                self.feed[i].append(tweetId)
            

