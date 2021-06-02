from view import View
from model import Player
from model import Tournament
from model import Match

class Controller(object):

    @staticmethod
    def start_menu_principal():
        View.menu_principal()
        choice = input()
        Controller.choice_menu_principal(choice)

    def choice_menu_principal(menu_choice):
        if menu_choice == "1":
            View.menu_tournoi()
            choice = input()
            Controller.choice_menu_tournament(choice)
        elif menu_choice == "2":
            View.menu_joueur()
            choice = input()
            Controller.choice_menu_joueur(choice)
        elif menu_choice == "3":
            quit()
        else:
            View.error()
            Controller.start_menu_principal()

    def choice_menu_tournament(menu_choice):
        if menu_choice == "1":
            list_players = list()
            match_players = list()
            View.add_tournament()
            info_tournament = input().replace(" ",'').split(sep = ',')
            tournament = {"name": info_tournament[0],
                               "localisation": info_tournament[1],
                               "date": info_tournament[2],
                               "nbturn": info_tournament[3],
                               "rounds": info_tournament[4],
                               "timecontrol": info_tournament[5],
                               "description": info_tournament[6],
                               }
            players = Player.get_players_alpha()
            nb_players = 0
            while nb_players <=7:
                nb_players += 1
                View.show_number_alpha(players)
                View.choice_players()
                choice_player = int(input())
                choice_player -= 1
                player = players[choice_player]
                players.__delitem__(choice_player)
                match_players.append(player)
                serialized_player = Player.serial_player(player)
                list_players.append(serialized_player)
            Match.Round_one(match_players)
            Tournament.create_tournament(tournament, list_players)
            View.menu_tournoi()
            choice = input()
            Controller.choice_menu_tournament(choice)
        elif menu_choice == "2":
            pass
        elif menu_choice == "3":
            pass
        elif menu_choice == "4":
            pass
        elif menu_choice == "5":
            pass
        elif menu_choice == "6":
            Controller.start_menu_principal()
        else:
            View.error()
            Controller.start_menu_principal()

    def choice_menu_joueur(menu_choice):
        if menu_choice == "1":
            repeat = True
            while repeat:
                View.add_player()
                info_player = input().replace(' ', '').split(sep=",")
                print(info_player)
                player = {'lastname': info_player[0],
                          'firstname': info_player[1],
                          'birthday': info_player[2],
                          'gender': info_player[3],
                          'rank': info_player[4]}
                View.repeat_addplayer()
                repeat = input()
                Player.create_player(player)
                if repeat == "1":
                    repeat = True
                else:
                    repeat = False
            View.menu_joueur()
            choice = input()
            Controller.choice_menu_joueur(choice)
        elif menu_choice == "2":
            pass
        elif menu_choice == "3":
            View.classement_choice_allplayers()
            alpha_or_rank = input()
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

        elif menu_choice == "4":
            Controller.start_menu_principal()
        else:
            View.error()
            Controller.start_menu_principal()
