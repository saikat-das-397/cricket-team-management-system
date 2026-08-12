class CommandManager:

    def __init__(self):

        self.__undo_stack = []
        self.__redo_stack = []

    # ---------------------------------
    # Execute Command
    # ---------------------------------

    def execute(self, command):

        command.execute()

        self.__undo_stack.append(
            command
        )

        # New action invalidates redo history
        self.__redo_stack.clear()

    # ---------------------------------
    # Undo
    # ---------------------------------

    def undo(self):

        if not self.__undo_stack:
            return False

        command = self.__undo_stack.pop()

        command.undo()

        self.__redo_stack.append(
            command
        )

        return True

    # ---------------------------------
    # Redo
    # ---------------------------------

    def redo(self):

        if not self.__redo_stack:
            return False

        command = self.__redo_stack.pop()

        command.execute()

        self.__undo_stack.append(
            command
        )

        return True

    # ---------------------------------
    # Can Undo
    # ---------------------------------

    def can_undo(self):

        return bool(
            self.__undo_stack
        )

    # ---------------------------------
    # Can Redo
    # ---------------------------------

    def can_redo(self):

        return bool(
            self.__redo_stack
        )