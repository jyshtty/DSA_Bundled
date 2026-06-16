"""
Problem: Design Twitter
Link: https://leetcode.com/problems/design-twitter/

Description:
    Design a simplified version of Twitter where users can post tweets,
    follow/unfollow, and see the 10 most recent tweets in their news feed.

Examples:
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.getNewsFeed(1)   # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    twitter.getNewsFeed(1)   # [6, 5]
    twitter.unfollow(1, 2)
    twitter.getNewsFeed(1)   # [5]

Constraints:
    1 <= userId, followerId, followeeId <= 500
    0 <= tweetId <= 10^4
    All tweets have unique IDs.
    At most 3 * 10^4 calls in total.
"""

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.timestamp = 0
        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # userId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # collect tweets from self + all followees
        candidates = list(self.tweets[userId])
        for followee in self.following[userId]:
            candidates.extend(self.tweets[followee])

        # nlargest by timestamp — negative timestamp so we can use min-heap naturally
        top = heapq.nlargest(10, candidates, key=lambda x: x[0])
        return [tweetId for _, tweetId in top]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
