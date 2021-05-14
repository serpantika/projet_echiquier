from view import View
from model import Player
from model import Tournament


class Controller(object):

    @staticmethod
    def start_menu_principal():
        choice = View.menu_principal()
        Controller.choice_menu_principal(choice)

    def choice_menu_principal(choice):
        if choice == "1":
            choice = View.menu_tournoi()
            Controller.choice_menu_tournament(choice)
        elif choice == "2":
            choice = View.menu_joueur()
            Controller.choice_menu_joueur(choice)
        elif choice == "3":
            quit()
        else:
            View.error()
            Controller.start_menu_principal()

    def choice_menu_tournament(choice):
        if choice == "1":
            list_players = list()
            info_tournament = View.add_tournament()
            players = Player.get_players_alpha()
            nb_players = 0
            while nb_players <=7:
                nb_players += 1
                View.show_number_alpha(players)
                choice_player = int(View.choice_players())
                choice_player -= 1
                player = players[choice_player]
                players.__delitem__(choice_player)
                list_players.append(player)
            print(list_players)
            Tournament.create_tournament(info_tournament,list_players)
            choice = View.menu_tournoi()
            Controller.choice_menu_tournament(choice)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            Controller.start_menu_principal()
        else:
            View.error()
            Controller.start_menu_principal()

    def choice_menu_joueur(choice):
        if choice == "1":
            repeat = True
            while repeat:
                info_player, repeat = View.add_player()
                Player.create_player(info_player)
                if repeat == "1":
                    repeat = True
                else:
                    repeat = False
                    choice = View.menu_joueur()
                    Controller.choice_menu_joueur(choice)
        elif choice == "2":
            pass
        elif choice == "3":
            alpha_or_rank = View.classement_choice_allplayers()
            while alpha_or_rank != "1" or alpha_or_rank != "2":
                if alpha_or_rank == "1":
                    players = Player.get_players_alpha()
                    View.show_number_alpha(players)
                    choice = View.menu_joueur()
                    Controller.choice_menu_joueur(choice)
                if alpha_or_rank == "2":
                    players = Player.get_players_rank()
                    View.show_number_rank(players)
                    choice = View.menu_joueur()
                    Controller.choice_menu_joueur(choice)
                View.error()
                alpha_or_rank = View.classement_choice_allplayers()

        elif choice == "4":
            Controller.start_menu_principal()
        else:
            View.error()
            Controller.start_menu_principal()
