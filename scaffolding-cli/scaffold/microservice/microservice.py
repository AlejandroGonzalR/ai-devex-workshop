import abc

from datetime import datetime
from pathlib import Path

from scaffold.clients.jinja import jinja_client
from scaffold.commands import ParametersBag, Step
from scaffold.config.app_environments import map_app_templates


class MicroserviceParameters(ParametersBag):
    def __init__(self, params: ParametersBag) -> None:
        super(MicroserviceParameters, self).__init__(bag=params.all())

    @property
    def app_name(self) -> str:
        return self.get('app_name')

    @property
    def app_type(self) -> str:
        return self.get('type')


class MicroserviceStep(Step, abc.ABC):
    def __init__(self, params: ParametersBag) -> None:
        super(MicroserviceStep, self).__init__(MicroserviceParameters(params))

    @property
    def jinja(self):
        return jinja_client


class Create(MicroserviceStep):
    def execute(self) -> None:
        app_root = Path(".generated", self.params.app_name)

        pkg = f"com.example.{self.params.app_name}"

        ctx = {
            "service_name": self.params.app_name,
            "package": pkg,
            "created": datetime.utcnow().isoformat(),
        }

        for template, destination in map_app_templates(pkg):
            self.jinja.render(template, app_root / destination, **ctx)
