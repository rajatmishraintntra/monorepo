from typing import List

from core_user_module.business.services.user_service import AbstractUserService
from core_user_module.business.utils.generators import *
from core_user_module.enterprise.dtos.user import UserDTO


class UserService(AbstractUserService):
    def __init__(self, query: object, user_dependencies: object):
        super().__init__(query, user_dependencies)

    def create(self, data: UserDTO):
        """AI is creating summary for create

        Args:
            data (UserDTO): [description]

        Returns:
            [type]: [description]
        """
        return super().create(data)

    def get_list(self) -> List[UserDTO]:
        """AI is creating summary for get_list

        Returns:
            List[UserDTO]: [description]
        """
        rows = super().get_list()
        return list(
            map(
                lambda x: UserDTO(
                    _id=x.id,
                    email=x.email,
                    password=x.password,
                    role=x.role_id,
                    permissions=x.permissions,
                ).__dict__,
                rows,
            )
        )

    def get_single(self, pk: int) -> List[UserDTO]:
        row = super().get_single(pk)
        return map(
            lambda x: UserDTO(
                _id=x.id,
                email=x.email,
                password=x.password,
                role=x.role_id,
                permissions=x.permissions,
            ).__dict__,
            row,
        )

    def bind_permissions(self, rows: object):
        return super().bind_permissions(rows)

    def get_single_email(self, email: str) -> List[object]:
        return super().get_single_email(email)

    def get_auth_token(self, email: str, password: str) -> dict:
        row = super().get_auth_token(email, password)
        if row:
            payload = [dict(id=x.id, email=x.email) for x in row]
            token = generate_token({"data": payload})
            return dict(token=token)
        return dict(error="user not found")

    def read_token(self, token: str):
        return decode_token(token)
