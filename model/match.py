class Match(object):

    def __init__(self, players):
        self.players = players


    def Round_one(players):
        players.sort(key=lambda player: player.rank, reverse=True)
        for player in players:
            print (player.lastname)
