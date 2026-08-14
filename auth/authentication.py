import hashlib
import re


class AuthenticationService:
    """
    Handles user authentication and input validation.
    """

    USERS = {
        "admin": {
            "password": hashlib.sha256(
                "Admin@123".encode()
            ).hexdigest(),
            "role": "admin"
        },

        "viewer": {
            "password": hashlib.sha256(
                "Viewer@123".encode()
            ).hexdigest(),
            "role": "viewer"
        }
    }

    USERNAME_PATTERN = (
        r"^[A-Za-z][A-Za-z0-9_]{2,19}$"
    )

    PASSWORD_PATTERN = (
        r"^(?=.*[A-Za-z])"
        r"(?=.*\d)"
        r"(?=.*[@$!%*#?&])"
        r".{8,}$"
    )

    # ==========================================
    # Username Validation
    # ==========================================

    @classmethod
    def validate_username(cls, username):

        if not re.fullmatch(
            cls.USERNAME_PATTERN,
            username
        ):
            return False, (
                "Username must be 3–20 characters "
                "and contain only letters, numbers, "
                "and underscores."
            )

        return True, "Valid username."

    # ==========================================
    # Password Validation
    # ==========================================

    @classmethod
    def validate_password(cls, password):

        if not re.fullmatch(
            cls.PASSWORD_PATTERN,
            password
        ):
            return False, (
                "Password must contain at least "
                "8 characters, one letter, one number, "
                "and one special character."
            )

        return True, "Valid password."

    # ==========================================
    # Authentication
    # ==========================================

    @classmethod
    def authenticate(cls, username, password):

        username_valid, _ = cls.validate_username(
            username
        )

        if not username_valid:
            return False, None

        user = cls.USERS.get(username)

        if user is None:
            return False, None

        password_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        if password_hash != user["password"]:
            return False, None

        return True, user["role"]
        