import io
import unittest

from rich.console import Console
from evocode.ui import show_welcome


class WelcomeTests(unittest.TestCase):
    def test_plain_header(self):
        output = io.StringIO()
        show_welcome(Console(file=output, width=80, height=24, color_system=None), '0.0.0')
        self.assertEqual(output.getvalue(),
                         '─' * 30 + '\nEvoCode\nVersion: 0.0.0\nModel: Not configured\n\n')
