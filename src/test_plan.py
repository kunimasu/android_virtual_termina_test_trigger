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
    format_version: Final[str]
    device: Final[str]
    os_version: Final[str]
    languages: Final[List[str]]
    steps: Final[List[TestPlanStep]]

    def __init__(
        self,
        format_version: str,
        device: str,
        os_version: str,
        languages: List[str],
        steps: List[TestPlanStep]
    ):
        self.format_version = format_version
        self.device = device
        self.os_version = os_version
        self.languages = languages
        self.steps = steps

    @staticmethod
    def create(obj: any):
        format_version = obj['format-version']
        device = obj['device']
        os_version = obj['os-version']
        languages = obj['languages']
        steps: List[TestPlanStep] = []
        for step in obj['steps']:
            for action, param in step.items():
                steps.append(TestPlanStep(action, param))
        return TestPlan(format_version, device, os_version, languages, steps)

    @property
    def dict(self) -> dict:
        map_handler: Callable[[TestPlanStep], dict] = lambda x: x.dict
        return {
            'formatVersion': self.format_version,
            'device': self.device,
            'osVersion': self.os_version,
            'languages': self.languages,
            'steps': list(map(map_handler, self.steps)),
        }
