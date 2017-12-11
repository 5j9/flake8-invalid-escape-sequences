from subprocess import Popen, PIPE
from unittest import TestCase, main


class PluginTest(TestCase):

    """Test the plugin."""

    def test_plugin(self):
        """Run the plugin on test_case.py."""
        # Fist see that the plugin actually exists
        popen = Popen(
            args=['python', '-m', 'flake8', '--version'],
            stdout=PIPE,
            universal_newlines=True,
        )
        stdout_data, stderr_data = popen.communicate()
        assert stderr_data is None
        self.assertIn(
            'flake8_invalid_escape_sequences',
            stdout_data,
            'it seems that flake8_invalid_escape_sequences is not installed',
        )
        popen = Popen(
            args=[
                'python', '-m', 'flake8', '--select=IES', '--ignore=H,E,D,N,F',
                'test_case.py'
            ],
            stdout=PIPE,
            universal_newlines=True,
        )
        stdout_data, stderr_data = popen.communicate()
        assert stderr_data is None
        self.assertEqual(
            stdout_data,
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
