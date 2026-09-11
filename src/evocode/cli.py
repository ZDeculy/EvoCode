"""EvoCode single-line CLI shell.

No model or tool execution is performed in this feature.
"""

from __future__ import annotations

import argparse
from importlib.metadata import version

from rich.console import Console
from rich.rule import Rule
from rich.text import Text

from evocode.ui import show_welcome


ACCENT = "#F3A66A"
PRIMARY = "#9AAED0"
SECONDARY = "#9AA4B8"
MUTED = "#667085"


def _prompt(console: Console) -> str:
    """Read one user input in a Claude Code-like terminal style."""

    console.print(Rule(style=MUTED))

    message = console.input(
        f"[bold {ACCENT}]❯[/] "
    ).strip()

    console.print(Rule(style=MUTED))

    return message


def _show_help(console: Console) -> None:
    """Render available shell commands."""

    console.print()

    help_text = Text()

    help_text.append("  /help", style=f"bold {PRIMARY}")
    help_text.append("       Show available commands\n", style=SECONDARY)

    help_text.append("  /exit", style=f"bold {PRIMARY}")
    help_text.append("       Exit EvoCode\n", style=SECONDARY)

    help_text.append(
        "  Ctrl+C / Ctrl+D",
        style=f"bold {PRIMARY}",
    )
    help_text.append(
        "   Exit EvoCode",
        style=SECONDARY,
    )

    console.print(help_text)
    console.print()


def _show_not_connected(console: Console) -> None:
    """Show placeholder response before Model Client exists."""

    console.print()
    console.print(
        f"  [{SECONDARY}]●[/] "
        f"[{PRIMARY}]Model is not connected yet.[/]"
    )
    console.print(
        f"    [{SECONDARY}]Model Client will be added in a later feature.[/]"
    )
    console.print()


def _show_unknown_command(
    console: Console,
    command: str,
) -> None:
    """Render unknown command feedback."""

    console.print()
    console.print(
        f"  [{ACCENT}]Unknown command:[/] "
        f"[{PRIMARY}]{command}[/]"
    )
    console.print(
        f"  [{SECONDARY}]Type /help for available commands.[/]"
    )
    console.print()


def interact(console: Console) -> int:
    """Run the local interactive shell."""

    while True:
        try:
            message = _prompt(console)

        except (EOFError, KeyboardInterrupt):
            console.print()
            console.print(
                f"[{SECONDARY}]Goodbye from [/]"
                f"[bold {PRIMARY}]Evo[/]"
                f"[bold {ACCENT}]Code[/]"
                f"[{SECONDARY}].[/]"
            )
            return 0

        if not message:
            continue

        if message == "/exit":
            console.print()
            console.print(
                f"[{SECONDARY}]Goodbye from [/]"
                f"[bold {PRIMARY}]Evo[/]"
                f"[bold {ACCENT}]Code[/]"
                f"[{SECONDARY}].[/]"
            )
            return 0

        if message == "/help":
            _show_help(console)
            continue

        if message.startswith("/"):
            _show_unknown_command(console, message)
            continue

        _show_not_connected(console)


def build_parser(
    package_version: str,
) -> argparse.ArgumentParser:
    """Create the EvoCode CLI argument parser."""

    parser = argparse.ArgumentParser(
        prog="evocode",
        description="EvoCode terminal coding agent.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {package_version}",
    )

    return parser


def main(
    argv: list[str] | None = None,
) -> int:
    """Start the EvoCode CLI."""

    package_version = version("evocode")

    parser = build_parser(package_version)
    parser.parse_args(argv)

    console = Console(
        highlight=False,
        soft_wrap=True,
    )

    show_welcome(
        console=console,
        package_version=package_version,
    )

    return interact(console)