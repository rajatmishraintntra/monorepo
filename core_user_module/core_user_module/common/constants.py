from enum import Enum


class DependenciesConstant(Enum):
    VALIDATORS = "validators"
    UNIQUE_VALIDATOR = "unique_validator"
    QUERY_BUILDER = "query_builder"
    CUSTOM_DICT = "custom_dict"
    DB_TABLES = "db_tables"
    DB_USER_TABLE = "db_user_table"
    DB_USER_PERMISSION_INTERMEDIATE = "db_user_permission_intermediate"
