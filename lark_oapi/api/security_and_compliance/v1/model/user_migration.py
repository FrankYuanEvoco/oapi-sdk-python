# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class UserMigration(object):
    _types = {
        "user_id": int,
        "dest_geo": str,
        "task_id": str,
        "status": str,
        "progress": int,
    }

    def __init__(self, d=None):
        self.user_id: Optional[int] = None
        self.dest_geo: Optional[str] = None
        self.task_id: Optional[str] = None
        self.status: Optional[str] = None
        self.progress: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserMigrationBuilder":
        return UserMigrationBuilder()


class UserMigrationBuilder(object):
    def __init__(self) -> None:
        self._user_migration = UserMigration()

    def user_id(self, user_id: int) -> "UserMigrationBuilder":
        self._user_migration.user_id = user_id
        return self

    def dest_geo(self, dest_geo: str) -> "UserMigrationBuilder":
        self._user_migration.dest_geo = dest_geo
        return self

    def task_id(self, task_id: str) -> "UserMigrationBuilder":
        self._user_migration.task_id = task_id
        return self

    def status(self, status: str) -> "UserMigrationBuilder":
        self._user_migration.status = status
        return self

    def progress(self, progress: int) -> "UserMigrationBuilder":
        self._user_migration.progress = progress
        return self

    def build(self) -> "UserMigration":
        return self._user_migration