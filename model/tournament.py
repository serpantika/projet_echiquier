from tinydb import TinyDB


class Tournament:
    def __init__(self, name, localisation, date, nbturn, rounds, timecontrol, description, players):
        self.name = name
        self.localisation = localisation
        self.date = date
        self.nbturn = nbturn
        self.rounds = rounds
        self.timecontrol = timecontrol
        self.description = description
        self.players = players

    def create_tournament(info_tournament, list_players):
        tournament = Tournament(info_tournament['name'], info_tournament['localisation'],
                                info_tournament['date'], info_tournament['nbturn'],
                                info_tournament['rounds'], info_tournament['timecontrol'],
                                info_tournament['description'], list_players)
        name = info_tournament['name']
        tournament.save(name)

    def save(self, name):
        dbtournament = TinyDB(name+'.json')
        tournament_table = dbtournament.table(name)
        serialized_tournament = {'name': self.name,
                                 'localisation': self.localisation,
                                 'date': self.date,
                                 'nbturn': self.nbturn,
                                 'rounds': self.rounds,
                                 'timecontrol': self.timecontrol,
                                 'description': self.description,
                                 'players': self.players}
        tournament_table.insert(serialized_tournament)



