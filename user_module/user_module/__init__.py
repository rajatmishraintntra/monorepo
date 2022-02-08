from user_module.business.utils.custom import CustomDict
from user_module.common.constants import DependenciesConstant as DC
from user_module.enterprise.queries.user_queries import UserQueries
from user_module.enterprise.validator.unique_validators import UniqueValidator


class UserDependencies:
    def __init__(self) -> None:
        self.depend = {
            DC.QUERY_BUILDER: UserQueries,
            DC.VALIDATORS: {DC.UNIQUE_VALIDATOR: UniqueValidator},
            DC.CUSTOM_DICT: CustomDict,
            DC.DB_TABLES: {
                DC.DB_USER_TABLE: "user_user",
                DC.DB_USER_PERMISSION_INTERMEDIATE: "user_user_permissions",
            },
        }

    def __call__(self, navigator) -> object:
        return self.depend.get(navigator)
