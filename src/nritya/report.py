"""Report generation for Nritya."""
from __future__ import annotations
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .models import DanceAnalysis, DancePose, Mudra, Adavu


class DanceReport:
    """Generate rich reports for dance analysis."""

    def __init__(self) -> None:
        self.console = Console()

    def display_analysis(self, analysis: DanceAnalysis) -> None:
        color = "green" if analysis.overall_score >= 85 else "yellow" if analysis.overall_score >= 70 else "red"
        self.console.print(Panel(
            f"[bold]{analysis.pose_name}[/bold] ({analysis.dance_form.value})\n"
            f"Score: [{color}]{analysis.overall_score}/100[/{color}]\n"
            f"{analysis.feedback}",
            title="Pose Analysis"))
        if analysis.corrections:
            table = Table(title="Corrections")
            table.add_column("Joint", style="cyan")
            table.add_column("Current", style="red")
            table.add_column("Target", style="green")
            table.add_column("Deviation")
            table.add_column("Suggestion")
            table.add_column("Severity")
            for c in analysis.corrections:
                table.add_row(c.joint_name, f"{c.current_angle:.1f}", f"{c.target_angle:.1f}",
                             f"{c.deviation:.1f}", c.suggestion, c.severity)
            self.console.print(table)

    def display_pose(self, pose: DancePose) -> None:
        self.console.print(Panel(f"[bold cyan]{pose.name}[/bold cyan]\n{pose.description}\nDifficulty: {pose.difficulty}\nTips: {pose.tips}",
                                  title=pose.dance_form.value))
        if pose.joint_angles:
            table = Table(title="Reference Joint Angles")
            table.add_column("Joint", style="cyan")
            table.add_column("Angle", style="green")
            table.add_column("Tolerance", style="yellow")
            for ja in pose.joint_angles:
                table.add_row(ja.joint_name, f"{ja.angle_degrees}", f"+/- {ja.tolerance}")
            self.console.print(table)

    def display_mudra(self, mudra: Mudra) -> None:
        self.console.print(Panel(
            f"[bold magenta]{mudra.name}[/bold magenta] ({mudra.mudra_type.value})\n"
            f"{mudra.description}\n\nFingers: {mudra.fingers}\n"
            f"Usage: {', '.join(mudra.usage)}",
            title="Mudra"))

    def display_mudra_list(self, mudras: list[Mudra]) -> None:
        table = Table(title="Mudras (Hand Gestures)")
        table.add_column("Name", style="bold cyan")
        table.add_column("Type", style="yellow")
        table.add_column("Description")
        table.add_column("Fingers")
        for m in mudras:
            table.add_row(m.name, m.mudra_type.value, m.description, m.fingers)
        self.console.print(table)
