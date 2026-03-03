import click

from scaffold.config import APP_TYPES
from scaffold.microservice.microservice import Create


@click.group()
@click.option('--name',
              help='The environment where the static front-end application should be published.',
              type=click.STRING,
              required=True)
@click.option('--type',
              help='The environment where the static front-end application should be published.',
              type=click.Choice(APP_TYPES),
              required=True)
@click.pass_context
def cli(ctx: object, name: str, type: str) -> None:
    ctx.obj['params'].set('app_name', name)
    ctx.obj['params'].set('type', type)


@click.command('create')
@click.pass_context
def create(ctx: object) -> None:
    app_name = ctx.obj['params'].get('app_name')

    click.echo(f"Generating '{app_name}' application base code...")
    Create(ctx.obj['params']).execute()
    click.echo('Code generated successfully!')


cli.add_command(create)
