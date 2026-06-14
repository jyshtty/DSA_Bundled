"""
Problem: Reconstruct Itinerary
Link: https://leetcode.com/problems/reconstruct-itinerary/

Description:
    Given a list of airline tickets [from, to], reconstruct the itinerary
    starting from "JFK". Use all tickets exactly once. If multiple valid
    itineraries, return the lexicographically smallest.

Examples:
    Input:  tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    Output: ["JFK","MUC","LHR","SFO","SJC"]

Constraints:
    1 <= tickets.length <= 300
    tickets[i].length == 2
    tickets[i][0] != tickets[i][1]
"""

from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)  # reverse sort so we pop from back in lex order

        result = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            result.append(airport)  # append after exhausting all outgoing edges (Hierholzer's)

        dfs("JFK")
        return result[::-1]
