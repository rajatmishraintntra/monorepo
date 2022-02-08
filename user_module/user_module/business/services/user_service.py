import abc
from typing import List

from user_module.common.constants import DependenciesConstant as DC


class AbstractUserService(abc.ABC):
    @abc.abstractmethod
    def __init__(self, query: object, user_dependencies: object) -> None:
        self.query = query
        self.unique_validators = user_dependencies(DC.VALIDATORS)[DC.UNIQUE_VALIDATOR]()
        db_tables = user_dependencies(DC.DB_TABLES)
        self.QueryBuilder = user_dependencies(DC.QUERY_BUILDER)(db_tables)
        self.custom_dict = user_dependencies(DC.CUSTOM_DICT)()

    @abc.abstractmethod
    def create(self, data: object) -> object:
        usr = self.query.execute(self.QueryBuilder.create_user(data))
        _id = int(*[x.id for x in usr])
        if data.permissions != []:
            self.query.execute(self.QueryBuilder.create_permissions(_id, data))
        return dict(id=_id)

    @abc.abstractmethod
    def get_list(self) -> List[object]:
        users = self.query.execute(self.QueryBuilder.get_users_list())
        return self.bind_permissions(users)

    @abc.abstractmethod
    def get_single(self, pk: int) -> List[object]:
        return self.bind_permissions(
            self.query.execute(self.QueryBuilder.get_single_user(pk))
        )

    @abc.abstractmethod
    def get_single_email(self, email: str) -> List[object]:
        return self.bind_permissions(
            self.query.execute(self.QueryBuilder.get_single_user_by_email(email))
        )

    @abc.abstractmethod
    def get_auth_token(self, email: str, password: str) -> dict:
        row = self.get_single_email(email)
        return row

    @abc.abstractmethod
    def bind_permissions(self, rows: object):
        resp = []
        for i in rows:
            permissions = self.query.execute(
                self.QueryBuilder.get_permissions_by_user_id(i.id)
            )
            data = self.custom_dict.set_attr(i)
            data.permissions = [x.permissions_id for x in permissions]
            resp.append(data)
        return resp
