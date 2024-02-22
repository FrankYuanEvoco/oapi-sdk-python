# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class AppWorkflow(object):
    _types = {
        "workflow_id": str,
        "status": str,
        "title": str,
    }

    def __init__(self, d=None):
        self.workflow_id: Optional[str] = None
        self.status: Optional[str] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppWorkflowBuilder":
        return AppWorkflowBuilder()


class AppWorkflowBuilder(object):
    def __init__(self) -> None:
        self._app_workflow = AppWorkflow()

    def workflow_id(self, workflow_id: str) -> "AppWorkflowBuilder":
        self._app_workflow.workflow_id = workflow_id
        return self

    def status(self, status: str) -> "AppWorkflowBuilder":
        self._app_workflow.status = status
        return self

    def title(self, title: str) -> "AppWorkflowBuilder":
        self._app_workflow.title = title
        return self

    def build(self) -> "AppWorkflow":
        return self._app_workflow