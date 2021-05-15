from tinydb import TinyDB, Query


class Player:

    def __init__(self, lastname, firstname, birthday, gender, rank):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    def create_player(info_player):
        player = Player(info_player['lastname'], info_player['firstname'], info_player['birthday'],
                        info_player['gender'], info_player['rank'])
        player.save()

    def get_players_alpha():
        listplayers = TinyDB('listplayers.json')
        players_table = listplayers.table('players')
        serialized_players = players_table.all()
        players = list()
        for serialized_player in serialized_players:
            player = Player(serialized_player['lastname'], serialized_player['firstname'], serialized_player['birthday']
                            , serialized_player['gender'], serialized_player['rank'])
            players.append(player)
        players.sort(key=lambda player: player.lastname )
        return players

    def get_players_rank():
        listplayers = TinyDB('listplayers.json')
        players_table = listplayers.table('players')
        serialized_players = players_table.all()
        players = list()
        for serialized_player in serialized_players:
            player = Player(serialized_player['lastname'], serialized_player['firstname'], serialized_player['birthday']
                            , serialized_player['gender'], serialized_player['rank'])
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
                             'rank': self.rank}
        if listplayers.search(Query()['lastname'] == self.lastname):
            print("joueur déjà inscrit")
        else:
            players_table.insert(serialized_player)

    def serial_player(player):
        serialized_player = {'lastname': player.lastname,
                             'firstname': player.firstname,
                             'birthday': player.birthday,
                             'gender': player.gender,
                             'rank': player.rank}
        return serialized_player