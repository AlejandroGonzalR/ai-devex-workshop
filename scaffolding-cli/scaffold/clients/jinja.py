from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from scaffold.client import Client


class Jinja(Client):
    TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

    def __init__(self):
        super().__init__(
            Environment(loader=FileSystemLoader(self.TEMPLATES))
        )

    def render(self, template: str, dest: Path, **ctx):
        content = self.get_template(template).render(**ctx)

        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")


jinja_client = Jinja()
