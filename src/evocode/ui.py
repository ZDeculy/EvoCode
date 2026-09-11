"""EvoCode startup UI."""

from pathlib import Path

from rich import box
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text


PRIMARY = "#9AAED0"
ACCENT = "#F3A66A"
SECONDARY = "#9AA4B8"
BORDER = "#667085"


def _display_path() -> str:
    cwd = Path.cwd()
    home = Path.home()

    try:
        return f"~/{cwd.relative_to(home)}"
    except ValueError:
        return str(cwd)


def _title(package_version: str) -> Text:
    title = Text()

    title.append("Evo", style=f"bold {PRIMARY}")
    title.append("Code", style=f"bold {ACCENT}")
    title.append(f"   v{package_version}", style=SECONDARY)

    return title


def _info() -> Text:
    text = Text()

    text.append("Model    ", style=SECONDARY)
    text.append("Not configured\n", style=PRIMARY)

    text.append("Path     ", style=SECONDARY)
    text.append(f"{_display_path()}\n", style=PRIMARY)

    text.append("Mode     ", style=SECONDARY)
    text.append("Interactive (local)", style=PRIMARY)

    return text


def show_welcome(
    console: Console,
    package_version: str,
) -> None:

    divider = Text("─" * 48, style=BORDER)

    content = Group(
        _title(package_version),
        Text(""),
        divider,
        Text(""),
        _info(),
        Text(""),
        divider,
        Text(""),
        Text.from_markup(
            f"[{SECONDARY}]Type [/]"
            f"[{PRIMARY}]/help[/]"
            f"[{SECONDARY}] for commands   │   [/]"
            f"[{PRIMARY}]Ctrl+C / Ctrl+D[/]"
            f"[{SECONDARY}] to exit[/]"
        ),
    )

    console.print()

    console.print(
        Panel(
            content,
            box=box.HEAVY,
            border_style=BORDER,
            padding=(1, 2),
            expand=False,
        )
    )

    console.print()

    welcome = Text()
    welcome.append("❯ ", style=f"bold {ACCENT}")
    welcome.append("Welcome to ", style=SECONDARY)
    welcome.append("Evo", style=f"bold {PRIMARY}")
    welcome.append("Code", style=f"bold {ACCENT}")
    welcome.append("!", style=SECONDARY)

    console.print(welcome)
    console.print(
        Text("  What would you like to do?", style=SECONDARY)
    )
    console.print()