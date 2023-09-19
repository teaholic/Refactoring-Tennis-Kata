# -*- coding: utf-8 -*-

class ScoreService:
    tempScore=0

    def score(self, p1points, p2points) -> str:
        result = ""
        for i in range(1, 3):
            if (i == 1):
                self.tempScore = p1points
            else:
                result += "-"
                self.tempScore = p2points
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[self.tempScore]
        return result

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.service = ScoreService()

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        if (self.p1points==self.p2points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if (minusResult==1):
                result ="Advantage player1"
            elif (minusResult ==-1):
                result ="Advantage player2"
            elif (minusResult>=2):
                result = "Win for player1"
            else:
                result ="Win for player2"
        else:
            result = self.service.score(self.p1points, self.p2points)
        return result
