class Validator:
    """
    Responsible for validating player data.

    This class contains only business rules.
    """

    MAX_STRIKE_RATE = 400
    MAX_NAME_LENGTH = 50

    @staticmethod
    def validate_player(name, runs, balls):

        # -------------------------
        # Name
        # -------------------------
        if not name.strip():
            return False, "Player name cannot be empty."

        if len(name) > Validator.MAX_NAME_LENGTH:
            return False, "Player name is too long."

        # Optional: letters and spaces only
        if not all(ch.isalpha() or ch.isspace() for ch in name):
            return False, "Player name contains invalid characters."

        # -------------------------
        # Runs
        # -------------------------
        if runs < 0:
            return False, "Runs cannot be negative."

        # -------------------------
        # Balls
        # -------------------------
        if balls <= 0:
            return False, "Balls must be greater than zero."

        # -------------------------
        # Strike Rate
        # -------------------------
        strike_rate = (runs / balls) * 100

        if strike_rate > Validator.MAX_STRIKE_RATE:
            return (
                False,
                f"Strike rate ({strike_rate:.2f}) is unrealistically high."
            )

        return True, "Validation successful."