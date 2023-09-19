# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class ScoringService(ABC):

    @abstractmethod
    def can_handle(self, p1points, p2points) -> bool:
        pass

    @abstractmethod
    def score(self, p1points, p2points) -> str:
        pass


class EqualScoringService(ScoringService):

    def can_handle(self, p1points, p2points) -> bool:
        return p1points == p2points

    def score(self, p1points, p2points) -> str:
        return {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(p1points, "Deuce")


class DifferentScoringService(ScoringService):

    def can_handle(self, p1points, p2points) -> bool:
        return p1points >= 4 or p2points >= 4

    def score(self, p1points, p2points) -> str:
        minusResult = p1points - p2points
        if (minusResult == 1):
            return "Advantage player1"
        elif (minusResult == -1):
            return "Advantage player2"
        elif (minusResult >= 2):
            return "Win for player1"
        else:
            return "Win for player2"


class GenericScoringService(ScoringService):

    def can_handle(self, p1points, p2points) -> bool:
        return True

    def score(self, p1points, p2points) -> str:
        tempScore = 0
        result = ""
        for i in range(1, 3):
            if (i == 1):
                tempScore = p1points
            else:
                result += "-"
                tempScore = p2points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[tempScore]
        return result


class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.services = [EqualScoringService(), DifferentScoringService(), GenericScoringService()]

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        for service in self.services:
            if service.can_handle(self.p1points, self.p2points):
                return service.score(self.p1points, self.p2points)
