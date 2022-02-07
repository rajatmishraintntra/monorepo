class Password:
    @property
    def password(self):
        # validation rule goes here
        return str

    def __init__(self, password: str) -> None:
        self.emailid = password
