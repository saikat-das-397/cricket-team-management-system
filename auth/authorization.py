class AuthorizationService:
    """
    Handles role-based authorization.
    """

    ADMIN = "admin"
    VIEWER = "viewer"

    @classmethod
    def can_view(cls, role):
        return role in (
            cls.ADMIN,
            cls.VIEWER
        )

    @classmethod
    def can_modify(cls, role):
        return role == cls.ADMIN

    @classmethod
    def can_save(cls, role):
        return role == cls.ADMIN

    @classmethod
    def can_generate_pdf(cls, role):
        return role == cls.ADMIN

    @classmethod
    def can_generate_charts(cls, role):
        return role in (
            cls.ADMIN,
            cls.VIEWER
        )