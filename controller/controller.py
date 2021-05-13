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
            info_tournament, players = View.add_tournament()
            list_players= Player.get_players(players)
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
