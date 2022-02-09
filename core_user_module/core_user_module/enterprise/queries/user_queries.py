from pypika import Table, PostgreSQLQuery
from core_user_module.business.utils.generators import generate_password_hash
from core_user_module.common.constants import DependenciesConstant as DC


class UserQueries:
    def __init__(self, db_tables: dict) -> None:
        self.Table = Table
        self.Query = PostgreSQLQuery
        # tables related to user module
        self.db_user_table = db_tables.get(DC.DB_USER_TABLE)
        self.db_user_permission_intermediate = db_tables.get(
            DC.DB_USER_PERMISSION_INTERMEDIATE
        )

    def create_user(self, data: object):
        table = self.Table(self.db_user_table)
        password = generate_password_hash(data.password.encode("utf-8"))
        q = (
            self.Query.into(table)
                .columns("email", "password", "role_id")
                .insert(data.email, password.decode("utf-8"), data.role)
        )

        return q.get_sql() + "RETURNING id"

    def create_permissions(self, _id, data: object):
        q2 = (
            self.Query.into(self.Table(self.db_user_permission_intermediate))
                .columns("user_id", "permissions_id")
                .insert(*[(_id, i) for i in data.permissions])
        )
        return q2.get_sql() + "RETURNING id"

    def get_single_user(self, pk):
        table = self.Table(self.db_user_table)
        q = self.Query.from_(table).select("*").where(table.id == pk)
        return q.get_sql()

    def get_single_user_by_email(self, email):
        table = self.Table(self.db_user_table)
        q = self.Query.from_(table).select("*").where(table.email == email)
        return q.get_sql()

    def get_users_list(self):
        table = self.Table(self.db_user_table)
        q = self.Query.from_(table).select("*")
        return q.get_sql()

    def get_permissions_by_user_id(self, user_id: int):
        table = self.Table(self.db_user_permission_intermediate)
        q = self.Query.from_(table).select("*").where(table.user_id == user_id)
        return q.get_sql()

    def update_user_query(self):
        raise NotImplementedError
