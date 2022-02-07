from typing import List

from user_module.business.entities.user import AbstractUser
from user_module.business.value_object.email import EmailID
from user_module.business.value_object.password import Password
from user_module.business.value_object.userid import UserID


class UserDTO(AbstractUser):
    _id: UserID
    email: EmailID
    password: Password

    def __init__(
        self,
        email: EmailID,
        password: Password = None,
        role: object = None,
        permissions: List[object] = None,
        _id: UserID = None,
    ) -> None:
        self._id = _id if not None else 0
        self.email = email
        self.password = password
        self.role = role
        self.permissions = permissions
