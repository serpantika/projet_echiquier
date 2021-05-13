class View(object):

    @staticmethod
    def show_number_alpha(players):
        print('--- {} LISTE ---')
        for i, player in enumerate(players):
            print('{}. {}, {}, {}, {}, {}' .format(i+1, player.name,
                                                   player.birthday, player.gender, player.rank, player.point))

    @staticmethod
    def show_number(players):
        print('--- {} LISTE ---')
        for i, player in enumerate(players):
            print('{}. {}, {}, {}, {}, {}'.format(i + 1, player.lastname,player.firstname,
                                                  player.birthday, player.gender, player.rank))

    @staticmethod
    def menu_principal():
        print("/////////_Accueil_/////////\n"
              "-1: Gérer tournois\n"
              "-2: Gérer joueurs\n"
              "-3: Quitter ")
        choice = input()
        return choice

    @staticmethod
    def menu_tournoi():
        print("/////////_Menu-Tournoi_/////////\n"
              "-1: Créer nouveau tournoi\n"
              "-2: Charger tournoi\n"
              "-3: Modifier tournoi\n"
              "-4: Voir information tournoi\n"
              "-5: Retour menu principal")
        choice = input()
        return choice

    @staticmethod
    def menu_joueur():
        print("/////////_Menu-Joueur_/////////\n"
              "-1: Ajouter joueur\n"
              "-2: Modifier joueur\n"
              "-3: Afficher liste joueurs\n"
              "-4: Retour menu principal")
        choice = input()
        return choice

    @staticmethod
    def add_player():
        print("/////////_Ajouter-joueur_/////////\n"
              "Rentrer les informations du joueurs")
        lastname = input("-Nom :")
        firstname = input("-Prénom :")
        birthday = input("-Date de Naissance :")
        gender = input("-Genre :")
        rank = input("-Classement :")
        player = {'lastname': lastname,
                  'firstname': firstname,
                  'birthday': birthday,
                  'gender': gender,
                  'rank': rank}
        print('Ajouter nouveau joueur ?\n'
              '-1 : oui    -2 : non')
        repeat = input()
        return player, repeat

    @staticmethod
    def add_tournament():
        i = 1
        players = list()
        print("/////////_Créer-tournoi_/////////\n"
              "Rentrer les informations du tournoi")
        name = input("-Nom :")
        localisation = input("-Lieu :")
        date = input("-Date :")
        nbturn = input("-Nombre de tour :")
        rounds = input("-Tournées :")
        timecontrol = input("-Contrôle du temps :")
        description = input("-Description :")
        info_tournament = {"name": name,
                           "localisation": localisation,
                           "date": date,
                           "nbturn": nbturn,
                           "rounds": rounds,
                           "timecontrol": timecontrol,
                           "description": description,
                           }
        while i <= 8:
            print("Joueur n°" + str(i))
            lastname = input("-Nom: ")
            firstname = input("-prénom: ")
            player = {"lastname": lastname, "firstname": firstname}
            players.append(player)
            i += 1
        return info_tournament, players

    @staticmethod
    def error():
        print("/////////!!erreur!!/////////\n"
              "Commande inconnus")
