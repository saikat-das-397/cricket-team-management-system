from commands.command import Command


class UpdatePlayerCommand(Command):

    def __init__(
        self,
        player,
        old_name,
        old_runs,
        old_balls,
        new_name,
        new_runs,
        new_balls
    ):

        
        self.__player = player

        # Old state
        self.__old_name = old_name
        self.__old_runs = old_runs
        self.__old_balls = old_balls

        # New state
        self.__new_name = new_name
        self.__new_runs = new_runs
        self.__new_balls = new_balls

    # ---------------------------------
    # Execute
    # ---------------------------------

    def execute(self):

        self.__player.set_name(
            self.__new_name
        )

        self.__player.set_runs(
            self.__new_runs
        )

        self.__player.set_balls(
            self.__new_balls
        )

    # ---------------------------------
    # Undo
    # ---------------------------------

    def undo(self):

        self.__player.set_name(
            self.__old_name
        )

        self.__player.set_runs(
            self.__old_runs
        )

        self.__player.set_balls(
            self.__old_balls
        )