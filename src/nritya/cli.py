"""CLI for Nritya."""
from __future__ import annotations
import click
from rich.console import Console
from .dance.forms import DanceFormDatabase
from .dance.poses import DancePoseLibrary
from .dance.mudras import MudraDatabase
from .analyzer.corrector import DanceCorrector
from .report import DanceReport
from .models import DanceForm

console = Console()


@click.group()
def cli() -> None:
    """Nritya - Classical Dance Corrector."""
    pass


@cli.command()
@click.argument("form", type=click.Choice([f.value for f in DanceForm], case_sensitive=False))
def info(form: str) -> None:
    """Show information about a dance form."""
    db = DanceFormDatabase()
    df = DanceForm(form)
    details = db.get_form_details(df)
    console.print(f"\n[bold magenta]{df.value}[/bold magenta]")
    for k, v in details.items():
        if isinstance(v, list):
            console.print(f"  [bold]{k}:[/bold] {', '.join(v)}")
        else:
            console.print(f"  [bold]{k}:[/bold] {v}")


@cli.command()
@click.option("--form", "-f", type=click.Choice([f.value for f in DanceForm], case_sensitive=False), default=None)
def poses(form: str | None) -> None:
    """List dance poses."""
    lib = DancePoseLibrary()
    report = DanceReport()
    if form:
        pose_list = lib.get_poses_by_form(DanceForm(form))
    else:
        pose_list = lib.get_all_poses()
    for p in pose_list:
        report.display_pose(p)


@cli.command()
@click.option("--type", "-t", "mudra_type", type=click.Choice(["asamyuta", "samyuta"]), default=None)
def mudras(mudra_type: str | None) -> None:
    """List mudras (hand gestures)."""
    db = MudraDatabase()
    report = DanceReport()
    if mudra_type == "asamyuta":
        report.display_mudra_list(db.get_asamyuta())
    elif mudra_type == "samyuta":
        report.display_mudra_list(db.get_samyuta())
    else:
        report.display_mudra_list(db.get_all_mudras())


@cli.command()
@click.option("--form", "-f", type=click.Choice([f.value for f in DanceForm], case_sensitive=False), default=None)
def adavus(form: str | None) -> None:
    """List adavus (basic dance steps)."""
    db = DanceFormDatabase()
    adavu_list = db.get_adavus(DanceForm(form) if form else None)
    from rich.table import Table
    table = Table(title="Adavus")
    table.add_column("Name", style="cyan")
    table.add_column("Form", style="yellow")
    table.add_column("Description")
    table.add_column("Difficulty")
    for a in adavu_list:
        table.add_row(a.name, a.dance_form.value, a.description, a.difficulty)
    console.print(table)


@cli.command()
def expressions() -> None:
    """List Navarasas (nine expressions)."""
    db = DanceFormDatabase()
    from rich.table import Table
    table = Table(title="Navarasas - Nine Expressions")
    table.add_column("Rasa", style="bold magenta")
    table.add_column("Description")
    table.add_column("Facial Elements")
    for e in db.get_expressions():
        table.add_row(e.sanskrit_name, e.description, e.facial_elements)
    console.print(table)


if __name__ == "__main__":
    cli()
