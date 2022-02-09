class UserID:
    @property
    def userid(self):
        # validation rule goes here
        return int

    def __init__(self, userid: int) -> None:
        self.userid = userid
