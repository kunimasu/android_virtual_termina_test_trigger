from typing import Final, List, Callable

class TestPlanStep:
    action: Final[str]
    param: Final[str]

    def __init__(self, action, param):
        self.action = action
        self.param = param

    @property
    def dict(self) -> dict:
        return {
            'action': self.action,
            'param': self.param,
        }

class TestPlan:
    version: Final[str]
    title: Final[str]
    device: Final[str]
    os_version: Final[str]
    steps: Final[List[TestPlanStep]]

    def __init__(self, version: str, title: str, device: str, os_version: str, steps: List[TestPlanStep]):
        self.version = version
        self.title = title
        self.device = device
        self.os_version = os_version
        self.steps = steps

    @staticmethod
    def create(obj: any):
        steps: List[TestPlanStep] = []
        for step in obj['steps']:
            for action, param in step.items():
                steps.append(TestPlanStep(action, param))
        device = obj['device']
        os_version = obj['os-version']
        return TestPlan(obj['version'], obj.get('title', f'${device}(${os_version})'), device, os_version, steps)

    @property
    def dict(self) -> dict:
        map_handler: Callable[[TestPlanStep], dict] = lambda x: x.dict
        return {
            'version': self.version,
            'title': self.title,
            'device': self.device,
            'osVersion': self.os_version,
            'steps': list(map(map_handler, self.steps)),
        }