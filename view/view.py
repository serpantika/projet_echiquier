class View(object):

    @staticmethod
    def show_number_alpha(players):
        print(f"{'-' * 50} Liste de Joueur {'-' * 52}")
        print(f"{'id'.center(10)} | "
              f"{'Nom'.center(25)} | "
              f"{'Prenom'.center(25)} | "
              f"{'Date de naissance'.center(20)} | "
              f"{'Genre'.center(10)} | "
              f"{'Rank'.center(10)}"
              f"\n{'-' * 119}")
        for i, player in enumerate(players):
            print(f"{str(i + 1).center(10)} | "
                  f"{str(player.lastname).center(25)} | "
                  f"{str(player.firstname).center(25)} | "
                  f"{str(player.birthday).center(20)} | "
                  f"{str(player.gender).center(10)} | "
                  f"{str(player.rank).center(10)}"
                  f"\n{'-' * 119}")

    @staticmethod
    def show_number_rank(players):
        print(f"{'*' * 50} Liste de Joueur {'*' * 52}")
        print(f"{'id'.center(10)} | "
                  f"{'Nom'.center(25)} | "
                  f"{'Prenom'.center(25)} | "
                  f"{'Date de naissance'.center(20)} | "
                  f"{'Genre'.center(10)} | "
                  f"{'Rank'.center(10)}"
                  f"\n{'-' * 119}")
        for i, player in enumerate(players):
            print(f"{str(i+1).center(10)} | "
                  f"{str(player.lastname).center(25)} | "
                  f"{str(player.firstname).center(25)} | "
                  f"{str(player.birthday).center(20)} | "
                  f"{str(player.gender).center(10)} | "
                  f"{str(player.rank).center(10)}"
                  f"\n{'-' * 119}")

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
              "-2: Lancer tournois\n"
              "-3: Charger tournoi\n"
              "-4: Modifier tournoi\n"
              "-5: Voir information tournoi\n"
              "-6: Retour menu principal")
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
    def classement_choice_allplayers():
        print('/////////Classement/////////\n'
              '-1: Par nom\n'
              '-2: par rang ')
        alpha_or_rank = input()
        return alpha_or_rank

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
        return info_tournament

    @staticmethod
    def choice_players():
        choice_player = input("-Choisir numéro joueur: ")
        return choice_player

    @staticmethod
    def error():
        print("/////////!!erreur!!/////////\n"
              "Commande inconnus")

    @staticmethod
    def start_tournament():
        print("/////////Choix-tournois/////////\n")
        name = input("Nom du tournois à lancer :")
        return name
