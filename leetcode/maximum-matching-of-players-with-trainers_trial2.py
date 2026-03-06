class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        player = 0
        for trainer in trainers:
            if trainer >= players[player]:
                player += 1
            if player >= len(players):
                break
        return player
        