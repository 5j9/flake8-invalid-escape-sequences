from subprocess import Popen, PIPE
from unittest import TestCase, main


class PluginTest(TestCase):

    """Test the plugin."""

    def test_plugin(self):
        """Run the plugin on test_case.py."""
        popen = Popen(
            args=[
                'python', '-m', 'flake8', '--select=IES', '--ignore=H,E,D,N,F',
                'test_case.py'
            ],
            stdout=PIPE,
            universal_newlines=True,
        )
        popen.wait()
        self.assertEqual(
            popen.stdout.read(),
            'test_case.py:5:12: IES: invalid escape sequence \\[\n'
            'test_case.py:6:12: IES: invalid escape sequence \\[\n'
            'test_case.py:7:12: IES: invalid escape sequence \\[\n'
            'test_case.py:8:12: IES: invalid escape sequence \\[\n'
            'test_case.py:9:12: IES: invalid escape sequence \\[\n'
            'test_case.py:10:12: IES: invalid escape sequence \\[\n'
            'test_case.py:11:12: IES: invalid escape sequence \\[\n'
        )


if __name__ == '__main__':
    main()
