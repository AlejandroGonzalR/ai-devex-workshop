import click

from scaffold.commands import ParametersBag
from scaffold.microservice import commands as microservice


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.pass_context
def cli(ctx: object) -> None:
    ctx.obj = {'params': ParametersBag()}


cli.add_command(microservice.cli, 'microservice')
