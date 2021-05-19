from tinydb import TinyDB, Query


class Player:

    def __init__(self, lastname, firstname, birthday, gender, rank, point):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.rank = int(rank)
        self.point = point
    def create_player(info_player):
        player = Player(info_player['lastname'], info_player['firstname'], info_player['birthday'],
                        info_player['gender'], info_player['rank'], 0)
        player.save()

    @staticmethod
    def get_players_alpha():
        listplayers = TinyDB('listplayers.json')
        players_table = listplayers.table('players')
        serialized_players = players_table.all()
        players = list()
        for serialized_player in serialized_players:
            player = Player(serialized_player['lastname'], serialized_player['firstname'], serialized_player['birthday']
                            , serialized_player['gender'], serialized_player['rank'], serialized_player['point'])
            players.append(player)
        players.sort(key=lambda player: player.lastname )
        return players

    @staticmethod
    def get_players_rank():
        listplayers = TinyDB('listplayers.json')
        players_table = listplayers.table('players')
        serialized_players = players_table.all()
        players = list()
        for serialized_player in serialized_players:
            player = Player(serialized_player['lastname'], serialized_player['firstname'], serialized_player['birthday']
                            , serialized_player['gender'], serialized_player['rank'], serialized_player['point'])
            players.append(player)
        players.sort(key=lambda player: player.rank)
        return players

    def save(self):
        listplayers = TinyDB('listplayers.json')
        players_table = listplayers.table('players')
        serialized_player = {'lastname': self.lastname,
                             'firstname': self.firstname,
                             'birthday': self.birthday,
                             'gender': self.gender,
                             'rank': self.rank,
                             'point': self.point}
        if listplayers.search(Query()['lastname'] == self.lastname):
            print("joueur déjà inscrit")
        else:
            players_table.insert(serialized_player)

    def serial_player(player):
        serialized_player = {'lastname': player.lastname,
                             'firstname': player.firstname,
                             'birthday': player.birthday,
                             'gender': player.gender,
                             'rank': player.rank,
                             'point': player.point}
        return serialized_player

    def get_tournament_players_rank(tournament):
        serialized_tournament_players = tournament.players
        players = list()
        for serialized_player in serialized_tournament_players:
            player = Player(serialized_player['lastname'], serialized_player['firstname'], serialized_player['birthday']
                            , serialized_player['gender'], serialized_player['rank'], serialized_player['point'])
            players.append(player)
        players.players.sort(key=lambda player: player.rank)
        return players