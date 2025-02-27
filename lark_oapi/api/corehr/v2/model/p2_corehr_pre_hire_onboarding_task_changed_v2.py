# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .onboarding_task_change import OnboardingTaskChange
from .onboarding_flow_change import OnboardingFlowChange


class P2CorehrPreHireOnboardingTaskChangedV2Data(object):
    _types = {
        "tenant_id": str,
        "pre_hire_id": str,
        "onboarding_task_changes": List[OnboardingTaskChange],
        "onboarding_flow_change": OnboardingFlowChange,
        "onboarding_flow_id": str,
    }

    def __init__(self, d=None):
        self.tenant_id: Optional[str] = None
        self.pre_hire_id: Optional[str] = None
        self.onboarding_task_changes: Optional[List[OnboardingTaskChange]] = None
        self.onboarding_flow_change: Optional[OnboardingFlowChange] = None
        self.onboarding_flow_id: Optional[str] = None
        init(self, d, self._types)


class P2CorehrPreHireOnboardingTaskChangedV2(EventContext):
    _types = {
        "event": P2CorehrPreHireOnboardingTaskChangedV2Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrPreHireOnboardingTaskChangedV2Data] = None
        init(self, d, self._types)
