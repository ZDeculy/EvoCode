import unittest
from importlib.metadata import version


class PackageTests(unittest.TestCase):
    def test_installed_version(self):
        self.assertRegex(version('evocode'), r'^\d+\.\d+\.\d+')


class InteractionTests(unittest.TestCase):
    def run_shell(self, entries):
        import io
        from unittest.mock import patch
        from rich.console import Console
        from evocode.cli import interact
        output = io.StringIO()
        with patch('builtins.input', side_effect=entries):
            status = interact(Console(file=output, color_system=None))
        self.assertEqual(status, 0)
        return output.getvalue()

    def test_multiple_inputs_and_commands(self):
        output = self.run_shell(['', '  ', 'one', '[red]', 'three', '/help', '/unknown', '/exit'])
        self.assertEqual(output.count('Model is not connected yet.'), 3)
        self.assertIn('/exit  Exit EvoCode', output)
        self.assertIn('Unknown command.', output)

    def test_interrupt_and_eof(self):
        for event in (EOFError(), KeyboardInterrupt()):
            with self.subTest(event=type(event).__name__):
                self.run_shell([event])


class StartupTests(unittest.TestCase):
    def test_help_and_version_do_not_prompt(self):
        import io
        from contextlib import redirect_stdout
        from unittest.mock import patch
        from evocode.cli import main
        for option, expected in [('--help', 'usage:'), ('--version', version('evocode'))]:
            with self.subTest(option=option), patch('builtins.input') as prompt:
                output = io.StringIO()
                with redirect_stdout(output), self.assertRaises(SystemExit) as result:
                    main([option])
                self.assertEqual(result.exception.code, 0)
                self.assertIn(expected, output.getvalue())
                prompt.assert_not_called()

    def test_startup_metadata(self):
        from pathlib import Path
        from unittest.mock import patch
        from evocode.cli import main
        with patch('evocode.ui.show_welcome') as welcome, patch('evocode.cli.interact', return_value=0):
            self.assertEqual(main([]), 0)
        self.assertEqual(welcome.call_args.args[1:], (version('evocode'),))


class EntryPointTests(unittest.TestCase):
    def run_cli(self, args=(), data='', cwd=None):
        import os
        import subprocess
        import sys
        from pathlib import Path
        executable = Path(sys.executable).parent / 'evocode'
        return subprocess.run([str(executable), *args], input=data, text=True,
                              capture_output=True, cwd=cwd, timeout=10,
                              env={**os.environ, 'NO_COLOR': '1'})

    def test_entry_point_session_and_eof(self):
        for ending in ('/exit\n', ''):
            with self.subTest(ending=ending):
                result = self.run_cli(data='one\ntwo\nthree\n/help\n/unknown\n' + ending)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.count('Model is not connected yet.'), 3)
                self.assertIn('Not configured', result.stdout)
                self.assertIn('Unknown command.', result.stdout)
                self.assertNotIn('\x1b', result.stdout)
                self.assertEqual(result.stderr, '')

    def test_entry_point_in_other_directory_and_options(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory(prefix='evocode-') as directory:
            result = self.run_cli(data='/exit\n', cwd=directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('EvoCode', result.stdout)
        for flag in ('--help', '--version'):
            result = self.run_cli([flag])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn('Welcome to', result.stdout)
