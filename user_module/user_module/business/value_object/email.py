class EmailID:
    @property
    def emailid(self):
        # validation rule goes here
        return str

    def __init__(self, emailid: str) -> None:
        self.emailid = emailid
