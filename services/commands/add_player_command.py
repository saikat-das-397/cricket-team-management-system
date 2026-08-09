from commands.command import Command


class AddPlayerCommand(Command):

    def __init__(self, team, player):

        self.__team = team
        self.__player = player

    # ---------------------------------
    # Execute
    # ---------------------------------

    def execute(self):

        self.__team.add_player(
            self.__player
        )

    # ---------------------------------
    # Undo
    # ---------------------------------

    def undo(self):

        self.__team.delete_player(
            self.__player.get_name()
        )